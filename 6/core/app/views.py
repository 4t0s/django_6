from django.shortcuts import render
from .models import Team, Player, dz

def home(request):
    
    team  = Team.objects.create(name = '1',
                                creation_year =  1,
                                sport = 'FB',
                                coach =  '1',
                                owner = '1')
    dz = dz.objects.create(test_list = [1,2])
    for i in range(1, 100):
        dz = dz.objects.create(test_list = [i])
    
    return render(request, 'home.html', context = {'team': team, 'dz': dz})