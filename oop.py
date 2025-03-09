#object oriented programming
'''class, object, properties(attributes ,charactertics, features),
methods constructors, 
principles of oop(abstraction, encapulsation,inheritance, polymorphism)
overloading , overriding'''
# a class  is a blueprint or orginal format of something
# name,size,price, color ,type ,location
# "is a" is a phrase we use to identify  a class of a particular a object.
# an object should fulfill all the properties of a class

students =['Pesh' 'Travis' 'Erica' 'Login']
student1 ={"Name": "Pesh", "Gender": "Female", "School": "Refactory"}

class Latop():
    pass

class Food():
    name = ""
    taste = ""
    calories = 0
    price = 0
    value = ""
# 
#creating objects out of the class Food
# all objects have a level of abstraction
matooke = Food()
matooke.name = matooke
matooke.taste = "sweet"
matooke.calories = 0
matooke.price = 2500
matooke.value = "one"

rice = Food()
rice.name ="rice"
rice.calories = 0
print(rice.name)
