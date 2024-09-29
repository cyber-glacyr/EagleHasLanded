from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html', viability=is_viable())

def is_viable():
    """
    - solar, price, and roofing
    """


def solar_viable(lat, long):
    """
    does the house get enough energy year-long?
    """
    api = ""
    url = f'curl -X GET "https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={long}&requiredQuality=HIGH&key={api}"'
    response = requests.get(url)

    if response.status_code == 200:
        # Printing the JSON response
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


def price_viable(currentCost):
    """
    does the cost of solar outweigh the current cost of bills?
    """
    solarCost = 20000
