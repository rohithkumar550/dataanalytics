class Vehicle:
    def display(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def display(self):
        super().display()
        print("Inside Car class")
