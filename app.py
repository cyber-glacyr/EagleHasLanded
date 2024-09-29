from flask import Flask, render_template

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
    return latitude + ',' + longitude


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
