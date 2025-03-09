# how to declare under encapsulation
class Animal:
    # This is a constructor always defined with an underscore
    # A constructor is used to initialize/give a value of an object of  class
    # the first parameter will always be used to identify the properties e.g self)(animalname is a value of the parameter of the class)
    def __init__(self,name,sound, size, color):
       self.animalname = name
       self.animalsize = size
       self.animalsound = sound
       self.animalcolor = color

cat = Animal("cat","small", "meow" "white")
stallion = Animal("buddy" "large" "nickers" "beige")
    
