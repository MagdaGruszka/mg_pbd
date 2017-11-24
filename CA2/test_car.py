import unittest

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()
# new car - mileage = 0; after moving the car by 15 miles test will show +15
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(25)
        self.assertEqual(25, self.car.getMileage())
        
# new car - after setting up the brand the brand will show up
    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

# new car - after setting up the new colour it will show the new colour
    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        
        
        
class TestPetrolCar(unittest.TestCase):

    def setUp(self):                
        self.car = PetrolCar()
        
# test for checking the cylinders no. after setting different value than before
    def test_PetrolCar_getNumberCylinders(self):
        self.assertEqual(1, self.car.getNumberCylinders())
        self.car.setNumberCylinders(2)
        self.assertEqual(2, self.car.getNumberCylinders())


class TestElectricCar(unittest.TestCase):

    def setUp(self):                
        self.car = ElectricCar()
        
# test for checking the fuel cells no.after setting different value than before 
    def test_ElectricCar_NumberFuelCells(self):
        self.assertEqual(2, self.car.getNumberFuelCells())
        self.car.setNumberFuelCells(4)
        self.assertEqual(4, self.car.getNumberFuelCells())


class TestDieselCar(unittest.TestCase):

    def setUp(self):                
        self.car = DieselCar()
        
# test for checking the cylinders no. after setting different value than before
    def test_DieselCar_NumberCylinders(self):
        self.assertEqual(4, self.car.getNumberCylinders())
        self.car.setNumberCylinders(6)
        self.assertEqual(6, self.car.getNumberCylinders())

class TestHybridCar(unittest.TestCase):

    def setUp(self):                
        self.car = HybridCar()
        
# test for checking the fuel cells no.after setting different value than before 
    def test_HybridCar_NumberFuelCells(self):
        self.assertEqual(4, self.car.getNumberFuelCells())
        self.car.setNumberFuelCells(8)
        self.assertEqual(8, self.car.getNumberFuelCells())       

# test for checking the cylinders no. after setting different value than before        
    def test_HybridCar_NumberCylinders(self):
        self.assertEqual(4, self.car.getNumberCylinders())
        self.car.setNumberCylinders(6)
        self.assertEqual(6, self.car.getNumberCylinders())
       

if __name__ == '__main__':                                  
    unittest.main()                                           

