import pandas as pd
from helpers.haversine import calc_dist_with_haversine
from helpers.content import get_data 

def calc_restaurant_to_delivery_distance_by_row(row):
    restaurant_location = row[['Restaurant_longitude', 'Restaurant_latitude']]
    delivery_location = row[['Delivery_location_longitude','Delivery_location_latitude']]

    return calc_dist_with_haversine(restaurant_location,delivery_location)

def average_speed_by_distance_and_time(total_kilometers: float, total_time: float):
    return total_kilometers / total_time

def estimate_time_by_estimators(total_distance: float,
                                type_of_vehicle: str = "scooter",
                                condition: int = 1,
                                weather: str = "conditions Sunny",
                                traffic_condition: str = "Low"):
    
    data_of_interest = get_data()

    data_of_interest["distance_km"] = data_of_interest.apply(calc_restaurant_to_delivery_distance_by_row, axis=1)
    data_of_interest["Time_taken(min)"] = pd.to_numeric(data_of_interest["Time_taken(min)"].str.replace('(min)',''), errors="coerce")

    vehicle = data_of_interest["Type_of_vehicle"].str.strip() == type_of_vehicle
    vehicle_condition = data_of_interest["Vehicle_condition"] == condition
    weather = data_of_interest["Weatherconditions"].str.strip() == weather
    traffic = data_of_interest["Road_traffic_density"].str.strip() == traffic_condition

    specific_data = data_of_interest.loc[(vehicle & weather) & (traffic & vehicle_condition)]

    average_speed = average_speed_by_distance_and_time(specific_data['distance_km'].sum(), specific_data['Time_taken(min)'].sum())

    return total_distance / average_speed