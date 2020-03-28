# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
        
    def age(self):
        from datetime import date
        year = date.today().year
        return year - self.year
    
my_car = Car(2018, "Lamborghini", "Aventador")
print("The age of my car is:", my_car.age())
