from unittest import TestCase , mock
from unittest.mock import patch
from games.cards.player import player
from games.cards.deckofcards import deckofcards
from games.cards.card import card

class TestPlayer(TestCase):
    def setUp(self):
        print("setUp:")
        self.player1 = player("Gilad",5000,5)
        self.deck1 = deckofcards()
        print("=================================================")

    def tearDown(self):
        print("tearDown ^")

    def test_sethand_1(self): # test that the player gets in hand the amount of cards given. (this case -> 5 cards)
        self.player1.sethand(self.deck1)
        self.assertTrue(len(self.player1.cardsinhand) == self.player1.card_amount)

    def test_sethand_2(self): # test that - when i mock dealone to a specific card, it adds to the player's cards in hand.
        with patch("games.cards.deckofcards.deckofcards.dealone") as mocked_deal_one:
            self.card1 = card(8,"♠")
            mocked_deal_one.return_value = self.card1
            self.player1.sethand(self.deck1)
            self.assertIn(self.card1 , self.player1.cardsinhand)

    def test_sethand_3(self): # test that sethand function, when given an invalid deck, results an error
        self.player1.cardsinhand = []
        try:
            self.player1.getcard()
        except:
            pass
        else:
            self.fail()

    def test_getcard_1(self): # test that getcard function removes one card from the player's hand.
        self.player1.sethand(self.deck1)
        self.player1.getcard()
        self.assertTrue(len(self.player1.cardsinhand) == self.player1.card_amount - 1)

    def test_getcard_2(self): # test that getcard function runs when player has no cards
        self.player1.cardsinhand = []
        try:
            self.player1.getcard()
        except:
            pass
        else:
            self.fail()

    def test_addcard_1(self): # test that addcard, adds the given card to the player's hand.
        self.card1 = card(8, "♠")
        self.player1.addcard(self.card1)
        self.assertIn(self.card1 , self.player1.cardsinhand)

    def test_addcard_2(self): # test that addcard, when adds an invalid card, will result with an error.
        try:
            self.player1.addcard(8)
        except:
            pass
        else:
            self.fail()

    def test_reduceamount_1(self): # test that reduceamount function, reduces the given money amount from the player's money
        before_change_money = self.player1.money_amount
        self.player1.reduceamount(1000)
        self.assertTrue(before_change_money - 1000 == self.player1.money_amount)

    def test_reduceamount_2(self): # test that reduceamount function, when given zero money, will cause an error
        try:
            self.player1.reduceamount(0)
        except:
            pass
        else:
            self.fail()
    def test_reduceamount_3(self): # test that reduceamount function, when given a negative amount of money, will result with an error
        try:
            self.player1.reduceamount(-1000)
        except:
            pass
        else:
            self.fail()

    def test_reduceamount_4(self): # test that reduceamount function, when given "str", will result with an error
        try:
            self.player1.reduceamount("str")
        except:
            pass
        else:
            self.fail()

    def test_addamount_1(self): # test that addamount function, adds the given money amount to the player's money
        before_change_money = self.player1.money_amount
        self.player1.addamount(1000)
        self.assertTrue(before_change_money + 1000 == self.player1.money_amount)

    def test_addamount_2(self): # test that addamount function, when given zero money, will cause an error
        try:
            self.player1.addamount(0)
        except:
            pass
        else:
            self.fail()

    def test_addamount_3(self): # test that addamount function, when given a negative amount of money, will result with an error
        try:
            self.player1.addamount(-1000)
        except:
            pass
        else:
            self.fail()

    def test_addamount_4(self): # test that addamount function, when given "str", will result with an error
        try:
            self.player1.reduceamount("str")
        except:
            pass
        else:
            self.fail()




