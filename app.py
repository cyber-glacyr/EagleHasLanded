from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    primary application
    """
    if request.method == 'POST':
        return render_template('result.html', viability=is_viable(), api_key=API_KEY)
    else:
        return render_template('form.html')


def convert_to_cords(address):
    """
    convert address into latitude / longitude
    """
    latitude = ''
    longitude = ''
    api = "<<APIKEY>>"
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api}'

    response = requests.get(url)
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
