# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 23:49:11 2023

@author: hansd
"""

import numpy as np
import pylab as pl
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
from playsound import playsound
import random

class Game:
    def __init__(self,players):
        self.__free_money = 0
        self.__no_bank = 0
        self.__no_player = 2
        self.__name_array = ['Go','Old Kent Road','Community Chest','Income Tax','Kings Cross Station','The Angel Islington','Chance','Euston Road','Pentonville Road','Just Visitng','Pall Mall','Electric Company','Whitechapel','Northumberland Avenue','Marylebone Station','Bow Street','Community Chest','Marlborough Street','Vine Street','Free Parking','Strand','Chance','Fleet Street','Trafalgar Square','Fenchurch Street','Leicester Square','Coventry Street','Water Works','Piccadilly','Go to Jail','Regent Street','Oxford Street','Community Chest','Bond Street','Liverpool Street Station','Chance','Park Lane','Super Tax','Mayfair']
        
        self.__p1_turns = 0
        self.__p2_turns = 0
        
        self.__p1_jail = False
        self.__p2_jail = False
        self.__p1_pos = 0
        self.__p2_pos = 0
        self.__p1_money = 1500
        self.__p2_money = 1500
        self.__p1_bank = False
        self.__p2_bank = False
        self.__p1_jailtime = 0
        se;f.__p2_jailtime = 0
        if players == 3:
            self.__p3_turns = 0
            
            self.__p3_jail = False
            self.__p3_pos = 0
            self.__p3_money = 1500
            self.__p3_bank = False
            self.__p3_jailtime = 0
            self.__no_player = 3
            if players == 4:
                self.__p4_turns = 0               
                
                self.__p4_jail = False
                self.__p4_pos = 0
                self.__p4_money = 1500
                self.__p4_bank = False
                self.__p4_jailtime = 0
                self.__no_player = 4

    def start(self):
        Game.turn(self,1)
        
    def turn(self,player):
        if player == 1 and self.__p1_bank == False:
            print("It is player 1's turn")
            print("Player 1 has %.10f"%self.__p1_money)
            if self.__p1_jail == True:
                Game.outofjail(self,1)
            else:
                Game.move(self,1)
        if player == 2 and self.__p2_bank == False:
            print("It is player 2's turn")
            print("Player 2 has %.10f"%self.__p2_money)
            if self.__p2_jail == True:
                Game.outofjail(self,2)
            else:
                Game.move(self,2)
        if player == 3 and self.__p3_bank == False:
            print("It is player 3's turn")
            print("Player 3 has %.10f"%self.__p3_money)
            if self.__p3_jail == True:
                Game.outofjail(self,3)
            else:
                Game.move(self,3)
        if player == 4 and self.__p4_bank == False:
            print("It is player 4's turn")
            print("Player 4 has %.10f"%self.__p4_money)
            if self.__p4_jail == True:
                Game.outofjail(self,4)
            else:
                Game.move(self,4)
        
        if self.__p1_money < 0 and self.__p1_bank == False:
            self.__p1_bank = True
            print("Player 1 is bankrupt and out of the game")
        
        if self.__p2_money < 0 and self.__p2_bank == False:
            self.__p2_bank = True
            print("Player 2 is bankrupt and out of the game")
            
        if self.__p3_money < 0 and self.__p3_bank == False:
            self.__p3_bank = True
            print("Player 3 is bankrupt and out of the game")
            
        if self.__p4_money < 0 and self.__p4_bank == False:
            self.__p4_bank = True
            print("Player 4 is bankrupt and out of the game")
            
        Game.endturn(self,player)
    
    def endturn(self,player):
        if self.__no_bank == 1 and self.__no_player == 2:
            if self.__p1_bank == False:
                print("Player 1 has won the game!")
            if self.__p2_bank == False:
                print("Player 2 has won the game!")
        elif self.__no_bank == 2 and self.__no_player == 3:
            if self.__p1_bank == False:
                print("Player 1 has won the game!")
            if self.__p2_bank == False:
                print("Player 2 has won the game!")
            if self.__p3_bank == False:
                print("Player 3 has won the game")
        elif self.__no_bank == 3 and self.__no_player == 4:
            if self.__p1_bank == False:
                print("Player 1 has won the game!")
            if self.__p2_bank == False:
                print("Player 2 has won the game!")
            if self.__p3_bank == False:
                print("Player 3 has won the game")
            if self.__p4_bank == False:
                print("Player 4 has won the game!")
        else:
            if self.__no_player == 2:
                if player == 1:
                    Game.turn(self,2)
                if player == 2:
                    Game.turn(self,1)
            if self.__no_player == 3:
                if player == 1:
                    Game.turn(self,2)
                if player == 2:
                    Game.turn(self,3)
                if player == 3:
                    Game.turn(self,1)
            if self.__no_player == 4:
                if player == 1:
                    Game.turn(self,2)
                if player == 2:
                    Game.turn(self,3)
                if player == 3:
                    Game.turn(self,4)
                if player == 4:
                    Game.turn(self,1)
        

    def move(self,player,number=False):
        if number == False:
            roll = Game.roll(self)
        else:
            roll = number
        if player == 1:
            self.__p1_pos += roll
            if self.__p1_pos > 38:
                self.__p1_pos = self.__p1_pos - 39
                self.__p1_money += 200
            print("Player 1 has landed on %.10s"%Game.name(self,self.__p1_pos))
            if self.__p1_pos == 4 or self.__p1_pos == 38:
                Game.tax(self,1)
            elif self.__p1_pos == 2 or self.__p1_pos == 17 or self.__p1_pos == 33:
                # community chest
            elif self.__p1_pos == 7 or self.__p1_pos == 22 or self.__p1_pos == 36:
                # chance
            elif self.__p1_pos == 10:
                Game.just(self,1)
            elif self.__p1_pos == 20:
                Game.free(self,1)
            elif self.__p1_pos == 0:
                Game.go(self,1)
            else:
                # land on house
        
        if player == 2:
            self.__p2_pos_pos += roll
            if self.__p2_pos > 38:
                self.__p2_pos = self.__p2_pos - 39
                self.__p2_money += 200
            print("Player 2 has landed on %.10s"%Game.name(self,self.__p2_pos))
            if self.__p2_pos == 4 or self.__p2_pos == 38:
                Game.tax(self,2)
            elif self.__p2_pos == 2 or self.__p2_pos == 17 or self.__p2_pos == 33:
                # community chest
            elif self.__p2_pos == 7 or self.__p2_pos == 22 or self.__p2_pos == 36:
                # chance
            elif self.__p2_pos == 10:
                Game.just(self,2)
            elif self.__p2_pos == 20:
                Game.free(self,2)
            elif self.__p2_pos == 30:
                Game.jail(self,2)
            elif self.__p2_pos == 0:
                Game.go(self,2)
            else:
                # land on house
                
        if player == 3:
            self.__p3_pos += roll
            if self.__p3_pos > 38:
                self.__p3_pos = self.__p3_pos - 39
                self.__p3_money += 200
            print("Player 3 has landed on %.10s"%Game.name(self,self.__p3_pos))
            if self.__p3_pos == 4 or self.__p3_pos == 38:
                Game.tax(self,3)
            elif self.__p3_pos == 2 or self.__p3_pos == 17 or self.__p3_pos == 33:
                # community chest
            elif self.__p3_pos == 7 or self.__p3_pos == 22 or self.__p3_pos == 36:
                # chance
            elif self.__p3_pos == 10
                Game.just(self,3)
            elif self.__p3_pos == 20:
                Game.free(self,3)
            elif self.__p3_pos == 30:
                Game.jail(self,3)
            elif self.__p3_pos == 0:
                Game.go(self,3)
            else:
                # land on house
                
        if player == 4:
            self.__p4_pos += roll
            if self.__p4_pos > 38:
                self.__p4_pos = self.__p4_pos - 39
                self.__p4_money += 200
            print("Player 4 has landed on %.10s"%Game.name(self,self.__p4_pos))
            if self.__p4_pos == 4 or self.__p4_pos == 38:
                Game.tax(self,4)
            elif self.__p4_pos == 2 or self.__p4_pos == 17 or self.__p4_pos == 33:
                # community chest
            elif self.__p4_pos == 7 or self.__p4_pos == 22 or self.__p4_pos == 36:
                # chance
            elif self.__p4_pos == 10:
                Game.just(self,4)
            elif self.__p4_pos == 20:
                Game.free(self,4)
            elif self.__p4_pos == 30:
                Game.jail(self,4)
            elif self.__p4_pos == 0:
                Game.go(self,4)
            else:
                # land on house
                
    def pay(self,amount,frm,to):
        if frm == 1:
            self.__p1_money -= amount
            print("Player 1 now has %.10f M"%self.__p1_money)
        if frm == 2:
            self.__p2_money -= amount
            print("Player 2 now has %.10f M"%self.__p2_money)
        if frm == 3:
            self.__p3_money -= amount
            print("Player 3 now has %.10f M"%self.__p3_money)
        if frm == 4:
            self.__p4_money -= amount
            print("Player 4 now has %.10f M"%self.__p4_money)
        if frm == 'free':
            self.__free_money -= amount
        
        if to == 1:
            self.__p1_money += amount
            print("Player 1 now has %.10f M"%self.__p1_money)
        if to == 2:
            self.__p2_money += amount
            print("Player 2 now has %.10f M"%self.__p2_money)
        if to == 3:
            self.__p3_money += amount
            print("Player 3 now has %.10f M"%self.__p3_money)
        if to == 4:
            self.__p4_money += amount
            print("Player 4 now has %.10f M"%self.__p4_money)
        if to == 'free':
            self.__free_money += amount
            print("Free Parking now has %.10f M"%self.__free_money)
                            
    def roll(self):
        return random.randrange(1,6)+random.randrange(1,6)
    
    def name(self,position):
        return self.__name_array[position]
    
    def jail(self,player):
        if player == 1:
            self.__p1_jail = True
            self.__p1_pos = 10
        if player == 2:
            self.__p2_jail = True
            self.__p2_pos = 10
        if player == 3:
            self.__p3_jail = True
            self.__p3_pos = 10
        if player == 4:
            self.__p4_jail = True
            self.__p4_pos = 10
            
    def go(self,player):
        None
            
    def free(self,player):
        if player == 1:
            Game.pay(self,self.__free_money,'free',1)
        if player == 2
            Game.pay(self,self.__free_money,'free',2)
        if player == 3:
            Game.pay(self,self.__free_money,'free',3)
        if player == 4:
            Game.pay(self,self.__free_money,'free',4)
        
    def just(self,player):
        None

    def tax(self,player):
        if player == 1:
            if self.__p1_pos == 4:
                Game.pay(self,200,1,'bank')
            else:
                Game.pay(self,100,1,'bank')
        if player == 2:
            if self.__p2_pos == 4:
                Game.pay(self,200,2,'bank')
            else:
                Game.pay(self,100,2,'bank')
        if player == 3:
            if self.__p1_pos == 4:
                Game.pay(self,200,3,'bank')
            else:
                Game.pay(self,100,3,'bank')
        if player == 4:
            if self.__p1_pos == 4:
                Game.pay(self,200,4,'bank')
            else:
                Game.pay(self,100,4,'bank')
                
    def outofjail(self,player)
        if player == 1:
            choice = None
            while choice != 'a' or choice != 'b':
                choice = str(input("Player 1, type 'a' if you want to roll to get out of jail or type 'b' if you want to pay 50 M to get out of jail"))
            if choice == 'a':
                roll_1 = random.randint(1,6)
                roll_2 = random.randint(1,6)
                if roll_1 == roll_2:
                    print("Player 1 has rolled out of jail")
                    self.__p1_jail = False
                    self.__p1_jailtime = 0
                    Game.move(self,1,roll_1*2)
                elif self.__p1_jailtime == 2:
                    if self.__p1_money > 49:
                        self.__p1_money -= 50
                        print("Player 1 has been forced to pay 50 M to get out of jail")
                    else:
                        self.__p1_bank = True
                        print("Player 1 cannot afford to get out of jail and so has gone bankrupt")
                else:
                    self.__p1_jailtime += 1
                    print("Player 1 has failed to get out of jail and will stay there for the rest of the round")
            else:
                if self.__p1_money > 49:
                    self.__p1_money -= 50
                    Game.move(self,1)
                else:
                    self.__p1_bank = True
                    print("Player 1 has gone bankrupt")
        if player == 2:
            choice = None
            while choice != 'a' or choice != 'b':
                choice = str(input("Player 2, type 'a' if you want to roll to get out of jail or type 'b' if you want to pay 50 M to get out of jail"))
            if choice == 'a':
                roll_1 = random.randint(1,6)
                roll_2 = random.randint(1,6)
                if roll_1 == roll_2:
                    print("Player 2 has rolled out of jail")
                    self.__p2_jail = False
                    self.__p2_jailtime = 0
                    Game.move(self,1,roll_1*2)
                elif self.__p2_jailtime == 2:
                    if self.__p2_money > 49:
                        self.__p2_money -= 50
                        print("Player 2 has been forced to pay 50 M to get out of jail")
                    else:
                        self.__p2_bank = True
                        print("Player 2 cannot afford to get out of jail and so has gone bankrupt")
                else:
                    self.__p2_jailtime += 1
                    print("Player 2 has failed to get out of jail and will stay there for the rest of the round")
            else:
                if self.__p2_money > 49:
                    self.__p2_money -= 50
                    Game.move(self,1)
                else:
                    self.__p2_bank = True
                    print("Player 2 has gone bankrupt")
        if player == 3:
            choice = None
            while choice != 'a' or choice != 'b':
                choice = str(input("Player 3, type 'a' if you want to roll to get out of jail or type 'b' if you want to pay 50 M to get out of jail"))
            if choice == 'a':
                roll_1 = random.randint(1,6)
                roll_2 = random.randint(1,6)
                if roll_1 == roll_2:
                    print("Player 3 has rolled out of jail")
                    self.__p3_jail = False
                    self.__p3_jailtime = 0
                    Game.move(self,1,roll_1*2)
                elif self.__p3_jailtime == 2:
                    if self.__p3_money > 49:
                        self.__p3_money -= 50
                        print("Player 3 has been forced to pay 50 M to get out of jail")
                    else:
                        self.__p3_bank = True
                        print("Player 3 cannot afford to get out of jail and so has gone bankrupt")
                else:
                    self.__p3_jailtime += 1
                    print("Player 3 has failed to get out of jail and will stay there for the rest of the round")
            else:
                if self.__p3_money > 49:
                    self.__p3_money -= 50
                    Game.move(self,1)
                else:
                    self.__p3_bank = True
                    print("Player 3 has gone bankrupt")
        if player == 4:
            choice = None
            while choice != 'a' or choice != 'b':
                choice = str(input("Player 4, type 'a' if you want to roll to get out of jail or type 'b' if you want to pay 50 M to get out of jail"))
            if choice == 'a':
                roll_1 = random.randint(1,6)
                roll_2 = random.randint(1,6)
                if roll_1 == roll_2:
                    print("Player 4 has rolled out of jail")
                    self.__p4_jail = False
                    self.__p4_jailtime = 0
                    Game.move(self,1,roll_1*2)
                elif self.__p4_jailtime == 2:
                    if self.__p4_money > 49:
                        self.__p4_money -= 50
                        print("Player 4 has been forced to pay 50 M to get out of jail")
                    else:
                        self.__p4_bank = True
                        print("Player 4 cannot afford to get out of jail and so has gone bankrupt")
                else:
                    self.__p4_jailtime += 1
                    print("Player 4 has failed to get out of jail and will stay there for the rest of the round")
            else:
                if self.__p4_money > 49:
                    self.__p4_money -= 50
                    Game.move(self,1)
                else:
                    self.__p4_bank = True
                    print("Player 4 has gone bankrupt")
    def chance(self,player):
        chance_no = random.randint(0,15)
        chance_array = ["Advance to Go","Advance to Trafalgar Square","Advance to Mayfair","Advance to Pall Mall","Advance to the Nearest Station. If unowned, you may buy it from the Bank. If owned, pay the owner twice the rental to which they are entitled","Advance to the nearest utility. If unowned, you may buy it from the bank. If owned, roll and pay the owner ten times the amount thrown","Bank pays you dividend of 50 M","Get out of Jail free card","Go back 3 spaces","Go to Jail","Make general repairs on your property. For each house pay 25 M. For each hotel pay 100 M","Speeding fine 15 M","Take a trip to Kings Cross Station","You have been elected chairman of the board. Pay each player 50 M","Your building loan matures. Collcet 150M"]
        if player == 1:
            if chance_no == 0:
                print("Player 1 chance: ",chance_array[0])
                Game.move(self,1,39-self.__p1_pos)
            if chance_no == 2:
                print("Player 1 chance: ",chance_array[1])
                Game.move(self,1,39+24-self.__p1_pos)
            
        
                    
    def animateboard(self):
        plt.show()

#%%

import matplotlib.pyplot as plt
plt.figure(facecolor='honeydew')
ax = plt.axes()
ax.set_facecolor("honeydew")
ax.grid(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_xlim(0,24)
ax.set_ylim(0,24)
ax.add_patch(pl.Rectangle([3,3],18,18,ec='black',fc='honeydew'))

#Corners
ax.add_patch(pl.Rectangle([0,0],3,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,0],3,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,21],3,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,21],3,3,ec='black',fc='honeydew'))

#Cells left
ax.add_patch(pl.Rectangle([0,3],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,5],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,7],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,9],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,11],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,13],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,15],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([0,17],3,2,ec='black',fc='honeydew'))

#Cells top
ax.add_patch(pl.Rectangle([3,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([5,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([7,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([9,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([11,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([13,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([15,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([17,21],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([19,21],2,3,ec='black',fc='honeydew'))

#Cells right
ax.add_patch(pl.Rectangle([21,3],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,5],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,7],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,9],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,11],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,13],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,15],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,17],3,2,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([21,19],3,2,ec='black',fc='honeydew'))

#Cells bottom
ax.add_patch(pl.Rectangle([3,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([5,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([7,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([9,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([11,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([13,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([15,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([17,0],2,3,ec='black',fc='honeydew'))
ax.add_patch(pl.Rectangle([19,0],2,3,ec='black',fc='honeydew'))

#Light blue
ax.add_patch(pl.Rectangle([3,2.5],2,0.5,ec='black',fc='lightblue'))
ax.add_patch(pl.Rectangle([5,2.5],2,0.5,ec='black',fc='lightblue'))
ax.add_patch(pl.Rectangle([9,2.5],2,0.5,ec='black',fc='lightblue'))

#brown
ax.add_patch(pl.Rectangle([15,2.5],2,0.5,ec='black',fc='brown'))
ax.add_patch(pl.Rectangle([19,2.5],2,0.5,ec='black',fc='brown'))
ax.text(19.25,2,"Old Kent Road",fontsize=3)
ax.text(15.25,2,"Whitechapel Road",fontsize=3)

#blue
ax.add_patch(pl.Rectangle([21,3],0.5,2,ec='black',fc='blue'))
ax.add_patch(pl.Rectangle([21,7],0.5,2,ec='black',fc='blue'))

#green
ax.add_patch(pl.Rectangle([21,19],0.5,2,ec='black',fc='green'))
ax.add_patch(pl.Rectangle([21,17],0.5,2,ec='black',fc='green'))
ax.add_patch(pl.Rectangle([21,13],0.5,2,ec='black',fc='green'))

#yellow
ax.add_patch(pl.Rectangle([19,21],2,0.5,ec='black',fc='yellow'))
ax.add_patch(pl.Rectangle([15,21],2,0.5,ec='black',fc='yellow'))
ax.add_patch(pl.Rectangle([13,21],2,0.5,ec='black',fc='yellow'))

#red
ax.add_patch(pl.Rectangle([3,21],2,0.5,ec='black',fc='red'))
ax.add_patch(pl.Rectangle([7,21],2,0.5,ec='black',fc='red'))
ax.add_patch(pl.Rectangle([9,21],2,0.5,ec='black',fc='red'))

#orange
ax.add_patch(pl.Rectangle([2.5,19],0.5,2,ec='black',fc='orange'))
ax.add_patch(pl.Rectangle([2.5,17],0.5,2,ec='black',fc='orange'))
ax.add_patch(pl.Rectangle([2.5,13],0.5,2,ec='black',fc='orange'))

#pink
ax.add_patch(pl.Rectangle([2.5,3],0.5,2,ec='black',fc='pink'))
ax.add_patch(pl.Rectangle([2.5,5],0.5,2,ec='black',fc='pink'))
ax.add_patch(pl.Rectangle([2.5,9],0.5,2,ec='black',fc='pink'))





plt.show()
#%%
c= 43
d =3

def move(c,d=False):
    if d == False:
        print(1)
    else:
        print(d)
        
move(c,d)