from random import shuffle

# Card
class Card(object):
    def __init__(self,suit,size):
        self.suit = suit
        self.size = size

    def __str__(self):
        return '%s: %d' % (self.suit,self.size)

# Deck
class Deck(object):
    deck_list = []

    def __init__(self):
        for i in xrange(1,14):
            self.deck_list.append(Card('Clubs', i))
            self.deck_list.append(Card('Diamonds', i))
            self.deck_list.append(Card('Hearts', i))
            self.deck_list.append(Card('Spades', i))

    def shuffle_deck(self):
        shuffle(self.deck_list)

    def is_empty(self):
        return len(self.deck_list) == 0

# Player
class Player(object):
    hand1 = []
    hand2 = []

    def __init__(self, name, total_money=0, current_bet=0):
        self.name = name
        self.total_money = total_money
        self.current_bet = current_bet

    def set_total_money(self,money):
        self.total_money = money

    def make_bet(self, bet):
        self.current_bet = bet

    def hit(self, deck=Deck()):
        if deck.is_empty():
            print 'The deck is empty.'
            return
        else:
            self.hand1.append(deck.deck_list.pop())

    def double_down(self, deck=Deck()):
        if deck.is_empty():
            print 'The deck is empty.'
            return
        else:
            if self.total_money < self.current_bet:
                print "You don't have enough money to double down."
                return
            else:
                self.hand1.append(deck.deck_list.pop())
                self.total_money -= self.current_bet
                self.current_bet *= 2

    def split(self):
        if self.hand1[0] != self.hand1[1]:
            print 'You can not split the cards.'
            return
        else:
            self.hand2.append(self.hand1.pop())

    def __str__(self):
        return 'Name: %s, Total money: %d, Current bet: %d, Hand 1: %s, Hand 2: %s' % (self.name, self.total_money, self.current_bet, str(self.hand1), str(self.hand2))

# Introduction
def introduction():
    print 'Welcome to BlackJack Game!'
    print 'There will be 3 players and 1 dealer in this game.'
    print 'Wins are paid out at 1:1 ratio.'
    print 'Good luck!\n'

# check money input
def input_total_money(player):
    while True:
        try:
            user_input = int(raw_input('%s, please enter the total money you want to put in the game: ' % player.name))
        except:
            print 'Try again - you must enter an integer which is > 0.'
            continue
        else:
            if user_input <= 0:
                print 'Try again - you must enter an integer which is > 0.'
                continue
            else:
                player.set_total_money(user_input)
                break

# A game starts here:
player1 = Player('Player 1')
player2 = Player('Player 2')
player3 = Player('Player 3')

new_deck = Deck()

new_deck.shuffle_deck()

introduction()

input_total_money(player1)
input_total_money(player2)
input_total_money(player3)

