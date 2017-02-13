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

    def __init__(self, name, total_money, current_bet=0):
        self.name = name
        self.total_money = total_money
        self.current_bet = current_bet

    def make_bet(self, bet):
        self.current_bet = bet

    def hit(self, deck = Deck()):
        if deck.is_empty():
            print 'The deck is empty.'
            return
        else:
            self.hand1.append(deck.deck_list.pop())

    def double_down(self, deck = Deck()):
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
    global player1
    global player2
    global player3

    print 'Welcome to BlackJack Game! There will be 3 players and 1 dealer in this game! Good Luck!\n'

    while True:
        try:
            input1 = int(raw_input('Player 1, please enter the total money you want to put in the game: '))
        except:
            print 'Try again - you must enter an integer which is > 0.'
            continue
        else:
            if input1 <= 0:
                print 'Try again - you must enter an integer which is > 0.'
                continue
            else:
                player1 = Player('Player 1', input1)
                while True:
                    try:
                        input2 = int(raw_input('Player 2, please enter the total money you want to put in the game: '))
                    except:
                        print 'Try again - you must enter an integer which is > 0.'
                        continue
                    else:
                        if input1 <= 0:
                            print 'Try again - you must enter an integer which is > 0.'
                            continue
                        else:
                            player2 = Player('Player 2', input2)
                            while True:
                                try:
                                    input3 = int(raw_input('Player 3, please enter the total money you want to put in the game: '))
                                except:
                                    print 'Try again - you must enter an integer which is > 0.'
                                    continue
                                else:
                                    if input1 <= 0:
                                        print 'Try again - you must enter an integer which is > 0.'
                                        continue
                                    else:
                                        player3 = Player('Player 3', input3)
                                        break
                            break
                break

# make bet
def make_bet():


# A game starts here:
new_deck = Deck()

new_deck.shuffle_deck()

introduction()




