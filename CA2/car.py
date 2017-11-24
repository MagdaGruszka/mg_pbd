# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__make = ''
        self.__cartype = ''
        self.engineSize = ''
        self.__mileage = 0
        self.__colour = ''

    def setMake(self, make):
        self.__make = make
        
    def getMake(self):
        return self.__make
    
    
    def setCartype(self, cartype):
        self.__cartype = cartype
        
    def getCartype(self):
        return self.__cartype

    
    
    def setMileage(self, mileage):
        self.__mileage = mileage
        
    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
    
    def getMileage(self):
        return self.__mileage   
    
    
    def getColour(self):
        return self.__colour
    
    def paint(self, colour):
        self.__colour = colour
        return self.__colour
    
    def setColour(self, colour):
        self.__colour = colour
        

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value   
        
        
class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 2

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 4

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 4
        self.__numberCylinders = 4

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value
        
    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value