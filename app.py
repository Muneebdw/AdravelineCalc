from flask import Flask, render_template, request

app = Flask(__name__)

def get_mileage(vehicle):
    mileage = {
        'Car': 11, 'Prado': 5, 'Grand Cabin': 6, 'Coaster': 4, 'Bus': 2.6
    }
    return mileage.get(vehicle, 0)

def get_booking_cost(vehicle):
    booking_costs = {
        'Car': 5000, 'Prado': 8000, 'Grand Cabin': 9000, 'Coaster': 13000, 'Bus': 50000
    }
    return booking_costs.get(vehicle, 0)

def get_stay_cost(stay_type):
    stay_costs = {
        'Economy': 2000, 'Standard': 4000, 'Deluxe': 45000
    }
    return stay_costs.get(stay_type, 0)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        departure_city = request.form['departure_city']
        destination_city = request.form['destination_city']
        travel_mode = request.form['travel_mode']
        vehicle = request.form['vehicle']
        stay_type = request.form['stay_type']
        number_of_days = int(request.form['number_of_days'])
        distance = float(request.form['distance'])  # Assuming distance is provided directly from an API or input

        mileage = get_mileage(vehicle)
        booking_cost = get_booking_cost(vehicle)
        stay_cost = get_stay_cost(stay_type)

        # Calculate liters consumed
        liters_consumed = distance / mileage if mileage else 0

        # Calculate total costs
        total_travel_cost = liters_consumed * 150  # Assume 150 is current fuel price per liter
        total_vehicle_booking_cost = booking_cost * number_of_days
        total_stay_cost = stay_cost * number_of_days

        # Tolls
        tolls = 5000 if departure_city == 'Lahore' else 2000 if departure_city == 'Islamabad' else 0

        total_cost = total_travel_cost + total_vehicle_booking_cost + total_stay_cost + tolls

        result = f'Total Cost for the trip is: {total_cost}'
        return render_template('index.html', result=result, travel_mode=travel_mode)
    else:
        return render_template('index.html', result=None, travel_mode='By Road')

if __name__ == '__main__':
    app.run(debug=True)
