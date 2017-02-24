from flask import Flask, request, render_template, jsonify
import requests
import logging
import json

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/api/lookup/<id>")
def get_id(id):
    params = get_params_for_id(id)
    return params

def get_params_for_id(id):

    headers = {
    'client_id' : 'e5a29d5e4e244c9889d19c5e89f05bcf',
    'client_secret' : '360a2abef6e448ed98bb568baf146cf9',
    'redirect_uri' : 'http://127.0.0.1/5000/callback'
    }

    response = requests.get("https://api.spotify.com/v1/tracks/" + id, headers = headers)

    response = response.json()
    print response

    artists = response["artists"]

    # for a in artists:
    #     nombre = a["name"]

    # print nombre
    return render_template("trackid.html", **response)


@app.route("/api/search")
def get_song():
    q = request.args.get("q")
    types = request.args.get("type")

    params = get_params_for_this(q, types)
    return params

def get_params_for_this(q, types):

    headers = {
    'client_id' : 'e5a29d5e4e244c9889d19c5e89f05bcf',
    'client_secret' : '360a2abef6e448ed98bb568baf146cf9',
    'redirect_uri' : 'http://127.0.0.1/5000/callback'
    }

    response = requests.get("https://api.spotify.com/v1/search?q=" + q + "&type=" + types, headers = headers)
    response = response.json()
    array = json.dumps(response)

    data = json.loads(array)



    #print response



    print data['tracks'][0]['items'][0]['album'][0]['name']

    return render_template("search.html", **response)



if __name__ == "__main__":
    app.run(debug = True)
