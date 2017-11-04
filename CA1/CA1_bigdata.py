
class Calculator(object): #calculator functions in python
 
    def add(self, x, y):
        number_type = (int, float, complex)
        if isinstance(x,number_type) and isinstance(y,number_type):
            return x + y
        else:
            raise ValueError
            
    def subtract(self, x, y):
        return x - y 
        
    def multiply(self, x, y):
        return x*y
        
    def divide(self, x,y):
        if y == 0:
            return 'NaN'
        else:
            return x/float(y)
            
    def exponent(self, x,y):
        return x ** y
        
    def sqrt(self,x):
        if x <= 0:
            return 'NaN'
        else:
            return x**0.5
   
    def square(self, x):
        return x * x 
        
    def cube(self, x):
        return x*x*x 

    def sin(self,x):
        try:
            return math.sin(x)
        except:
            raise ValueError



    
    
    

