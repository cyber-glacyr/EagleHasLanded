from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html', viability=is_viable())


def convert_to_cords(address):
    """
    convert address into latitude / longitude
    """
    latitude = ''
    longitude = ''
    api = "<<APIKEY>>"
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api}'

    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])

        for index, article in enumerate(articles[:3], start=1):
            print(f & quot; Article{index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n & quot;)
            else:
            print(f & quot;
            Error: {response.status_code} & quot;)
    return "location.latitude="+latitude + '&location.longitude=' + longitude

def is_viable():
    """
    - solar, price, and roofing
    """


def solar_viable(lat, long):
    """
    does the house get enough energy year-long?
    """


def price_viable(currentCost):
    """
    does the cost of solar outweigh the current cost of bills?
    """
    solarCost = 20000
