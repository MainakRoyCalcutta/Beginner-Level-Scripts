"""
Betting Game: If the total sum of received numbers is more than 10
Betting on which number is given by random
First two numbers are shown from the deck of number cards then it is shuffled and if the player hits it shows the top number on the deck 
"""

import random

"""
Class to create deck and shuffle
"""


class Deck:

    def __init__(self):
        self.cards_hand = []

    def add_cards(self, adder):
        # Adding Cards to the deck
        self.cards_hand.extend(adder)

    def shuffle(self):
        # Shuffling Cards to the deck
        random.shuffle(self.cards_hand)


# Accept name and money

name = input("Enter name : ")
money = int(input("Enter money : "))

"""
Betting class
"""


class Play(Deck):

    def __init__(self, nam, monay):

        Deck.__init__(self)
        self.name = nam
        self.money = monay
        self.bett = 0

    def bet(self):

        # Accepting the bet amount
        self.bett = int(input("Enter bet amount : "))

    def bet_check(self):

        # Checking whether bet is possible or not
        if self.bett <= self.money and self.bett != 0:
            print("Bet allowed")
            self.money = self.money - self.bett
            return 0
        elif self.bett > self.money and self.bett != 0:
            print("Bet not allowed")
            Play.bet(self)
            Play.bet_check(self)
            return 1
        elif self.money == 0:
            print("Bankrupt")

        elif self.bett == 0:
            print("Please bet to continue")
            Play.bet(self)
            Play.bet_check(self)

    def aaaa(self, aa):

        # Function to calculate final balance after bet
        if aa == 0:

            self.money += self.bett * 2
            print(f"Your balance now: {self.money}")
        elif aa == 1:
            print(f"Your balance now: {self.money}")
            if self.money == 0:
                return 2

    def hit(self):

        # Function to bring a card to the table
        return self.cards_hand[0]

    def remove(self):

        # Remove the card once used
        self.cards_hand.pop(0)


x = Play(name, money)


def table_play():
    # Making a deck
    # Showing the cards to the player
    x.add_cards([1, 2, 3, 4, 5, 6, 7])
    x.shuffle()
    x.bet()
    x.bet_check()

    first = x.hit()
    x.remove()
    second = x.hit()
    x.remove()

    print(f"Your Cards: {first}, {second}")

    if first + second < 10:
        h = input("Do you want to hit?(Y/N) : ").upper()
        #Asking the player to hit
        if h == "Y":
            m = x.hit()
            print(m)
            x.remove()
            #If the total sum of received numbers is more than 10
            if first + second + m > 10:
                print("Win")
                x.aaaa(0)
                agan()

            else:
                print("Lose")

                if x.aaaa(1) == 2:
                    print("No more play")
                    print("Thank You")
                else:
                    agan()

        elif h == "N":
            print("Game end")
            x.aaaa(1)
            agan()
        else:
            print("Wrong Choice")
            table_play()
    else:
        print("Win")

        x.aaaa(0)
        agan()


def agan():
    # Playing again syntax
    agn = input("Do you want to play again?(Y/N) : ").upper()

    if agn == "Y":

        table_play()

    elif agn == "N":

        print("Thank You")

    else:

        print("Wrong choice")
        agan()

#Final Function Call
table_play()
