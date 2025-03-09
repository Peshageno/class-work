#functions are self-contained blocks of code
#return exposes the value to be accessed out of the function
def add():
  var1 = 26
  var2 = 45
  return var1 + var2

print(add())
my_Num = add()
print(my_Num)

def sub():
  var1 = 26
  var2 = 45
  return var2 - var1

def both():
  return sub() + add()

print(both())

def add1():
  sum1 = int(input("please enter your number"))
  sum2 = int(input("please enter your value"))
  return sum1 + sum2

def sub1():
  var3 = int(input("please enter your number"))
  var4 = int(input("please enter your value"))
  return var3 -var4

def both1():
  return sub1() + add1()

print(both1())