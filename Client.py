class Client:
    
    book_dates = dict([])


    def book_car(self, rentals):
        total_price = 0.0
        vehicles = []

        discount = False

        for rental in rentals:
            

            if not rental.vehicle.check_availability(rental.rent_from,rental.rent_to):
                return []

            rental.vehicle.book_dates.append((rental.rent_from,rental.rent_to))

            self.book_dates[rental.vehicle.registration_number] = (rental.rent_from, rental.rent_to)

            hours_booked = abs(rental.rent_from - rental.rent_to).total_seconds() / 3600.0


            if hours_booked < 24:
                price = rental.vehicle.hour_cost
            elif hours_booked >= 168:
                price = rental.vehicle.weekly_cost
            else:
                price = rental.vehicle.daily_cost

            if len(rentals) > 3:
                price = float(price) * 0.7
                discount = True

            
            total_price += float(price)

            vehicles.append(rental.vehicle)

        print("Booking Ok!\n")

        if discount:
            print("30% Discount is applied.\n")
        
        print("Total price: \n", round(total_price,2))
        
        
        return vehicles

    def cancel_booking(self,vehicle):

        for i, vehicle_date_pair in enumerate(vehicle.book_dates):
            flag = False
            for key in self.book_dates:
                if vehicle_date_pair == self.book_dates[key]:
                    print("Deleted")
                    del vehicle.book_dates[i]
                    self.book_dates.pop(key)
                    flag = True
                    break
            if flag:
                break
        
        return vehicle