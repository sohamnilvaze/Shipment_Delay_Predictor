import pandas as pd

def load_model():
    model = joblib.load('model/model.pkl')
    import joblib

def process_delivery_dates(planned_delivery_dates,actual_delivery_dates):
    planned_delivery_date=pd.to_datetime(planned_delivery_date)
    actual_delivery_date=pd.to_datetime(actual_delivery_date)
    delay_days=(actual_delivery_date - planned_delivery_date).days

    return delay_days

def process_shipment_date(shipment_date):
    shipment_date=pd.to_datetime(shipment_date)
    shipment_year=shipment_date.year
    shipment_month=shipment_date.month
    shipment_day=shipment_date.day

    return shipment_year,shipment_month,shipment_day

def process_origin(origin):
    origin_input=0.0

    if(origin=='Ahmedabad'):
        origin_input=0.739747
    elif(origin=='Banglore'):
        origin_input=0.738916
    elif(origin=='Chennai'):
        origin_input=0.747852
    elif(origin=='Delhi'):
        origin_input=0.732256
    elif(origin=='Hyderabad'):
        origin_input=0.739504
    elif(origin=='Jaipur'):
        origin_input=0.742257
    elif(origin=='Kolkata'):
        origin_input=0.732387
    elif(origin=='Lucknow'):
        origin_input=0.729069
    elif(origin=='Mumbai'):
        origin_input=0.733879
    elif(origin=='Pune'):
        origin_input=0.742560

    return origin_input

def process_destination(destination):
    dest_input=0.0

    if(destination=='Ahmedabad'):
        dest_input=0.746521
    elif(destination=='Banglore'):
        dest_input=0.739173
    elif(destination=='Chennai'):
        dest_input=0.725759
    elif(destination=='Delhi'):
        dest_input=0.735116
    elif(destination=='Hyderabad'):
        dest_input=0.761393
    elif(destination=='Jaipur'):
        dest_input=0.724560
    elif(destination=='Kolkata'):
        dest_input=0.744078
    elif(destination=='Lucknow'):
        dest_input=0.728304
    elif(destination=='Mumbai'):
        dest_input=0.734818
    elif(destination=='Pune'):
        dest_input=0.740070
    
    return dest_input

def process_weather(weather):
    weather_conditions_fog=0
    weather_conditions_rain=0
    weather_conditions_storm=0

    if(weather=='Rain'):
        weather_conditions_rain=1
    elif(weather=='Storm'):
        weather_conditions_storm=1
    elif(weather=='Fog'):
        weather_conditions_fog=1

    return weather_conditions_fog,weather_conditions_rain,weather_conditions_storm

def process_traffic(traffic):
    traffic_conditions_light=0
    traffic_conditions_moderate=0

    if(traffic=='Moderate'):
        traffic_conditions_moderate=1
    elif(traffic=='Light'):
        traffic_conditions_light=1

    return traffic_conditions_light,traffic_conditions_moderate

def process_vehicle_type(vehicle):
    vehicle_lorry=0
    vehicle_truck=0
    vehicle_trailer=0

    if(vehicle=='Lorry'):
        vehicle_lorry=1
    elif(vehicle=='Truck'):
        vehicle_truck=1
    elif(vehicle=='Trailer'):
        vehicle_trailer=1
    
    return vehicle_lorry,vehicle_trailer,vehicle_truck
