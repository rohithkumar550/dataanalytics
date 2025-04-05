# Single level inheritance
class Writer:
    def write(self):
        print("Writer writes a story")

class Novelist(Writer):
    def publish(self):
        print("Novel is published")

# Create an object of Novelist
novelist = Novelist()
novelist.write()   # Inherited from Writer
novelist.publish() # Defined in Novelist

# Multiple inheritance
class Chef:
    def cook(self):
        print("Chef cooks food")

class Designer:
    def draw(self):
        print("Designer draws a layout")

class MultiTalented(Chef, Designer):
    pass

# Create an object of MultiTalented
person = MultiTalented()
person.cook()  # Inherited from Chef
person.draw()  # Inherited from Designer

# Mulilevel inheritance
class Machine:
    def start(self):
        print("Machine starts")

class Engine(Machine):
    def fuel(self):
        print("Engine uses fuel")

class Car(Engine):
    def drive(self):
        print("Car drives smoothly")

# Create an object of Car
car = Car()
car.start()  # Inherited from Machine
car.fuel()   # Inherited from Engine
car.drive()  # Defined in Car

# Hierarchical Inheritance
class Instrument:
    def play(self):
        print("Instrument is being played")

class Guitar(Instrument):
    def strum(self):
        print("Guitar strums")

class Piano(Instrument):
    def press_keys(self):
        print("Piano keys are pressed")

# Create objects of Guitar and Piano
guitar = Guitar()
piano = Piano()

guitar.play()      # Inherited from Instrument
guitar.strum()

piano.play()       # Inherited from Instrument
piano.press_keys()

# Hybrid Inheritance
class Appliance:
    def power(self):
        print("Appliance gets electricity")

class Washer(Appliance):
    def wash(self):
        print("Washer cleans clothes")

class Dryer(Appliance):
    def dry(self):
        print("Dryer dries clothes")

class ComboWasherDryer(Washer, Dryer):
    def combo_mode(self):
        print("Combo Washer-Dryer running both modes")

# Create an object of ComboWasherDryer
combo = ComboWasherDryer()
combo.power()       # Inherited from Appliance
combo.wash()        # Inherited from Washer
combo.dry()         # Inherited from Dryer
combo.combo_mode()  # Defined in ComboWasherDryer
