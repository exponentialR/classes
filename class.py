# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:32:38 2020

@author: Research
"""
# class ClassName:
#     def __init__(self): #define an initializer (__init__)
#         self.Attribute = 0
        
#     def AnotherFunction(self):
#         Action(s)
        
class Team :
    def __init__(self, Name="Name", Origin="Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin
    
    def DefineTeamName(self, Name):
        self.TeamName = Name
    
    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin
        
Team1 = Team("Tigers", "Chicago")
Team2 = Team("Hawks", "New York")
Team3 = Team()

print(Team1.TeamName)
Team1.DefineTeamName("Dolphins")
print(Team1.TeamName)
print(Team1.TeamOrigin)
Team1.DefineTeamOrigin("Chicago")
#print(Team1.TeamOrigin)
print(Team2.TeamName)
print(Team2.TeamOrigin)
print(Team3.TeamName)
print(Team3.TeamOrigin)