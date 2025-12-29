# car_class.py

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand      # Instance attribute
        self.model = model      # Instance attribute

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Call methods
car1.drive()
car2.drive()

# Access instance attributes
print("Car 1 brand:", car1.brand)
print("Car 2 brand:", car2.brand)

# Access class attribute
print("Number of wheels:", Car.wheels)
