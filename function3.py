# static funtion have fixed values of a variables
def add():
    number= 5
    numbers = 15
    return number + numbers
print(add())

# add ,return and not changing(dynamic function expect values on the call of a function)
def add1(number,numbers):# a variable within the braces() is called a parameter
    return number+ numbers
#the values of the parameter is called arguments/actual parameters(20,50..)
print(add1(20, 50))#parameter list ,the number of argument in the brackets(2)
print(add1(40, 20))
print(add1(10,30))

