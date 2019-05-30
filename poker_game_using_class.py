#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:23:25 2019

@author: dongxujia
"""

import random
import sys

n = int(sys.argv[1])
    
class poker_game:
    
    def __init__(self):
        self.number_of_players = n
        self.names = [input("Please enter your name:") for i in range(self.number_of_players)]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
        self.dictstring = {}
        self.dictvalue = {}
        self.compared = {}
        self.values = {
			'2':2,
			'3':3,
			'4':4,
			'5':6,
			'6':6,
			'7':7,
			'8':8,
			'9':9,
			'T':10,
			'J':11,
			'Q':12,
			'K':13,
			'A':14
		}
        
    def play(self):
        for x in self.names:
            self.dictstring[x] = []
            for i in range(5):
                string = random.choice(self.cards)
                self.dictstring[x] += [string]
                self.cards.remove(string)
            print("{}'s hand is {},{},{},{},{}.".format(
                    x,
                    self.dictstring[x][0],
                    self.dictstring[x][1],
                    self.dictstring[x][2],
                    self.dictstring[x][3],
                    self.dictstring[x][4],))
                    
    def get_value(self):
        for s in self.dictstring:
            self.dictvalue[s] = []
            for string in self.dictstring[s]:
                value = self.values.get(string)
                self.dictvalue[s] += [value]
            self.dictvalue[s] = sorted(self.dictvalue[s],reverse = True)
            



            
    def compare(self):
        for name,values in self.dictvalue.items():
            if not self.compared:
                self.compared[name] = values
                continue
            for i in range(5):
                if values[i] == list(self.compared.values())[0][i]:
                    continue 
                elif values[i] > list(self.compared.values())[0][i]:
                    self.compared = {name:values}
                    break
                break
        print ("The winner is {}.".format(list(self.compared.keys())[0]))
        
        
a = poker_game()
a.play()
a.get_value()
a.compare()




        
        
    