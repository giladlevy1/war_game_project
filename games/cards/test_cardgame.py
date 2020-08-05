from unittest import TestCase
from games.cards.cardgame import cardgame

class Testcardgame(TestCase):
    def setUp(self):
        print("setUp:")
        self.testgame = cardgame(1000,5)
        print("=================================================")

    def tearDown(self):
        print("tearDown ^")

    def test_newgame(self): # test that newgame function deals new cards to the players - meaning a new game is created.
        first_player_1 = self.testgame.playerslist[0]
        first_cards_1 = first_player_1.cardsinhand
        self.testgame.newgame()
        first_player_2 = self.testgame.playerslist[0]
        first_cards_2 = first_player_2.cardsinhand

        self.assertTrue(first_cards_1 != first_cards_2)

    def test_players_money_1(self): # test that when given positive number of money, will work.
        for player in self.testgame.playerslist:
            self.assertTrue(player.money_amount == 1000)

    def test_players_money_2(self): # test that when given zero money, will work.
        testgame2 = cardgame(0)
        for player in testgame2.playerslist:
            self.assertTrue(player.money_amount == 0)

    def test_players_money_3(self): # test that when given negative number of money will cause an error.
        try:
            testgame2 = cardgame(-500)
        except:
            pass
        else:
            self.fail()

    def test_players_money_4(self): # test that when given "str" in money will cause an error.
        try:
            testgame2 = cardgame("str")
        except:
            pass
        else:
            self.fail()

    def test_players_cards_1(self): # test that when given positive number of cards, will work.
        for player in self.testgame.playerslist:
            self.assertTrue(player.card_amount == 5)

    def test_players_cards_2(self): # test that zero cards will cause an error.
        try:
            testgame2 = cardgame(500,0)
        except:
            pass
        else:
            self.fail()

    def test_players_cards_3(self): # test that negative number of cards will cause an error.
        try:
            testgame2 = cardgame(500,-5)
        except:
            pass
        else:
            self.fail()


    def test_players_cards_4(self): # test that "str" amount of cards will cause an error.
        try:
            testgame2 = cardgame(500,"str")
        except:
            pass
        else:
            self.fail()