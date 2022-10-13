from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse
from django.utils.html import escape
from .movie import reverse_genres, genres


# Create your views here.

def home(request):
    return render(request, 'base/structure.html')

import requests


def form_submit(request):
    if request.method == 'POST':
        print(request.POST)
            # print(f'Value: {value}') in Python >= 3.7
        email = request.POST['mail'] 
        audiences = request.POST['audiences']
        ageranges = request.POST['age-ranges']
        gp = request.POST.getlist('gp')


        print(gp)
        genrestring = [] 
        for string in gp: 
            if(string != 'none'):
                genrestring.append(str(genres[string][0]))
        genrestring = ','.join(genrestring)
        languages = request.POST['Languages']
        x1 = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=34fe3fc711aaf02629366ba6335190d4&language={}&page=1&include_adult=false&with_genres={}&sort_by=popularity.desc".format(languages, genrestring))
        recommendations = []
        for o in x1.json()['results']:
            movie = {}
            movie['title'] = o['title']
            movie['genre'] = [reverse_genres[x] for x in o['genre_ids']]
            #print(o['title'])
            #print(o['original_language'])
            #print([reverse_genres[x] for x in o['genre_ids']])
            #print(o['popularity'])

            recommendations.append(movie)

    return render(request, 'base/display.html', {'recommendations':recommendations})
    

