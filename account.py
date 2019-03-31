'''module that handles all the account processing for a player and their current chip totals during a game'''

import os
import timer


class Account():
    '''class that handles a player's account during the game(s)'''

    def __init__(self, account=100):
        '''set the account's initial value'''

        self.account = account
    
    def update_account(self, amount):
        '''update the account's current value'''
        self.amount = amount
        self.account += self.amount
        