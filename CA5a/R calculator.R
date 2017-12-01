add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  return(x / y)
}

exponent <- function (x,y){
  return(x ** y)
}
  
sqrt <- function (x){
  return (x**0.5) 
}

square <- function(x){
  return (x * x)
}
   

cube <- function(x){
  return (x*x*x)
}
  
sin <- function(x) {
  return (math.sin(x))
}


factorial = 1

factorial <- function (x){
  return (for(i in 1:num1)
    factorial = factorial * i)
  }

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.square root")
print("7.Square")
print("8.Cube")
print("9.sin")
print ("10.factorial")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

num1 = as.integer(readline(prompt="Enter first number: "))
num2 = as.integer(readline(prompt="Enter second number: "))

operator <- switch(choice,"+","-","*","/", "**", "**0.5", "*" , "**", "sin", "!")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2),
                 exponent(num1, num2), sqrt(num1), square(num1), Cube(num1), sin(num1), factorial(num1))

print(paste(num1, operator, num2, "=", result))
