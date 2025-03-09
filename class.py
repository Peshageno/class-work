class Animal():
    name = ""
    color = ""
    owner = ""

#a function within the class is called a method(its in the oop)
# the statement you write in a method are referred to as behaviours
    def sound(self):
        print("I bark")

dog = Animal()
dog.sound()



class Fruit:
    def __init__(pesh, name, color, size, taste, price):
        pesh.name = name
        pesh.color = color
        pesh.size = size
        pesh.taste = taste
        pesh.price = price

mango = Fruit("Mango","Yellow","Small","Yummy",2000)
apple = Fruit("Apple","Red","Meduim","Sweet",1000)
# Always remember self is not the key word we use any name as a key word


class Animal:
    def __init__(self, name, breed, color, size):
        self.name = name
        self.breed = breed
        self.color = color 
        self.size = size

#the first method
    def display_details(self):
        print(f"animalname: {self.name} animalbreed:{self.breed} animalcolor:{self.color} animalsize:{self.size}")
#dog class has inheritance from Animal class in line 29 and line 39
class Dog(Animal):
    def sound(self):
        print("dog woofs!")

dog = Dog("Max", "German sherperd", "Beige","Big",) 
dog.display_details() 
      
        
