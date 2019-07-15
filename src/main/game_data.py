#GAME DATA 
import numpy as np 
import pandas as pd
from ast import literal_eval
from django.conf import settings
from django.conf.urls.static import static
import os
import io

#GAME DATA FRAME
df = pd.read_csv(os.path.join(settings.BASE_DIR, "static/main/data/game_data.csv"))

#ALL GAME TITLES
game_titles = list(df['game_title'])