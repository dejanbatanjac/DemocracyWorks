# Importing flask
from flask import Flask, request, render_template, redirect
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'seek_rhett'


@app.route('/', methods=['GET', 'POST'])
def index():
    """Return homepage"""
    return render_template("index.html")


@app.route('/results', methods=['POST', 'GET'])
def results():
    """get results based on address"""
    place = request.form["place"]
    state = request.form["state"]
    # url = "https://api.turbovote.org/elections/upcoming?place=" + place + "&state=" + state
    #print(url)
    url = "https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland
"
    res = requests.get(url)
    res.headers["Content-Type"] = "json"
    print(res.json)
    return res.json()
    



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
