from flask import Flask, request, render_template, jsonify
import util

app = Flask(__name__)
util.loading_save_data()


@app.route('/')
def home_page():
    return render_template('index.html',options=util.get_movie_names())

@app.route('/recommend', methods=['GET', 'POST'])
def show_recommend():
    movie_name = request.form['movie_search']
    names, posters = util.recommend_movies(movie_name)
    recommendations = list(zip(names, posters))
    return render_template('index.html', options=util.get_movie_names(), recommendations=recommendations)
if __name__=='__main__':
    app.run(debug=True)