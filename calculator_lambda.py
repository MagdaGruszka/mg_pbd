class Calculator(object):
    
    def add():
        return list(map(lambda x,y:x+y, a,b))

    def subtract():
        return list(map(lambda x,y:x-y, b,a))

    def divide():
        return list(map(lambda x,y:x/y, b,a ))

    def multiply():
        return list(map(lambda x,y:x*y, a,b))

a = [1,2,3,4]
b = [17,12,11,10]

print add()
print subtract()
print divide()
print multiply()