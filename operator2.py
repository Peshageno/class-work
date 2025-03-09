#comparison operators
#these compare two values and return a boolean value

comp1 = 10
comp2 = 20
print(comp1 < comp2)# less than
print(comp1 > comp2)# greater than
print(comp1 >= comp2)# greater than or equal to
print(comp1 <= comp2)# less than or equal to
print(comp1 != comp2)#not equal to(exclamation mark in programming means not)
print(comp1 == comp2)#equal to

#logical operators
#the examples are and, or, not(for and it is for (&) or it is fo (|))
log1 = 5
log2 = 6
#and operator prints true if both conditions are true
print((log1> log2)) and ((log2< log1))
#
print(not (log2 < log1))
#or operator will return true when one is true
print((log1 > log2)) or ((log2 < log1))

print(True and True)
print(True and False)
print(True or False)
print(not True)
print(True or True)

# membership operators are used to

numbers = [20,30,40,50]
print(20 in numbers)
print (20 not in numbers)

name ="patience"
print("P" not in name)

#identity operators
#we use is and is not to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
#it is used to compare the objects not if they are equal, but if they are actually the same object, with the same memory location
print(20 is not numbers)
print(20 is 20)




