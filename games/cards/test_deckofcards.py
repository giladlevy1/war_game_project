from unittest import TestCase
from games.cards.deckofcards import deckofcards
from games.cards.card import card

class TestDeckofcards(TestCase):
    def setUp(self):
        print("setUp:")
        self.deck1 = deckofcards()
        print("=================================================")

    def tearDown(self):
        print("tearDown ^")

    def test_shuffle_1(self):# test that a shuffled deck is different than a regular deck
        deck2 = self.deck1.decklist.copy()
        self.deck1.shuffle()
        self.assertTrue(deck2 != self.deck1.decklist)

    def test_shuffle_2(self): # test that the shuffle won't work if the deck has less than 52 cards
        self.deck1.decklist.remove(self.deck1.decklist[0]) # removing the first card from the deck
        deck2 = self.deck1.decklist.copy()
        self.deck1.shuffle()
        self.assertTrue(self.deck1.decklist == deck2)

    def test_dealone_1(self): # test that dealone function removes the first card
        self.deck1.dealone()
        self.assertTrue(len(self.deck1.decklist) == 51)

    def test_dealone_2(self): # test that dealone function removes the first card when deck has only one card.
        self.card1 = card(8,"♠")
        self.deck1.decklist = []
        self.deck1.decklist.append(self.card1)
        self.deck1.dealone()
        self.assertTrue(len(self.deck1.decklist) == 0)

    def test_dealone_3(self): # test that an empty deck w'ont give an error, and function runs
        self.deck1.decklist = []
        try:
            self.deck1.dealone()
        except:
            pass
        else:
            self.fail()

    def test_newgame_1(self): # test that newgame creates a new full deck
        self.deck1.newgame()
        self.assertTrue(len(self.deck1.decklist) == 52)

    def test_newgame_2(self): #test that newgame shuffles the new created deck
        deck2 = self.deck1.decklist.copy()
        self.deck1.newgame()
        self.assertTrue(deck2 != self.deck1.decklist)

    def test_show(self):
        pass
