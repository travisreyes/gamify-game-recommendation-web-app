#RECOMMENDATION ENGINE
import numpy as np 
import pandas as pd
from ast import literal_eval
from django.conf import settings
from django.conf.urls.static import static
import os
import io

def recommend(first,second,third):

    game_data_df = pd.read_csv(os.path.join(settings.BASE_DIR, "static/main/data/game_data.csv"))
    game_data_df = game_data_df[['game_title', 'genre', 'platforms', 'developers', 'release_year', 'release_month', 'release_day','average_metascore_ratings']]

    for column in ['genre', 'platforms', 'developers']:
        game_data_df[column] = game_data_df[column].apply(literal_eval)

    #Game Titles inputted by user
    user_input = [first, second, third]

    def user_game_data(df,titles):
        data_frame = df[df["game_title"].isin(titles)]
        data_frame.index = range(len(data_frame.index))
        return data_frame

    #Data frame generated from grabbing data
    user_df = user_game_data(game_data_df, user_input)

    #Prints out inputted video games
    print(user_df['game_title'])

    def count_items(df,title):
        dic = {}
        column = df[title]
        for row in column:
            for item in row:
                if item not in dic:
                    dic[item] = 1
                else:
                    dic[item] +=1
        return pd.DataFrame({title : list(dic.keys()), "count": list(dic.values())}).sort_values(by='count', ascending = False)

    def weighted_distances(u_df, meta_df):
        meta_df_length = len(meta_df)
        user_genres = count_items(u_df, 'genre')
        user_platforms = count_items(u_df, 'platforms')
        user_developers = count_items(u_df, 'developers')
    
        # Helper Functions
        def count_weighted(column, category):
            items = list(category.iloc[:,0])
            array = []
            for row in column:
                count = 0
                for item in items:
                    if item in row:
                        count += list(category.loc[category[category.columns[0]] == item]['count'])[0]
                array.append(count)  
            return array
        
        def find_distance():
            genre_similar_counts = np.array(count_weighted(list(meta_df['genre']),user_genres))
            platform_similar_counts = np.array(count_weighted(list(meta_df['platforms']),user_platforms))
            developer_similar_counts = np.array(count_weighted(list(meta_df['developers']),user_developers))
            distance_array = []
            
            for i in range(meta_df_length):
                sqr_diff_genres = np.square(sum(list(user_genres['count'])) - genre_similar_counts[i])
                sqr_diff_platforms = np.square(sum(list(user_platforms['count'])) - platform_similar_counts[i])
                sqr_diff_developers = np.square(sum(list(user_developers['count'])) - developer_similar_counts[i])
                distance = np.sqrt(sqr_diff_genres + sqr_diff_platforms  + sqr_diff_developers)
                distance_array.append(distance)
            return distance_array

        return pd.DataFrame({'game_title' :list(meta_df['game_title']), 'distance': find_distance() }).sort_values(by='distance')

    def recommend_weighted(u_df, meta_df):
        suggest_df = meta_df[-meta_df["game_title"].isin(user_input)]
        suggest_df = suggest_df[suggest_df.average_metascore_ratings >= 80]
        distances_df = weighted_distances(u_df, suggest_df)
        return distances_df[['game_title']]

    recommended_titles = list(recommend_weighted(user_df,game_data_df)['game_title'][0:20])

    recommended_games_df = user_game_data(game_data_df,recommended_titles).head(20)

    recommended_games_df = recommended_games_df[['game_title', 'genre', 'platforms', 'developers', 'average_metascore_ratings']]

    return recommended_games_df.values.tolist()

