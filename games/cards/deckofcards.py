import random
from games.cards.card import card
from termcolor import colored # i used pip to download this function

class deckofcards:
    def __init__(self): # a deck contains all possible options of a card, meaning 52 cards in a deck.
        self.decklist = []
        self.valuelist = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.suitlist = ["♦","♠","♥","♣"]

        self.suitlist[0] = colored("♦","red") # function to color the card's suit
        self.suitlist[2] = colored("♥", "red")

        for value in self.valuelist:
            for suit in self.suitlist:
                card1 = card(value,suit)
                self.decklist.append(card1) # creating a deck with 52 cards.

    def shuffle(self): # shuffles the cards in the deck
        if len(self.decklist) == 52: # # can only work when deck is full
            random.shuffle(self.decklist)
        else:
            pass

    def dealone(self): # returning a card from the top of the deck, then deletes it.
        if len(self.decklist) > 0: # can only work when deck has cards
            c = self.decklist[0]
            self.decklist.remove(self.decklist[0])
            return c
        else:
            raise ValueError("deck empty, cant deal a card")

    def newgame(self): # creates a new deck and shuffles it.
        self.decklist = []
        for value in self.valuelist:
            for suit in self.suitlist:
                card1 = card(value,suit)
                self.decklist.append(card1)
        random.shuffle(self.decklist)

    def show(self): # prints the created deck.
        print(self.decklist)


