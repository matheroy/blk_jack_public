'''module that contains all the tests for major blackjack functions'''

import unittest
from blackjack import *


def validate_deck_test():
    '''test your deck build process'''

    test_deck = Deck()
    #print(test_deck) # this will print out the deck in order
    test_deck.shuffle()
    #print(test_deck) # this print out a shuffled deck in random order
    return test_deck


def validate_player_test(test_deck):
    '''test your player build process'''

    # define your players
    test_player = Hand()
    # deal 1 card from the deck CARD(suit, rank)
    pulled_card = test_deck.deal()
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)

    # we can also run the following code in a single line
    test_player.add_card(test_deck.deal())
    print(test_player.value)
    print(test_player)

    return


def validation_tests():
    '''run your validation tests from a central test process'''

    test_deck = validate_deck_test()
    validate_player_test(test_deck)

    return
