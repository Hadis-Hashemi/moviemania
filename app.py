import pandas as pd
import json as json
from pandas.io.json import json_normalize
from flask import Flask, jsonify, render_template
import os

# Join file from resources
filepath_imdb = os.path.join("Resources/imdb_movies.json")
with open(filepath_imdb) as jsonfile:
    imdbjson = json.load(jsonfile)

# Convert to dataframe
imdb_data = imdbjson['imdb_data']
imdb_df = pd.DataFrame(imdb_data)

imdb_title_id = imdb_df[0]
title = imdb_df[1]
year = imdb_df[3]
genre = imdb_df[5]
duration = imdb_df[6]
country = imdb_df[7]
description = imdb_df[13]
avg_vote = imdb_df[14]

imdb_df = pd.DataFrame({"title": title,
                        "year": year,
                        "genre": genre,
                        "duration": duration,
                        "country": country,
                        "description": description,
                        "avg_vote": avg_vote})


filepath_meta = os.path.join("Resources/imdb_movies")
with open(filepath_meta) as jsonfile:
    metajson = json.load(jsonfile)

meta_data = metajson['meta_data']
meta_df = pd.DataFrame(meta_data)

movie_title = meta_df[0]
metascore = meta_df[6]

imdb_df = pd.DataFrame({"movie_title": movie_title,
                        "metascore": metascore})

app = Flask(__name__)


@app.route("/", methods=("POST", "GET"))
def welcome():

if __name__ == "__main__":
    app.run(debug=True)