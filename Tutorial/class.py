# Atharv Kolhar
# Python Bytes

"""
Class
"""


class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def add_miles(self, miles):
        self.miles = miles

    def next_service(self, date):
        self.service_date = date


car_1 = Car(brand='Tesla', model='Model 3', fuel='Electric')

car_2 = Car('Honda', 'Accord', 'Gasoline')

car_3 = Car(fuel='Hybrid', model='CRV', brand='Honda')

car_1.add_miles(100)
car_2.add_miles(500)
car_3.add_miles(1000)

print(car_3.miles)

car_3.next_service('03032022')

print(car_3.service_date)

