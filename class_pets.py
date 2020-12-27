# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:40:33 2020

@author: Samuel Adebayo
"""

class Pet:
    def __init__(self, name, age, hunger, playful):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.playful = playful
    
    #getters
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getHunger(self):
        return self.hunger
    
    def getPlayful(self):
        return self.playful
    
    #setters
    
    def setName(self, name):
        self.name = name
    
    def setAge(self, Age):
        self.age = Age
    
    def setHunger(self, hunger):
        self.hunger = hunger
    
    def setplayful(self, playful):
        self.playful = playful

    def __str__(self):
        return (self.name + " is " + str(self.age) + "years old")
    

Pet1 = Pet("Skippy", 3, False, True)
print(Pet1.getName(), Pet1.getHunger(), Pet1.getAge())

print(Pet1.getPlayful())

Pet1.setName("Jacky")
print(Pet1.getName())

class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, favoriteToy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favoriteToy = favoriteToy
    
    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " +self.favoriteToy)
        else: 
            return("Dog doesn't want to play")
        
class Cat(Pet):
    def __init__(self, name, age, hunger, playful, place):
        Pet.__init__(self, name, age, hunger, playful)
        self.FavoritePlacetoSit = place
    
    def wantsToSit(self):
        if self.playful == False:
            print("The cat wants to sit in", self.FavoritePlacetoSit)
        else:
            print("The car wants to play")
        
    def __str__(self):
        return (self.name + " likes to sit in " + self.FavoritePlacetoSit)

class Human:
    def __init__(self, name, Pets):
        self.name = name 
        self.Pets = Pets
    def hasPets(self):
        if len(self.Pets) != 0:
            return "Yes"
        else:
            return "no"
        
huskyDog = Dog("Snowball", 5, False, True, "Husky", "Stick")

Play = huskyDog.wantsToPlay()
print(Play)
huskyDog.playful=False
Play = huskyDog.wantsToPlay()
print(Play)

typicalCat = Cat("Fluffy", 3, False, False, "the sun ray")
typicalCat.wantsToSit()
print(typicalCat)
print(Dog)

yourAverageHuman = Human("Alice", [huskyDog, typicalCat])

hasPet = yourAverageHuman.hasPets()
print(hasPet)
print(yourAverageHuman.Pets[0].name)