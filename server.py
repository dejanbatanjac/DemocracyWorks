# Importing flask
from flask import Flask, request, render_template, redirect
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "seek_rhett"


@app.route("/", methods=["GET", "POST"])
def index():
    """Return homepage"""
    return render_template("index.html")


@app.route("/results", methods=["POST", "GET"])
def results():
    """get results based on address"""
    place = request.form["place"].lower().replace(" ", "_")
    state = request.form["state"].lower()

    url = "https://api.turbovote.org/elections/upcoming"
    querystring = {}
    querystring["district-divisions"] = (
        "ocd-division/country:us/state:"
        + state
        + ",ocd-division/country:us/state:"
        + state
        + "/place:"
        + place
    )
    print(querystring)
    headers = {"Accept": "application/json", "cache-control": "no-cache"}

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response)
        return
    except Exception as err:
        return print(f"Exception: {err}")
        raise


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
