# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 06:26:11 2020

@author: Samuel Adebayo
"""
from termcolor import colored, cprint 
import random



class Vehicle():
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance = False, TripsSinceMaintenance =0):
        self.Make = Make
        self.Model = Model
        self.Year =Year
        self.Weight = Weight
        self.NeedsMaintenance= NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance



    #setters
    def Maker(self, Make):
        self.Make = Make        

    def sModel(self, Model):
        self.Model = Model      

    def setYear(self, Year):
        self.Year = Year      

    def setWeight(self, Weight):
        self.Weight = Weight      
    
#======================================
    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight
    
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

#=============================================  
#Inheritance classes from vehicle called cars

class Cars (Vehicle):
    def __init__(self, Make, Model, Year, Weight, isDriving = True):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isDriving = isDriving
    
    def Drive(self):
        self.isDriving = True
    
    def Stop(self):
        if self.isDriving == False:
            self.TripsSinceMaintenace +=1
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            
    def __str__(self):
        print("===============================================")
        print("Needs Maintenance? ", self.NeedsMaintenance)
        return "This " + self.Model + " car was made by " + self.Make +  " in the year " + str(self.Year) + " with weight " + str(self.Weight) + "Kg and it has done " + str(self.TripsSinceMaintenance) + " trips"
        
#=========================== Driving the car code
def drivecar(Car):
    dt = random.randint(1, 500)
    for driver in range (dt):
        Car.Drive()
        Car.Stop()

#==================================================
class Plane(Vehicle):
    def __init__(self, Make, Model, Year, Weight, isFlying = False):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isFlying = isFlying
    
    def flying(self):
        if self.NeedsMaintenance == True:
            return False
        self.isFlying = True
        return True
    
    def landing(self):
        if self.isFlying:
            self.TripsSinceMaintenance += 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
        self.isFlying = False

        
# =====================================
def randomly_fly_plane(Plane, fly_times = None):
    fly_times = random.randint(1, 500) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = Plane.flying()
        if is_flying:
            Plane.landing()
        else:
            cprint("plane " + Plane.Model + " can't fly until it's repair", 'red', attrs=['bold'])
            cprint("Under Repair... " + Plane.Model, 'green', attrs=['bold'])
            Plane.Repair()


#==================== Testing
plane1 = Plane("Boeing Commercial Airplanes", "Boeing 737 Max", 2016, 80286 )

randomly_fly_plane(plane1, 332)

Car1 = Cars("Tesla", "Tesla Model 3", 2017, 1726)
Car2 = Cars("Mercedes-Benz", "Mercedes-AMG A35 Sedan", 2020, 2055)
Car3 = Cars("Bayerische Motoren Werke AG", "BMW 3 Series", 2020, 2020)

print(Car1)
print (Car2)
print (Car3)



drivecar(Car1)
