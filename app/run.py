from flask import Flask, request, Response
from flask_cors import CORS
import requests

import config

app = Flask(__name__)
CORS(app)

URL = "https://api.yelp.com/v3/businesses/search"
headers = {'Authorization': f"Bearer {config.API_KEY}"}


@app.route('/')
def ramen_yelp():
    payload = {
        "term": request.args.get("term", "ramen"),
        "location": request.args.get("location", "ny")
    }
    response = requests.request("GET", URL, headers=headers, params=payload)

    return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
