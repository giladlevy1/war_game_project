from unittest import TestCase
from games.cards.card import card

class Testcard(TestCase):
    def setUp(self):
        print("setUp:")
        self.card1 = card(5, "♦")
        self.card2 = card(5, "♣")
        self.card3 = card(8, "♥")
        print("=================================================")

    def tearDown(self):
        print("tearDown ^")

    def test___gt___1(self): # test that a card with a bigger value, is in fact stronger.
        self.assertTrue(self.card1 < self.card3)

    def test___gt___2(self): # test that cards with the same value, the suit will determine which card is stronger.
        self.assertTrue(self.card1 < self.card2)




