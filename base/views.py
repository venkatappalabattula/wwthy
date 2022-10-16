from importlib.abc import FileLoader
from msilib.schema import RadioButton
from multiprocessing import context
from tkinter import Y
from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse
from django.utils.html import escape
from .movie import reverse_genres, genres
from base.models import forminput, singleforminput
from django.http import HttpResponse
from django.template import loader
import json 

# Create your views here.
def landing(request):
    return render(request, 'base/landing.html')

def multiple(request):
    return render(request, 'base/multiple.html')

def single(request):
    return render(request, 'base/single.html')

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

        ins = forminput(email=email, audiences = audiences, ageranges = ageranges, gp = gp, recommendations = recommendations)
        ins.save()
        print("The data has been written to the db")  
    return render(request, 'base/display.html', {'recommendations':recommendations})
    

def single_form(request):
    if request.method == 'POST':
        print(request.POST)
            # print(f'Value: {value}') in Python >= 3.7
        email = request.POST['mail'] 
        age = request.POST['age']
        gp = request.POST.getlist('gp')

    # radio = []
    # x = 0 
    # for i in range(0,13):
    #     radio = "radio"+str(i)
    #     radio= request.POST["radio"]
    #     # print(radio)
    #     x = x + int(radio[0])
    #     # print(x)
    #     i = i+1

    




        radio = request.POST['radio']
        radio1 = request.POST['radio1']
        radio2 = request.POST['radio2']
        radio3 = request.POST['radio3']
        radio4 = request.POST['radio4']
        radio5 = request.POST['radio5']
        radio6 = request.POST['radio6']
        radio7 = request.POST['radio7']
        radio8 = request.POST['radio8']
        radio9 = request.POST['radio9']
        radio10 = request.POST['radio10']
        radio11 = request.POST['radio11']
        radio12 = request.POST['radio12']
        # print(radio12)
        # y = int(radio12)
        # print(y)

        sum = int(radio) + int(radio1) + int(radio2) + int(radio3) + int(radio4) + int(radio5)+int(radio6) + int(radio7) + int(radio8) + int(radio9) + int(radio10) + int(radio11) + int(radio12)
        print(sum)
    

        # Scoring a 12 or higher on the short version may indicate the presence of depression in the respondent.


        # print(gp)
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
            # print(o['popularity'])
            recommendations.append(movie)     

        singleinput = singleforminput( email=email, age = age, gp = gp, recommendations = recommendations, sum = sum)
        singleinput.save()
        print("The data has been written to the db")  
    return render(request, 'base/displaysingle.html', {'recommendations':recommendations, 'sum':sum})



# def tictac(request):
#     return render(request, 'base/tictactoe.html')

# def wordle(request):
#     return render(request, 'base/wordle.html')


