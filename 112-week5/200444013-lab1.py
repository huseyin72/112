# hüseyin özdemir 200444013
from tokenize import Double
from numpy import double

#question1 calculator 
class Calculator():
     def __init__(self):
          pass
          #self.num1 = double(num1)
          #self.num2 = double(num2)
    
    
     def add(self,num1,num2):
          
          return print (double(num1 + num2))

     def substract(self,num1,num2):
          return print (double(num2 - num1))

     def multipy(self,num1,num2):
          return print( double(num1*num2))
          

     def divide(self,num1,num2):
          try:
               return print (double(num1/num2))

          except ZeroDivisionError:
               return print("You can’t divide by zero")

calculator1 = Calculator()
calculator1.substract(5,3)
calculator1.add(5,8)
calculator1.multipy(3,8)
calculator1.divide(4,0)


#question2 Fotball class
class Footbal():
     def __init__(self,stadium_name = "",team_1 ="",team_2="",score={"team1":0,"team2":0}):
          self.stadium_name = stadium_name
          self.team_1 = team_1
          self.team_2 = team_2
          self.score = dict(score) 
          pass
     def set_stadium(self,stadiumName):
          self.stadium_name = stadiumName

     def set_team_1(self,team_1_name):
          self.team_1 = team_1_name
          
     def set_team_2(self,team_2_name):
          self.team_2 = team_2_name
          
     def set_score(self,score_dictionary):
          self.score = dict({})
          teams = ["team1","team2"]
          
          
          for i in range(0,2):
               
               self.score[teams[i]]=score_dictionary[i]
          
          
     def get_stadium(self):
          return print(self.stadium_name)
     def get_team1(self):
          return print(self.team_1)
     def get_team2(self):
          return print(self.team_2)
     def get_score(self):
          return print((self.score))
game1 = Footbal()
game1.set_stadium("şükrü saracaoglu")
game1.set_team_1("fenerbahce")

game1.get_stadium()
game1.set_score([8,2])
game1.get_team1()
game1.get_score()
