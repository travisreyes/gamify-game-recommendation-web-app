from django.shortcuts import render, get_object_or_404, redirect

from .models import Game

from .forms import RecommendationForm

from .recommendation_engine import recommend

from .game_data import game_titles

from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home_view(request, *args, **kwargs):
	form = RecommendationForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RecommendationForm()
		return redirect('recommendations/')
	context = {
		'form' : form
	}
	return render(request, "base.html", context)

def recommend_view(request, *args, **kwargs):
	titles = Game.objects.latest('id')
	context ={
		"user_titles": [titles.firstGame,titles.secondGame,titles.thirdGame],
		"lists": recommend(titles.firstGame, titles.secondGame, titles.thirdGame)
	}
	return render(request, "recommend_page.html",context)