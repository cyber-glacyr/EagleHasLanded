from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/validity", methods=['GET', 'POST'])
def validity():
    """
    primary application
    """
    if request.method == 'POST':
        name = request.form.get('name')
        latitude = request.form.get('lat')
        longitude = request.form.get('lng')
        roofing_health = request.form.get('roofing_health')
        roofing_type = request.form.get('roofing_type')
        elec_cost = request.form.get('elec_cost')
        return render_template('result.html', viability=is_viable(name, latitude, longitude, roofing_health, roofing_type, elec_cost))
    else:
        return render_template('form.html')

def is_viable(name, latitude, longitude, roofing_health, roofing_type, energy_price):
    """
    - solar, price, and roofing
    """
    solar = solar_viable(latitude, longitude)
    roofing = roofing_viable(roofing_health, roofing_type)
    price = price_viable(float(energy_price))
    if not solar[0]:
        return (f"Not viable.\nAt {name}, there is not enough light with only {int(solar[1])} solar hours a year. 1460 solar hours are "
                f"minimum.")
    if not roofing[0]:
        return (f"Not viable.\nIt's important that your roof is healthy and will last long in order to install solar. "
                f"However, you do get enough sunlight, so consider installing a new roof, making sure it is Asphalt "
                f"Shingles, Metal, Tile, Tar and Gravel, or Composite.")
    if not roofing[1]:
        return (f"Not viable.\nCertain types of roofs are incompatible, including your {roofing_type} roof. However, "
                f"you do get enough sunlight, so consider installing a new roof, making sure it is Asphalt Shingles, "
                f"Metal, Tile, Tar and Gravel, or Composite.")
    else:
        return (f"Viable!\nYour house gets {int(solar[1])} solar hours a year, more than the 1460 necessary. You have "
                f"healthy roofing that is {roofing_type}. At an average household installation cost of £9600 ("
                f"converted into your local currency), you will break even in {round(price, 2)} months, and then you "
                f"will be saving £{energy_price} a month. However, this is for a three bedroom house so you will have "
                f"to consider factors like house size. Additional factors to consider, are government solar "
                f"incentives, whether there are good local installation businesses, and current supply chain issues. Price will also vary based on country and tax code, and maintenance costs need to be considered.")


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
        json_object = json.dumps(final, indent=2)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

        with open("sample.json", mode="r", encoding="utf-8") as read_file:
            solarHours = json.load(read_file)
        solarHours = json.loads(solarHours)
        return solarHours["solarPotential"]["maxSunshineHoursPerYear"] > 1460, solarHours["solarPotential"]["maxSunshineHoursPerYear"]
    else:
        print(f"Error: {response.status_code}")



def price_viable(currentCost):
    """
    does the cost of solar outweigh the current cost of bills?
    """
    solarCost = 9600
    return solarCost / currentCost


def roofing_viable(roofing_health, roofing_type):
    """
    Is the roofing suitable
    """
    return roofing_health, roofing_type in ["Asphalt Shingles", "Metal", "Tile", "Tar and Gravel", "Composite"]


def test():
    solar_viable(37.4449439, -122.13914659999998)


if __name__ == '__main__':
    test()