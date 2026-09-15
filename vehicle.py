class vehicle:
    def __init__(self,brand, rent_per_day):
        self.brand = brand

        self.rent_per_day = rent_per_day


        

        def calculate_rent(self,days):

            

            return self.rent_per_day*days



class car(vehicle):
    def calculate_rent(self,days):

        return (self.rent_per_day*days)+ 500

class bike(vehicle):

    def calculate_rent(self,days):

        return (self.rent_per_day*days)+200
        
car = car("Toyota",2500)
bike = bike("HONDA",1000)

vehicles = [car,bike]

for vehicle in vehicles:

    print(vehicle.brand,vehicle.calculate_rent(3))
