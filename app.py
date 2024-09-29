from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    primary application
    """
    if request.method == 'POST':
        name = request.form['name']
        latitude = request.form['lat']
        longitude = request.form['lng']
        return render_template('result.html', viability=is_viable())
    else:
        return render_template('form.html')

def is_viable():
    """
    - solar, price, and roofing
    """


def solar_viable(lat, long):
    """
    does the house get enough energy year-long?
    """
    api = ""
    url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={lat}&location.longitude={long}&requiredQuality=HIGH&key={api}"
    response = requests.get(url)

    if response.status_code == 200:
        # Printing the JSON response
        js = response.json()
        final = json.dumps(js)
        json_object = json.dumps(final, indent=4)
        print(json_object)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        with open("sample.json", mode="r", encoding="utf-8") as read_file:
            solarHours = json.load(read_file)
        print(solarHours["solarPotential"]["maxSunshineHoursPerYear"])
    else:
        print(f"Error: {response.status_code}")



def price_viable(currentCost):
    """
    does the cost of solar outweigh the current cost of bills?
    """
    solarCost = 20000


def test():
    solar_viable(37.4449439, -122.13914659999998)


if __name__ == '__main__':
    test()