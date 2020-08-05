from games.cards.deckofcards import deckofcards
from games.cards.player import player

class cardgame:
    def __init__(self, money, cards_player = 5): # a card game contains a deck and some players.
        self.money = money
        self.cards_player = cards_player
        self.deck1 = deckofcards()
        self.newgame()

        if type(money) == int: # money paramater has to be a number
            if money >= 0:
                pass
            else:
                raise ValueError("can only enter a positive number of money or zero")
        else:
            raise ValueError("can only enter a valid number of money")

        if type(cards_player) == int: # cards_player paramater has to be a number
            if cards_player > 0:
                pass
            else:
                raise ValueError("can only enter a positive number of cards")
        else:
            raise ValueError("can only enter a valid number of cards")


    def newgame(self): # creating a new deck and shuffles it. then dealing cards to the players hand's.
        self.deck1.newgame()
        self.playerslist = []
        for i in range (1,5): # a card game contains 4 players.
            player1 = player("Player "+str(i) , self.money , self.cards_player)
            player1.sethand(self.deck1)
            self.playerslist.append(player1)