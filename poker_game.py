import random
import sys

def game(n_of_players):
    names = [input("Please enter your name:") for i in range(int(n_of_players))]
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
    dictstring = {}  
    for x in names:
        dictstring[x] = []
        for i in range(5):
            string = random.choice(cards)
            dictstring[x] += [string]
            cards.remove(string)
        print("{}'s hand is {},{},{},{},{}.".format(
                x,
                dictstring[x][0],
                dictstring[x][1],
                dictstring[x][2],
                dictstring[x][3],
                dictstring[x][4],))

    values = {
                '2':2,
                '3':3,
                '4':4,
                '5':6,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                'J':11,
                'Q':12,
                'K':13,
                'A':14
            }

    dictvalue = {}
    for x in dictstring:
        dictvalue[x] = []
        for string in dictstring[x]:
            value = values.get(string)
            dictvalue[x] += [value]
        dictvalue[x].sort(reverse = True)
        
        
        
    compare = {}
    for name,value in dictvalue.items():
        if not compare:
            compare[name] = value
            continue
        for i in range(5):
            if value[i] == list(compare.values())[0][i]:
                continue 
            elif value[i] > list(compare.values())[0][i]:
                compare = {name:value}
                break
            break
            
    print("The winner is {}.".format(list(compare.keys())[0]))

number_of_players = int(sys.argv[1])
game(number_of_players)

        
        