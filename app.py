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
# imdb_data = imdbjson['imdb_data']
imdb_df = pd.DataFrame(imdbjson)


imdb_df = imdb_df[['title', 'year', 'genre', 'duration', 'country', 'description', 'avg_vote']]


filepath_meta = os.path.join("Resources/metacritic_movies.json")
with open(filepath_meta) as jsonfile:
    metajson = json.load(jsonfile)

# meta_data = metajson['meta_data']
meta_df = pd.DataFrame(metajson)
print(meta_df.head())


meta_df = meta_df[['movie_title', 'metascore']]

app = Flask(__name__)


@app.route("/", methods=("POST", "GET"))
def welcome():

    return render_template("index.html")

@app.route("/api/v1.0/imdb_data")
def imdb_data():
    """Return the CoD data as json"""

    return jsonify(imdbjson)

@app.route("/api/v1.0/meta_data")
def causaMortis():
    """Return the CoD data as json"""

    return jsonify(metajson)
    
if __name__ == "__main__":
    app.run(debug=True)