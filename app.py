from flask import Flask, render_template, request
from uber_delivery_trip import UberDeliveryTrip

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print("Entering the home function()")
    if request.method == 'POST':
        print("Receiving form data...")
        print("Form data:", request.form)
        
        distance = float(request.form['distance'])
        time = float(request.form['time'])
        total_fare = float(request.form['total_fare'])
        
        # Converting the gas price per liter to float, replacing ',' with '.' if necessary
        gas_price_per_liter = float(request.form['gas_price_per_liter'].replace(',', '.'))
        
        fuel_consumption = float(request.form['fuel_consumption'])

        print("Trip data:")
        print("Distance:", distance)
        print("Time:", time)
        print("Total Fare:", total_fare)
        print("Gas Price per Liter:", gas_price_per_liter)
        print("Fuel Consumption:", fuel_consumption)

        trip = UberDeliveryTrip(distance, time, total_fare, gas_price_per_liter, fuel_consumption)
        profit = trip.calculate_profit()

        print("Profit:", profit)

        return render_template('result.html', profit=profit)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
