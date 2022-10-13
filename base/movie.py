import requests
#
genres = {}
reverse_genres = {}
allin = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=34fe3fc711aaf02629366ba6335190d4&language=en-US").json()['genres']
genres['none'] = -1
for x in allin:
    genres[x['name']] = (x['id'], x['name'])
    reverse_genres[x['id']] = x['name']