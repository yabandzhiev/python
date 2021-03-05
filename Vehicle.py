import datetime

class Vehicle():




    def __init__(self, make, model, fuel_consumption, registration_number,daily_cost, weekly_cost, hour_cost):
        self.cost = Cost(daily_cost, weekly_cost, hour_cost)
        self.make = make
        self.model=model
        self.fuel_consumption=fuel_consumption
        self.registration_number=registration_number
        self.daily_cost=daily_cost
        self.weekly_cost=weekly_cost
        self.hour_cost=hour_cost
        self.book_dates=[]
    
    def check_availability(self, requested_rent_from, requested_rent_to):



        for date in self.book_dates:
            if date[0] <= requested_rent_from <= date[1] or date[0] <= requested_rent_to <= date[1]:
                print("The car with registration number: " + self.registration_number + " is not available.")
                return False
            else:
                return True
        
        return True
    
    def __str__(self):
        info = "Registration Number: " + self.registration_number + "\nMake: " + self.make +"\nModel: " + self.model + "\nFuel Consumption: " + str(self.fuel_consumption) + "\n" + self.cost.__str__()

        return info

class Cost:
    def __init__(self, daily_cost, weekly_cost, hour_cost):
        self.daily_cost=daily_cost
        self.weekly_cost=weekly_cost
        self.hour_cost=hour_cost
    
    def __str__(self):
        info = "Daily Cost: " + str(self.daily_cost) + "\nWeekly Cost: " + str(self.weekly_cost) + "\nHour Cost: " + str(self.hour_cost) +"\n"

        return info

class Car(Vehicle):
    def __init__(self,make,model,fuel_consumption,registration_number,daily_cost,weekly_cost,hour_cost):
        super().__init__(make,model,fuel_consumption,registration_number,daily_cost,weekly_cost,hour_cost)
    
    def __str__(self):
        info = super().__str__()
        return info