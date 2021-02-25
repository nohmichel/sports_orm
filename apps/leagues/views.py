from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(name__contains='baseball'),
		"womens_leagues":League.objects.filter(name__contains='women'),
		"hockey_leagues":League.objects.filter(sport__contains='hockey'),
		"other_than_football":League.objects.exclude(sport='Football'),
		"conference_leagues":League.objects.filter(name__contains="conference"),
		"atlantic_leagues":League.objects.filter(name__contains="atlantic"),
		"dallas_teams":Team.objects.filter(location="Dallas"),
		"raptor_teams":Team.objects.filter(team_name__contains="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"starts_with_t": Team.objects.filter(team_name__startswith="T"),
		"ordered_by_loc":Team.objects.order_by('location'),
		"reversed_by_loc":Team.objects.order_by('-location'),
		"last_name_cooper":Player.objects.filter(last_name="Cooper"),
		"first_name_joshua": Player.objects.filter(first_name="Joshua"),
		"cooper_no_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_and_wyatt": Player.objects.filter(first_name__in=['Alexander','Wyatt']),

	}	
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")





