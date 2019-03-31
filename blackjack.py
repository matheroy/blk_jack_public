'''This Python program will contain all the functions and processes
that simulates a blackjack game with 2 players
'''
import sys
#import os
#import random
#import timer
from blackjack_core import *

def take_bet(total_funds):
    '''prompt the player for the bet and place it'''
    while True:
        try:
            bet = int(input("How much of your $%s, would you like to bet: "%(total_funds)))
        except:
            print("Sorry, that is not a valid amount, please only provide numbers.")
        else:
            if bet <= total_funds:
                break
            else:
                print("Sorry, you don't have enough funds.  You have {}".format(total_funds))

    return bet


def hit(deck,hand):
    '''function that adds another card to the player'''

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

    return


def hit_or_stand(deck,hand):
    '''ask the player to either hit or stand on their hand'''

    global PLAYING  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s ') # h for Hit and s for Stand
        #print(x, x[0])
        if x[0].lower() == 'h':
            hit(deck, hand)
            

        elif x[0].lower() == 's':
            print("Player Stands, Dealer's turn. ")
            PLAYING = False

        else:
            print("Sorry, I didn't understand your response.  Please enter either a h or s only!")
            continue

        break

    return


def show_some(player,dealer):
    '''show only the player hand and not the dealers' hand '''

    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    #print("Dealer's Hand =",dealer.value)
    print("Dealer's Hand =", VALUES[dealer.cards[1].rank])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

    return

def show_all(player,dealer):
    '''show everyone's hands '''

    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

    return


def player_busts(player, dealer, chips):
    '''info when the player busts a game'''

    print("Player loses!  Bust!")
    chips.lose_bet()

    return

def player_wins(player, dealer, chips):
    '''info when the player wins a game'''

    print("Player Wins!")
    chips.win_bet()

    return

def dealer_busts(player, dealer, chips):
    '''info when the dealer busts a game'''

    print("Player Wins! Dealer Busts!")
    chips.win_bet()

    return

def dealer_wins(player, dealer, chips):
    '''info when the dealer wins a game'''

    print("Dealer Wins! Player Busts!")
    chips.lose_bet()

    return

def push(player, dealer):
    '''both player and dealer ties'''

    print("Dealer and Player ties! PUSH!")

    return

def play():
    '''play the game '''

    global PLAYING
    global GAME_COUNT

    while True:
        print('*'*20)
        print("Let's get ready to play Blackjack!!")
        print('*'*20)

        # Create & shuffle the deck, deal two cards to each player
        new_deck = Deck()
        new_deck.shuffle()

        # create an empty hand for each player
        player1_hand = Hand()
        dealer_hand = Hand()

        # deal each player 2 cards at the start
        for x in range(2): #[1,2]:
            player1_hand.add_card(new_deck.deal())
            dealer_hand.add_card(new_deck.deal())

        # Set up the Player's intial count of chips
        if GAME_COUNT == 1: 
            player1_chips = Chips()
        #dealer has infinite amout of money

        # Prompt the Player for their bet
        player1_chips.bet = take_bet(player1_chips.total)


        # Show cards (but keep one dealer card hidden)
        #print("Player 1: ",player1)
        #print("Dealer face up card: ", dealer.cards[-1])
        show_some(player1_hand, dealer_hand)


        while PLAYING:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(new_deck, player1_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player1_hand, dealer_hand)
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player1_hand.value > 21:
                player_busts(player1_hand, dealer_hand, player1_chips)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player1_hand.value <=21 and not PLAYING:

                while dealer_hand.value < player1_hand.value:
                    hit(new_deck, dealer_hand)

                # Show all cards
                show_all(player1_hand, dealer_hand)
            else:
                continue

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player1_hand, dealer_hand, player1_chips)
            elif dealer_hand.value > player1_hand.value:
                dealer_wins(player1_hand, dealer_hand, player1_chips)
            elif dealer_hand.value < player1_hand.value:
                player_wins(player1_hand, dealer_hand, player1_chips)
            else:
                push(player1_hand, dealer_hand)


        # Inform Player of their chips total
        print("\n Players total chips are at {}".format(player1_chips.total) )

        # Ask to play again
        new_game = input("Would you like to play again? y/n")

        if new_game[0].lower() == 'y':
            PLAYING = True
            player1_chips.total = player1_chips.total
            GAME_COUNT += 1
            continue
        else:
            print("Thank you for playing!!")
            break
    return


def main_blackjack(testing=0):
    '''call all your tests and other activities'''

    if testing: 
        import test_blackjack
        test_blackjack.validation_tests() 
    play()
    return


if __name__ == '__main__':

    #print("in Main")
    #print(sys.argv, type(sys.argv), len(sys.argv))
    #for index,arg in enumerate(sys.argv):
    #    print(index, arg)
    if len(sys.argv) > 1:
        test = sys.argv[1]
    else:
        test = 0
    
    main_blackjack(test)
