import pandas as pd

def get_data():
    data = pd.read_csv('../data/raw/Uber.ETA/train.csv').dropna().drop_duplicates()
    return data[["Restaurant_longitude", "Restaurant_latitude","Delivery_location_longitude", "Delivery_location_latitude","Road_traffic_density", "Vehicle_condition","Type_of_vehicle","Weatherconditions", "Time_taken(min)"]]


