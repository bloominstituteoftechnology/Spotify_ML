# Spotify_ML

### Startup Instructions

1) Clone the repository and change directories to the outer project folder:

`cd Spotify_ML`

2) Ensure that all dependencies are properly installed:

 `pipenv install`

3) Activate the virtual enviroment with:

`pipenv shell`

4) Start up the Flask app.

`flask run`

5) Obtain [API keys from Spotify.](https://developer.spotify.com/dashboard/login) and put them in a `.env` file

`touch .env`

```
FLASK_APP=spotify_app
FLASK_ENV=development
CLIENT_ID=YOUR_CLIENT_ID_HERE
CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE
```

6) Visit the `/reset` route to generate the `db.sqlite3` file.

[127.0.0.1:5000/reset](http://127.0.0.1:5000/reset)

Before this app will fully work you will need to export the trained Nearest Neighbors model found in [this Colab Notebook](https://colab.research.google.com/drive/1f4onAZsSDUcG9hgZJczvcDjk0XXT1L0w?usp=sharing). We will be doing this together during the Code-Along.
