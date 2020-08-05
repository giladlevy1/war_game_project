import random
from games.cards.card import card
from games.cards.deckofcards import deckofcards

class player:
    def __init__(self,name,money_amount,card_amount = 5): # player's features are: name, money amount and cards in hand.
        self.name = name
        self.money_amount = money_amount
        self.card_amount = card_amount
        self.cardsinhand = []

    def __repr__(self): # player object info
        return f'{self.name} - Money amount: {self.money_amount} $, Cards in hand: {self.cardsinhand}'

    def sethand(self,deck1): # deals cards to the player's hand.
        if type(deck1) == deckofcards: # can only be a valid deck
            for i in range (self.card_amount):
                self.cardsinhand.append(deck1.dealone())
        else:
            raise ValueError(f'{deck1} is not a deck, and cant set a hand')

    def getcard(self): # removes a random card from the player's hand.
        if len(self.cardsinhand) > 0: # can only work when player has cards in his hand
            rand = random.randint(0,len(self.cardsinhand))
            d = self.cardsinhand[rand]
            self.cardsinhand.remove(self.cardsinhand[rand])
            return d
        else:
            raise ValueError("player has no cards, and cant get one")

    def addcard(self,card1): # adds a given card to the player's hand.
        if type(card1) == card: # can only be a valid card
            self.cardsinhand.append(card1)
        else:
            raise ValueError(f'{card1} is not a card, and cant be added')

    def reduceamount(self,reduced_amount): # removes a given amount of money from the player's personal money.
        if type(reduced_amount) == int: # can only be a valid number
            if reduced_amount > 0:
                self.money_amount = self.money_amount - reduced_amount
            else:
                raise ValueError("can only enter a positive number of money")
        else:
            raise ValueError("can only enter a valid number of money")

    def addamount(self,increase_amount): # adds a given amount of money to the player's personal money.
        if type(increase_amount) == int: # can only be a valid number
            if increase_amount > 0:
                self.money_amount = self.money_amount + increase_amount
            else:
                raise ValueError("can only enter a positive number of money")
        else:
            raise ValueError("can only enter a valid number of money")

    def print (self): # same as the __repr__ method
        return f'{self.name} - Money amount: {self.money_amount} $, Cards in hand: {self.cardsinhand}'