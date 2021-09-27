import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cardgame = CardGame
        self.card1 = Card("diamonds", 2)
        self.card2 = Card("hearts", 6)
        self.card3 = Card("clubs", 9)
        self.card4 = Card("spades", 1)
        self.cards = [self.card1,self.card2, self.card3, self.card4]

    def test__check_for_ace(self):
        test_result = self.cardgame.check_for_ace(self, self.card4)
        self.assertTrue(test_result)

    def test__highest_card(self):
        test_result = self.cardgame.highest_card(self, self.card2,self.card3)
        self.assertEqual(self.card3, test_result)

    def test__cards_total(self):
        test_result = self.cardgame.cards_total(self,self.cards)
        self.assertEqual("You have a total of" + str(18), test_result)