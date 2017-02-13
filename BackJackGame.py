from random import shuffle

class Card(object):
    def __init__(self,suit,size):
        self.suit = suit
        self.size = size

    def __str__(self):
        return '%s: %d' % (self.suit,self.size)

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

class Player(object):
    hand1 = []
    hand2 = []

    def __init__(self, name, total_money, current_bet):
        self.name = name
        self.total_money = total_money
        self.current_bet = current_bet

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

    def print_info(self):
        print 'Name: %s, Total money: %d, Current bet: %d, Hand 1: %s, Hand 2: %s' % (self.name, self.total_money, self.current_bet, str(self.hand1), str(self.hand2))

# A game starts here:
new_deck = Deck()
new_deck.shuffle_deck()

print 'Welcome to BlackJack Game! Please enter the number of players who want to play this game: '





