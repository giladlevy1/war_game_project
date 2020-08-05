from games.cards.cardgame import cardgame
import random
import time

                                               # creating a card game named: "war"
war = cardgame((random.randint(5000,10000)),5) # all players start with the same amount of money, randomly from 5,000-10,000)
                                               # all players get 5 cards
for player1 in war.playerslist:
    pp = war.playerslist.index(player1) + 1
    player1.name = input("Enter Player "+str(pp)+" name:")
    if player1.name == "":  # if the user enters an empty name for the player - the default will be - "player" plus the number of the player.
        player1.name = f'Player {pp}'
print("=================================================")
for pl in war.playerslist:
    print(pl)
print("=================================================")
time.sleep(3)
for t in range (1,6): # the game has 5 rounds, one for each player's card.
    bank = 0
    roundbet = 100*t # each round - the players are betting the amount of money from their hand, depanding on the number of the round.
    thisroundcards = [] # a list of the round's cards.
    for pl in war.playerslist:
        pl.reduceamount(roundbet)
        bank = bank + roundbet
        thisroundcards.append(pl.cardsinhand[0]) # moving the top card of each player to this round's cards list.

    # the following code lines refrences to the __gt__ function written in the "card" module.
    # deciding which card from this round's cards, is "stronger".
    max1 = 0
    max2 = 0

    if thisroundcards[0] > thisroundcards[1]:
        max1 = 0
    else:
        max1 = 1

    if thisroundcards[2] > thisroundcards[3]:
        max2 = 2
    else:
        max2 = 3

    if thisroundcards[max1] > thisroundcards[max2]:
        pass
    else:
        max1=max2

    winnerplayer = ""
    for pl in war.playerslist:
        for i in range (len(pl.cardsinhand)):
            if thisroundcards[max1] == pl.cardsinhand[i]: # if one of the players (the winner player) has a card i his hand, which is equal to the strongest card in this round's cards list:
                pl.addamount(bank) # adds to the winner player the money from the round's bank
                winnerplayer = pl.name
        pl.cardsinhand.remove(pl.cardsinhand[0]) # removes the played card from the players hands.

    print(f'round {t} - the cards that were played: {thisroundcards}')
    print(f'{winnerplayer} is the winner for round {t}')
    print("=================================================")
    time.sleep(3)

print("Final war game results are:")
for pl in war.playerslist:
    print(pl.name,"- money amount:",pl.money_amount,"$")
print("=================================================")

moneylist = []
winnerslist = []
for pl in war.playerslist:
    moneylist.append(pl.money_amount)

maxmoney = max(moneylist) # the biggest amount of money, from the players final money amount.
for pl in war.playerslist:
    if maxmoney == pl.money_amount:
        winnerslist.append(pl) # the player with the biggest amount of money, is added to the winners list. if there are more than one winner, their all added.
if len(winnerslist) == 1:
    print("the winner of this war game is", winnerslist[0].name, "with", maxmoney,"$")
if len(winnerslist) == 2:
    print("the winners of this war game are", winnerslist[0].name,"and",winnerslist[1].name, "with", maxmoney,"$")
if len(winnerslist) == 3:     # the maximum players that can win one game are 3
    print("the winners of this war game are", winnerslist[0].name,",",winnerslist[1].name, "and",winnerslist[2].name, "with", maxmoney, "$")