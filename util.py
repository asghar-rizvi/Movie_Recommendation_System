import json
import pickle
import requests

__model = None
__movie_names = None
__movie_id = None
def get_poster(movieid):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=5bd5ff699f711ced47f5fbcad8d0f06b&language=en-US".format(movieid))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']
def get_movie_names():
    return __movie_names

def loading_save_data():
    global __model
    global __movie_names
    global __movie_id
    # print('start')

    with open('model/model.pickle','rb') as f:
        __model = pickle.load(f)
    with open('model/movie_names.json','r') as f:
        __movie_names = json.load(f)['movie_name']
    with open('model/movie_id.json','r') as f:
        __movie_id = json.load(f)['movie_ids']
    # print('ending')

def recommend_movies(movie_name):
    list_rec = []
    list_poster=[]
    movie_index = __movie_names.index(movie_name)
    distances = __model[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        list_rec.append(__movie_names[i[0]])
        list_poster.append(get_poster(__movie_id[i[0]]))
    return list_rec, list_poster


if __name__=='__main__':
    loading_save_data()
    # print(get_movie_names())
    # print(recommend_movies('Batman'))
    # name_movie, poster_movie = recommend_movies('Batman')
    # print(name_movie)
    # print(poster_movie)