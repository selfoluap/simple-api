from fastapi import FastAPI
import random
import time

app = FastAPI()

ship_information = {
    1: {
        "ship_id": 1,
        "ship_name": "Millennium Falcon",
        "ship_type": "YT-1300 light freighter",
        "ship_class": "Light freighter",
        "manufacturer": "Corellian Engineering Corporation",
        "length": "34.37",
    },
    2: {
        "ship_id": 2,
        "ship_name": "Slave 1",
        "ship_type": "Firespray-31-class patrol and attack",
        "ship_class": "Patrol craft",
        "manufacturer": "Kuat Systems Engineering",
        "length": "21.5",
    },
    3: {
        "ship_id": 3,
        "ship_name": "Imperial I-class Star Destroyer",
        "ship_type": "Star Destroyer",
        "ship_class": "Star Destroyer",
        "manufacturer": "Kuat Drive Yards",
        "length": "1600",
    },
}

global ship_status_data 

ship_status_data = {
    1: {
        "COG": 180,
        "SOG": 25,
        "HDG": 180,
        "STW": 25,
        "Lat": 34.0522,
        "Long": -118.2437,
        "Rudder Angle": 0,
        "Wind speed": 15,
        "Wind direction": 90,
        "Torgue propshaft": 5000,
        "RPM propshaft": 200,
        "Power propshaft (kW)": 1500,
        "Fuel Consumption ME": 100,
        "Total aux power demand": 300,
    },
    2: {
        "COG": 90,
        "SOG": 20,
        "HDG": 90,
        "STW": 20,
        "Lat": 37.7749,
        "Long": -122.4194,
        "Rudder Angle": 5,
        "Wind speed": 10,
        "Wind direction": 180,
        "Torgue propshaft": 4000,
        "RPM propshaft": 180,
        "Power propshaft (kW)": 1200,
        "Fuel Consumption ME": 80,
        "Total aux power demand": 250,
    },
    3: {
        "COG": 270,
        "SOG": 30,
        "HDG": 270,
        "STW": 30,
        "Lat": 40.7128,
        "Long": -74.0060,
        "Rudder Angle": -5,
        "Wind speed": 20,
        "Wind direction": 270,
        "Torgue propshaft": 6000,
        "RPM propshaft": 220,
        "Power propshaft (kW)": 1800,
        "Fuel Consumption ME": 120,
        "Total aux power demand": 350,
    },
}

def update_ship_status():
    for ship_id, ship_data in ship_status_data.items():
        for key, value in ship_data.items():
            if isinstance(value, int):
                ship_data[key] += random.randint(-5, 5)
            elif isinstance(value, float):
                ship_data[key] += random.uniform(-0.05, 0.05)

@app.get("/ship_information/{ship_id}")
def get_ship_information(ship_id: int):
    return {
        "ship_id": ship_id,
        "ship_name": ship_information[ship_id]["ship_name"],
        "ship_type": ship_information[ship_id]["ship_type"],
        "ship_class": ship_information[ship_id]["ship_class"],
        "manufacturer": ship_information[ship_id]["manufacturer"],
        "length": ship_information[ship_id]["length"],
    }

@app.get("/ship_status/{ship_id}")
def get_ship_status(ship_id: int):
    update_ship_status()
    return {
        "datetime": time.time(),
        **ship_status_data[ship_id] 
    }