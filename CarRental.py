from Vehicle import *
from Client import *
from Rental import *
import json
import datetime

user_list =[]
initial_vehicles={}

def initialize_data():
    
    print('initializing data...')

    with open("carsInput.json") as json_input:
        data = json.load(json_input)
        for vehicle in data["cars"]:
            initial_vehicles[vehicle["registration_number"]] = Vehicle(vehicle["name"],vehicle["model"],vehicle["fuel_consumption"],vehicle["registration_number"],vehicle["daily_cost"],vehicle["weekly_cost"],vehicle["hour_cost"])


    
    global temp_customer
    temp_customer = Client()
    user_list.append(temp_customer)
    
    for  vehicle in initial_vehicles.values():
        print(vehicle)

def book(*rentals):

    

    vehicles = temp_customer.book_car(rentals)


    for vehicle in vehicles:
        initial_vehicles[vehicle.registration_number]= vehicle
    
    
if __name__ == "__main__":
    initialize_data()
    
    book(Rental(initial_vehicles["CA-7618-KP"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,12,16)))

    initial_vehicles["CA-7618-KP"] = temp_customer.cancel_booking(initial_vehicles["CA-7618-KP"])
    
    book(Rental(initial_vehicles["CA-7618-KP"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,19,19)))
    book(Rental(initial_vehicles["CA-7618-KP"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,12,21)))

    book(Rental(initial_vehicles["K-0513-BC"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,13,19)), Rental(initial_vehicles["CA-2255-PP"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,12,19)), Rental(initial_vehicles["X-1122-KK"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,12,19)), Rental(initial_vehicles["X-3512-KB"], datetime.datetime(2012,6,12,15),datetime.datetime(2012,6,12,19)))


