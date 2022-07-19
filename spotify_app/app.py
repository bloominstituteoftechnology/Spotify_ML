from flask import Flask, render_template, request, url_for
from .spotify import get_song_by_title
from .models import DB, RecentSearches
from .predict import get_similar_songs
# import pandas as pd
# from os.path import relpath

import warnings
warnings.filterwarnings("ignore")

def create_app():

    app = Flask(__name__) 

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/', methods=['POST', 'GET'])
    def root():
        if request.method == "GET": 
            # get 5 most recent searches
            recent = RecentSearches.query.all()[-5:]
            # reverse list and display on the page
            return render_template('base.html', recent_searches=recent[::-1])
        elif request.method == 'POST':

            song_title = request.values['song_title']
            song = get_song_by_title(song_title)
            if song:
                try: 
                    db_song = RecentSearches(song_id=song['id'],
                                            title=song['title'],
                                            href=song['href'],
                                            uri=song['uri'])
                    DB.session.add(db_song)
                except Exception as e:
                    print(f'Error processing {song_title}: {e}')
                    raise e
                else:
                    DB.session.commit()
                    # get 5 most recent searches
                    recent = RecentSearches.query.all()[-5:]
                    # reverse list and display on the page
                    return render_template('base.html', recent_searches=recent[::-1], message='')
            else:
                # get 5 most recent searches
                recent = RecentSearches.query.all()[-5:]
                message = "Sorry, we couldn't find a song with that title."
                return render_template('base.html', recent_searches=recent[::-1], message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html')

    @app.route('/predict')
    def predict():

        predictions = get_similar_songs('Hey Macarena!')
        print(predictions)

        return render_template('base.html', predictions=predictions)

    return app






