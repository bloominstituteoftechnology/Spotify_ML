from spotify_app.spotify import get_song_by_title, get_audio_features
import pandas as pd
import numpy as np
from joblib import load

model = load('/Users/ryanallred/Projects/Spotify_ML/spotify_app/model.joblib')

# Columns of our X Matrix
# columns = ['popularity', 'duration_ms', 'explicit', 'danceability', 
#                   'energy', 'key', 'loudness', 'mode', 'speechiness', 
#                   'acousticness', 'instrumentalness', 'liveness', 'valence', 
#                   'tempo', 'time_signature', 'year']

def get_similar_songs(title):
    song = get_song_by_title(title)
    song_id = song['id']
    song_attributes = get_audio_features(song_id)


    row = [[song['popularity'], 
            song_attributes['duration_ms'],
            int(song['explicit']),
            song_attributes['danceability'],
            song_attributes['energy'],
            song_attributes['key'],
            song_attributes['loudness'],
            song_attributes['mode'],
            song_attributes['speechiness'],
            song_attributes['acousticness'],
            song_attributes['instrumentalness'],
            song_attributes['liveness'],
            song_attributes['valence'],
            song_attributes['tempo'],
            song_attributes['time_signature'],
            pd.to_datetime(song['year']).year]]

    distances, indices = model.kneighbors(row, 5)

    song_indices = pd.read_csv('https://raw.githubusercontent.com/ryanleeallred/datasets/master/song_indices.csv')

    return song_indices.iloc[indices[0]]['id'].values
    # print(np.array([song_indices.iloc[song]['id'].values for song in indices]))
        
    
