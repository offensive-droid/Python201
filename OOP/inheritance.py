class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model} has been started.")
        else:
            print(f"The {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has been stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

    def honk(self):
        print(f"The {self.make} {self.model} says 'Beep beep!'")

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
print(car1.__dict__)
