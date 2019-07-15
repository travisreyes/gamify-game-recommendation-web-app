from django import forms

from .models import Game

from .game_data import game_titles

#Form for video game title inputs
class RecommendationForm(forms.ModelForm):
    firstGame = forms.CharField(label="", required="False",
        widget = forms.TextInput(
            attrs={
                "class":"first-box",
                "placeholder": "Type a video game title here",
            }))
    secondGame = forms.CharField(label="", required=False,
        widget = forms.TextInput(
            attrs={
                "class":"second-box",
                "placeholder": "Type a video game title here",
            }))
    thirdGame = forms.CharField(label="", required=False,
        widget = forms.TextInput(
            attrs={
                "class":"third-box",
                "placeholder": "Type a video game title here",
            }))
    class Meta:
        model = Game 
        fields = [
            'firstGame',
            'secondGame',
            'thirdGame',
        ]


        