from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

# he user interface

class Dealership(object):
        
    print '#############################'
    print 'WELCOME TO AUNGIER CAR RENTAL'
    print '#############################'
    print 'You can rent petrol, diesel, electric, or hybrid cars'


    def __init__(self):
        self.PetrolCar = []
        self.ElectricCar = []
        self.DieselCar = []
        self.HybridCar = []

    def create_current_stock(self): # setting start values for each type of car   
        for i in range(20):
           self.PetrolCar.append(PetrolCar())
        for i in range(4):
           self.ElectricCar.append(ElectricCar())
        for i in range(12):
           self.DieselCar.append(DieselCar())
        for i in range(4):
           self.HybridCar.append(HybridCar())

    def stock_count(self):
        print 'Please check our current stock'
        print  str(len(self.PetrolCar)) + ' Petrol cars'
        print  str(len(self.ElectricCars)) + ' Elactric cars'
        print  str(len(self.DieselCars)) + ' Diesel cars'
        print  str(len(self.HybridCars)) + ' Hybrid cars'

    def process_rental(self):
        print 'Please press \'r\'to rent a car or any other key to return a car:  '
        answer = raw_input()
    
        if answer == 'r' or answer =='R':
            
            # define car1-Petrol
            car1 = PetrolCar()
            car1.setCartype('Petrol')
            car1.setMake('Honda Civic')
            car1.move(30)
            car1.setColour('Red')
            print 'Car Type: ' + car1.getCartype()
            print 'Make: ' + car1.getMake()
            print 'Number of cylinders: ' + str(car1.getNumberCylinders())
            print 'Colour: ' + car1.getColour()
            print '#####################'
            
            # define car2-Electric
            car2 = ElectricCar()
            car2.setCartype('Electric')
            car2.setMake('Nissan Leaf')
            car2.setNumberOfFuelCells(2)
            car2.move(20)
            car2.setColour('Blue')
            print 'Car Type: ' + car2.getCartype()
            print 'Make: ' + car2.getMake()
            print 'Number of fuel cells: ' + str(car2.getNumberFuelCells())
            print 'Colour: ' + car2.getColour()
            print '#####################'
                   
            # define car3-Diesel
            car3 = DieselCar()
            car3.setCartype('Diesel')
            car3.setMake('Hyundai Santa Fe')
            car3.move(30)
            car3.setColour('Silver')
            print 'Car Type: ' + car3.getCartype()
            print 'Make: ' + car3.getMake()
            print 'Number of cylinders: ' + str(car3.getNumberCylinders())
            print 'Colour: ' + car3.getColour()
            print '#####################'
            
            # define car4-Hybrid
            car4 = HybridCar()
            car4.setCartype('Hybrid')
            car4.setMake('Toyota Prius')
            car4.setNumberFuelCells(2)
            car4.setNumberCylinders(4)
            car4.move(50)
            car4.setColour('White')
            print 'Car Type: ' + car4.getCartype()
            print 'Make: ' + car4.getMake()
            print 'Number of cylinders: ' + str(car4.NumberCylinders())
            print 'Number of fuel cells: ' + str(car4.getNumberFuelCells())
            print 'Colour: ' + car4.getColour()
            print '#####################'

            #rent or return choice, for both with otional petrol/electric/diesel/hybrid
            choice = raw_input ('Press \'p\' for petrol, \'e\' for electric, \'d\' for diesel or \'h\' for hybrid:  ')
            amount = int(raw_input('How many would you like?: '))
            
            if choice == 'P'or choice == 'p':
                if len(self.PetrolCar) < amount:
                    print 'Not enough petrol cars in stock'
                    return
                else:
                    print 'Thank you, you have chosen to rent ', amount, 'petrol car(s)'
                self.rent(self.PetrolCar, amount)
                self.stock_count()
                
            elif choice == 'E'or choice == 'e':
                if len(self.ElectricCar) < amount:
                    print 'Not enough electric cars in stock'
                    return
                else:
                    print 'Thank you, you have chosen to rent ', amount, 'electric car(s)'
                self.rent(self.ElectricCar, amount)
                self.stock_count()
                
            elif choice == 'D'or choice == 'd':
                if len(self.DieselCar) < amount:
                    print 'Not enough diesel cars in stock'
                    return
                else:
                    print 'Thank you, you have chosen to rent ', amount, 'diesel car(s)'
                self.rent(self.DieselCar, amount)
                self.stock_count()
                
            elif choice == 'H'or choice == 'h':
                if len(self.HybridCar) < amount:
                    print 'Not enough hybrid cars in stock'
                    return
                else:
                    print 'Thank you, you have chosen to rent ', amount, 'hybrid car(s)'
                self.rent(self.HybridCar, amount)
                self.stock_count()
                
            else:
                print 'Please choose valid letter'
                return
    
        else:
            answer = raw_input('What type of car would you like to return? d/e/h/p: ')

            try:
                amount = int(raw_input('How many would you like to return?: '))
            except ValueError:
                print 'Please choose a number'
          
                if answer == 'P' or answer == 'p':
                    if len(self.PetrolCar) + amount > 20: 
                       print 'This numbr is incorrect, try again'
                       return

                    else:
                        print 'You have chosen ', amount, 'petrol car(s)'
                    self.rent(self.PetrolCar, amount)

                elif answer == 'E' or answer == 'e':
                    if len(self.ElectricCar) + amount > 4: 
                        print 'This numbr is incorrect, try again' 
                        return
                    else:
                        print 'You have chosen ', amount, 'electric car(s)'
                    self.rent(self.ElectricCar, amount)
                
                elif answer == 'D' or answer == 'd':
                    if len(self.DieselCar) + amount > 12: 
                        print 'This numbr is incorrect, try again' 
                        return
                    else:
                        print 'You have chosen ', amount, 'diesel car(s)'
                    self.rent(self.DieselCar, amount)

                elif answer == 'H' or answer == 'h':
                    if len(self.HybridCar) + amount > 4: 
                        print 'This numbr is incorrect, try again' 
                        return
                    else:
                        print 'You have chosen ', amount, 'hybrid car(s)'
                    self.rent(self.HybridCar, amount)                      
                
                else: 
                    print 'Please choose the type available in stock'
                    return       

# RENT FUNCT
    
	def rent(self, PetrolCar, amount):
		total = 0
		while total < amount:
			PetrolCar.pop()  # to subtract from current stock
			total = total + 1
            
	def rent(self, ElectricCar, amount):
		total = 0
		while total < amount:
			ElectricCar.pop()  # to subtract from current stock
			total = total + 1	
	
	def rent(self, DieselCar, amount):
		total = 0
		while total < amount:
			DieselCar.pop()  # to subtract from current stock
			total = total + 1

    def rent(self, HybridCar, amount):
		total = 0
		while total < amount:
			HybridCar.pop() # to subtract from current stock
			total = total + 1
            
# RETURN FUNCT

    def returncar(self, PetrolCar, amount):
        total = 0
        while total < amount:
            PetrolCar.append(PetrolCar()) #to add to current stock
	    total = total + 1
            		
	def returncar(self, ElectricCar, amount):
		total = 0 
		while total < amount:
			ElectricCar.append(ElectricCar()) #to add to current stock
		total = total + 1
	
	def returncar(self, DieselCar, amount):
		total = 0
		while total < amount:
			DieselCar.append(DieselCar()) #to add to current stock
		total = total + 1
			
	def returncar(self, HybridCar, amount):
		total = 0
		while total < amount:
			HybridCar.append(HybridCar()) #to add to current stock
		total = total + 1      		
        
       
        
dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')

def end ():
	dealership = 'AUNGIER CAR RENTAL'
	print 'Thank you for choosing', dealership, '.'
	quit()

end()

