from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Starting car...")

    def stop(self):
        print("Stop the car...")

class Motorcycle(Vehicle):
    def drive(self):
        print("Starting motorcycle...")

    def stop(self):
        print("Stop the motorcycle...")

class Bus(Vehicle):
    def drive(self):
        print("Starting bus...")

    def stop(self):
        print("Stop the bus...")

# membuat objek dari subclass Car, Motorcycle, dan Bus
car = Car()
motorcycle = Motorcycle()
bus = Bus()

# memanggil method drive dan method stop pada objek tersebut
car.drive()
car.stop()

motorcycle.drive()
motorcycle.stop()

bus.drive()
bus.stop()

    