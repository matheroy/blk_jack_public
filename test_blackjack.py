'''module that contains all the tests for major blackjack functions

Run this module independently with the pytest app
- If not already installed:
1. install with: pip install pytest
then
2. python -m pytest test_blackjack.py
or better yet, get verbose info with
3. py.test test_blackjack.py -v
'''


#import blackjack
import blackjack_core as core


def test_create_deck():
    '''create your test your deck '''

    test_deck = core.Deck()
    #print(test_deck) # this will print out the deck in order
    assert len(test_deck.deck) == 52

def test_shuffle_deck():
    '''shuffle the deck'''

    test_deck = core.Deck()
    test_deck.shuffle()
    #print(test_deck) # this print out a shuffled deck in random order
    assert test_deck.shuffled == True # if false, it will raise an error

def test_create_player_hand():
    '''create your test player's hand build process'''

    # define your players
    test_player = core.Hand()
    assert test_player.status == 1

def test_add_card():
    '''test adding a card to the hand'''

    test_deck = core.Deck()
    test_deck.shuffle()
    test_player = core.Hand()
    # deal 1 card from the deck CARD(suit, rank)
    pulled_card = test_deck.deal()
    #print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)

    assert test_player.value >= 1

    # we can also run the following code in a single line
    #self.test_player.add_card(self.test_deck.deal())
    #print(self.test_player.value)
    #print(self.test_player)
