from flask import Flask, render_template, request
import joblib
import datetime
import pandas as pd
import numpy as np
from functions import load_model,process_delivery_dates,process_shipment_date,process_origin,process_destination,process_weather,process_traffic,process_vehicle_type

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model/model.pkl')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    origin = request.form['origin']
    destination = request.form['destination']
    shipment_date=request.form['shipment_date']
    planned_delivery_date=request.form['planned_delivery_date']
    actual_delivery_date=request.form['actual_delivery_date']
    vehicle = request.form['vehicle']
    distance = int(request.form['distance'])
    weather = request.form['weather']
    traffic = request.form['traffic']

    delay_days=process_delivery_dates(planned_delivery_date,actual_delivery_date)
    shipment_year,shipment_month,shipment_day=process_shipment_date(shipment_date)
    origin_input=process_origin(origin)
    dest_input=process_destination(destination)
    weather_conditions_fog,weather_conditions_rain,weather_conditions_storm=process_weather(weather)
    traffic_conditions_light,traffic_conditions_moderate=process_traffic(traffic)
    vehicle_lorry,vehicle_trailer,vehicle_truck=process_vehicle_type(vehicle)
    
    
    origin_input=[origin_input]
    dest_input=[dest_input]
    distance=[distance]
    delay_days=[delay_days]
    shipment_year=[shipment_year]
    shipment_month=[shipment_month]
    shipment_day=[shipment_day]
    weather_conditions_fog=[weather_conditions_fog]
    weather_conditions_rain=[weather_conditions_rain]
    weather_conditions_storm=[weather_conditions_storm]
    traffic_conditions_light=[traffic_conditions_light]
    traffic_conditions_moderate=[traffic_conditions_moderate]
    vehicle_lorry=[vehicle_lorry]
    vehicle_trailer=[vehicle_trailer]
    vehicle_truck=[vehicle_truck]
    
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    
    if prediction==0:
        result="The shipment will be on time."
    else:
        result="The shipment will be delayed."

    # Render result template
    return render_template('result.html', result=result)

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
