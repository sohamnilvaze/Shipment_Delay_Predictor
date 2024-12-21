import pandas as pd

#Function to suggest truck vehicle type
def suggest_truck(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,traffic_conditions_light,traffic_conditions_moderate):
    vehicle_lorry=[0]
    vehicle_trailer=[0]
    vehicle_truck=[1]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction
#Function to suggest lorry vehicle type
def suggest_lorry(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,traffic_conditions_light,traffic_conditions_moderate):
    vehicle_lorry=[1]
    vehicle_trailer=[0]
    vehicle_truck=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest trailer vehicle type
def suggest_trailer(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,traffic_conditions_light,traffic_conditions_moderate):
    vehicle_lorry=[0]
    vehicle_trailer=[1]
    vehicle_truck=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest conatiner vehicle type
def suggest_container(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,traffic_conditions_light,traffic_conditions_moderate):
    vehicle_lorry=[0]
    vehicle_trailer=[0]
    vehicle_truck=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest light traffic conditions
def suggest_light_traffic(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,vehicle_lorry,vehicle_truck,vehicle_trailer):
    traffic_conditions_light=[1]
    traffic_conditions_moderate=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest moderate traffic conditions
def suggest_moderate_traffic(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,vehicle_lorry,vehicle_truck,vehicle_trailer):
    traffic_conditions_light=[0]
    traffic_conditions_moderate=[1]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest heavy traffic conditions
def suggest_heavy_traffic(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,weather_conditions_fog,weather_conditions_rain,weather_conditions_storm,vehicle_lorry,vehicle_truck,vehicle_trailer):
    traffic_conditions_light=[0]
    traffic_conditions_moderate=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest light weather conditions
def suggest_light_weather(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,traffic_conditions_light,traffic_conditions_moderate,vehicle_lorry,vehicle_trailer,vehicle_truck):
    weather_conditions_fog=[0]
    weather_conditions_rain=[0]
    weather_conditions_storm=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest foggy weather conditions
def suggest_fog_weather(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,traffic_conditions_light,traffic_conditions_moderate,vehicle_lorry,vehicle_trailer,vehicle_truck):
    weather_conditions_fog=[1]
    weather_conditions_rain=[0]
    weather_conditions_storm=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest rain weather conditions
def suggest_rain_weather(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,traffic_conditions_light,traffic_conditions_moderate,vehicle_lorry,vehicle_trailer,vehicle_truck):
    weather_conditions_fog=[0]
    weather_conditions_rain=[1]
    weather_conditions_storm=[0]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction

#Function to suggest storm weather conditions
def suggest_storm_weather(model,origin_input,dest_input,distance,delay_days,shipment_year,shipment_month,shipment_day,traffic_conditions_light,traffic_conditions_moderate,vehicle_lorry,vehicle_trailer,vehicle_truck):
    weather_conditions_fog=[0]
    weather_conditions_rain=[0]
    weather_conditions_storm=[1]
    data=pd.DataFrame({"Origin":origin_input,"Destination":dest_input,"Distance (km)":distance,"Delivery Delay":delay_days,"Shipment Year":shipment_year,"Shipment Month":shipment_month,"Shipment Day":shipment_day,"Weather Conditions_Fog":weather_conditions_fog,"Weather Conditions_Rain":weather_conditions_rain,"Weather Conditions_Storm":weather_conditions_storm,"Traffic Conditions_Light":traffic_conditions_light,"Traffic Conditions_Moderate":traffic_conditions_moderate,
                       "Vehicle Type_Lorry":vehicle_lorry,"Vehicle Type_Trailer":vehicle_trailer,"Vehicle Type_Truck":vehicle_truck})
    
    prediction=model.predict(data)
    return prediction








    