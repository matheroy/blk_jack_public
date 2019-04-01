'''Python program that simulates a blackjack game with 2 players
This module will contain all the core elements and classes of the blackjack game
'''

import random


# global variables

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# boolean used to control the while loop
PLAYING = True

GAME_COUNT = 1

GAME_HANDLER = [
    {
        'game': 1,
        'winner': [],
        'loser':[]
    }
]

# define a class for all cards
class Card(object):
    '''class definition for all references and items to a single card'''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # prints out the instantiation of the card
    def __str__(self):
        return self.rank + " of " + self.suit


# define a deck to contain all cards
class Deck():
    '''class layout for all items and methods that compromise a deck'''

    def __init__(self):
        self.deck = []  # start with an empty list
        self.shuffled = False
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
            #deck_comp += card.__str__() + '\n'
        return "The deck has: " + deck_comp

    def shuffle(self):
        '''shuffle the cards in the deck'''
        try:
            random.shuffle(self.deck)
            self.shuffled = True
        except:
            raise


    def deal(self):
        '''deal a single card'''

        single_card = self.deck.pop()
        return single_card

class Hand():
    ''' manage all the cards in a player's hand and the values
    of the Ace(s) in their hand '''

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        #player hand status of whether they're continuing or staying, can
        # also be used to determine if a player is active as well
        self.status = 1

    def add_card(self, card):
        '''card passed in will be from Deck.deal() --> Single Card(suit, rank)'''

        self.cards.append(card)
        self.value += VALUES[card.rank]

        # track the number of Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        ''' This method adjusts for the ace to be either 1 or 11'''

        #if the total value > 21 and I still have an Ace
        # then adjust the value of the ace to a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            # this also regulates the while loop
            # decrementing self.aces to 0, will break out of the loop
            self.aces -= 1

    def __str__(self):
        '''provides a string representation of the class'''

        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n' + card.__str__()
            #deck_comp += card.__str__() + '\n'
        return "This hand has : " + hand_comp

class Chips():
    ''' manage all the chips/money that a player has in their account '''

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        '''update the total if the player wins the bet'''

        self.total += self.bet

    def lose_bet(self):
        '''update the total if the player losses the bet'''

        self.total -= self.bet



def main():
    '''call all your tests and other activities'''

    test_deck = Deck()
    #print(test_deck) # this will print out the deck in order
    test_deck.shuffle()
    #print(test_deck) # this print out a shuffled deck in random order

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



# Run the main function if this module is called by itself.
# This will prevent overlaps of the main function in case this module is imported by another
if __name__ == '__main__':

	main()
