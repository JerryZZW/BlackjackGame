from random import shuffle

# Card
class Card(object):
    def __init__(self, suit, size):
        self.suit = suit
        self.size = size

    def __str__(self):
        if self.size == 1:
            return '%s: %s' % (self.suit, 'A')
        elif self.size == 11:
            return '%s: %s' % (self.suit, 'J')
        elif self.size == 12:
            return '%s: %s' % (self.suit, 'Q')
        elif self.size == 13:
            return '%s: %s' % (self.suit, 'K')
        else:
            return '%s: %d' % (self.suit, self.size)

# Deck
class Deck(object):
    def __init__(self):
        self.deck_list = []

        for i in xrange(1, 14):
            self.deck_list.append(Card('Clubs', i))
            self.deck_list.append(Card('Diamonds', i))
            self.deck_list.append(Card('Hearts', i))
            self.deck_list.append(Card('Spades', i))

    def shuffle_deck(self):
        shuffle(self.deck_list)

    def is_empty(self):
        return len(self.deck_list) == 0

    def reset(self):
        self.deck_list = []

        for i in xrange(1, 14):
            self.deck_list.append(Card('Clubs', i))
            self.deck_list.append(Card('Diamonds', i))
            self.deck_list.append(Card('Hearts', i))
            self.deck_list.append(Card('Spades', i))

# Player
class Player(object):
    def __init__(self, name):
        self.name = name
        self.total_money = 0
        self.current_bet = 0
        self.status = 0
        self.hand1 = []
        self.hand2 = []

    def hit(self, deck):
        if deck.is_empty():
            print 'The deck is empty.'
            return
        else:
            self.hand1.append(deck.deck_list.pop())

    def double_down(self, deck):
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

    def surrender(self):
        self.current_bet *= 0.5

    def insurance(self):
        if self.total_money < self.current_bet*0.5:
            print "Fail. You don't have enough money to buy an insurance."
        else:
            self.total_money -= self.current_bet*0.5
            print 'Succeed. Your total money has been subtracted by half your current bet.'

    def reset(self):
        self.total_money = 0
        self.current_bet = 0
        self.status = 0
        self.hand1 = []
        self.hand2 = []

    def __str__(self):
        return 'Name: %s, Total money: %d, Current bet: %d, Hand 1: %s, Hand 2: %s' % (
            self.name, self.total_money, self.current_bet, [str(x) for x in self.hand1], [str(x) for x in self.hand2])

# Introduction
def introduction():
    print ''
    print 'Welcome to BlackJack Game!'
    print 'There will be 3 players and 1 dealer in this game.'
    print 'Wins are paid out at 1:1 ratio.'
    print 'Good luck!\n'

# Check and input player's total money
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
                player.total_money = user_input
                break

# Check and input player's current bet
def input_current_bet(player):
    while True:
        try:
            user_input = int(raw_input('%s, please enter the bet you want to put in this round: ' % player.name))
        except:
            print 'Try again - you must enter an integer which is > 0 and <= your total money'
            continue
        else:
            if user_input <= 0 or user_input > player.total_money:
                print 'Try again - you must enter an integer which is > 0 and <= your total money'
                continue
            else:
                player.current_bet = user_input
                player.total_money -= user_input
                break

# Check "yes" and "no" input from user
def check_yes_no(player):
    while True:
        user_input = raw_input('%s, please enter y or n to make your decision: ' % player.name)
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print 'Try again - you must enter either y or n: '
            continue

# Check Black Jack
def check_blackjack(player):
    if (player.hand1[0].size == 1 and player.hand1[1].size == 10) or (player.hand1[0].size == 10 and player.hand1[1].size == 1):
        print '%s has the Black Jack!!!' % player.name
    elif dealer[0].size == 1 and dealer[1].size == 10:
        print 'Dealer has the Black Jack!!!'
    elif dealer[1].size == 1:
        print 'Dealer has an A, does the player want to buy insurance for this round? ', "(y for 'yes', n for 'no)'"
        if check_yes_no(player) == 'y':
            player.insurance()
            if dealer[0] == 10:
                print "Dealer's hold card is 10."
                player.current_bet *= 2
                print "%s's current bet has been doubled!" % player.name
            else:
                print 'Dealer has no Black Jack. Game continues.'

    if (player.hand1[0].size == 1 and player.hand1[1].size == 10) or (player.hand1[0].size == 10 and player.hand1[1].size == 1):
        if (dealer[0].size == 1 and dealer[1].size == 10) or (dealer[0].size == 10 and dealer[1].size == 1):
            print 'Dealer also has the Black Jack!!!'
            print '%s keeps the current bet.' % player.name
        else:
            player.current_bet *= 2
            print 'Dealer has no Black Jack.'
            print "%s's current bet has been doubled!" % player.name

    if (dealer[0].size == 1 and dealer[1].size == 10) or (dealer[0].size == 10 and dealer[1].size == 1):
        if (player.hand1[0].size == 1 and player.hand1[1].size == 10) or (player.hand1[0].size == 10 and player.hand1[1].size == 1):
            print '%s also has the Black Jack!' % player.name
            print '%s keeps the current bet.' % player.name
        else:
            player.current_bet = 0
            print "Dealer wins %s's current bet!!!" % player.name

    if (dealer[0].size != 1 and dealer[1].size != 10) or (dealer[0].size != 10 and dealer[1].size != 1
    ) or (player.hand1[0].size != 1 and player.hand1[1].size != 10) or (player.hand1[0].size != 10 and player.hand1[1].size != 1):
        print 'Neither Dealer or %s has the Black Jack.' % player.name

# check and input player's choice (i.e. hit, stand, and etc.)
def input_player_choice(player):
    while True:
        user_input = raw_input('%s, please enter a choice: hit, stand, double, split, or surrender: ' % player.name)
        if user_input == 'hit':
            print '%s chooses to hit.' % player.name
            player.hit(new_deck)
            break
        elif user_input == 'stand':
            player.status = 1
            break
        elif user_input == 'double':
            print '%s chooses to double down.' % player.name
            player.double_down(new_deck)
            player.status = 1
            break
        elif user_input == 'split':
            print '%s chooses to split the cards.' % player.name
            player.split()
            break
        elif user_input == 'surrender':
            print '%s chooses to surrender.' % player.name
            player.surrender()
            player.status = 1
            break
        else:
            print "Try again - you must enter 'hit', 'stand', 'double', 'split', or 'surrender'. "
            continue

# check bust
def check_bust(player):
    count_hand1 = 0
    count_hand2 = 0

    for x in player.hand1:
        count_hand1 += x.size

    for x in player.hand2:
        count_hand2 += x.size

    if count_hand1 > 21 or count_hand1 >21:
        print "%s bust !!! Dealer wins %s's bet." % player.name
        player.current_bet = 0
        return True
    else:
        return False

# Check players' hands
def check_hands(player):
    while True:
        print ''
        input_player_choice(player)
        if check_bust(player) == True:
            break
        elif player.status == 1:
            break
        else:
            continue

# Check hands's size
def check_hands_size(hands):
    count = 0

    for x in hands:
        count += x.size

    return count

# Compare the size with the dealer
def compare_size(player):
    if check_hands_size(dealer) > check_hands_size(player.hand1) or check_hands_size(dealer) > check_hands_size(player.hand2):
        print 'Dealer has larger size. %s loses the current bet.' % player.name
        player.current_bet = 0
    elif check_hands_size(dealer) == check_hands_size(player.hand1) or check_hands_size(dealer) == check_hands_size(player.hand2):
        print 'Dealer and %s have the same size. %s keeps the current bet' % player.name
    else:
        print "Dealer has smaller size. %s's current bet doubles." % player.name
        player.current_bet *= 2

# check if players want to play one more round
def check_one_more_round():
    while True:
        user_input = raw_input('Please enter y or n to make your decision: ')
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print 'Try again - you must enter either y or n: '
            continue

# Deal cards
def deal_cards():
    while True:
        print ''
        input_current_bet(player1)
        input_current_bet(player2)
        input_current_bet(player3)
        print ''

        player1.hand1.append(new_deck.deck_list.pop())
        player1.hand1.append(new_deck.deck_list.pop())
        player2.hand1.append(new_deck.deck_list.pop())
        player2.hand1.append(new_deck.deck_list.pop())
        player3.hand1.append(new_deck.deck_list.pop())
        player3.hand1.append(new_deck.deck_list.pop())
        dealer.append(new_deck.deck_list.pop())
        dealer.append(new_deck.deck_list.pop())

        print 'Player 1 deals two cards: ', player1.hand1[0], ', ', player1.hand1[1]
        print 'Player 2 deals two cards: ', player2.hand1[0], ', ', player2.hand1[1]
        print 'Player 3 deals two cards: ', player3.hand1[0], ', ', player3.hand1[1]
        print 'Dealer deals two cards: (hold card), ', dealer[1]

        print ''
        check_blackjack(player1)
        check_blackjack(player2)
        check_blackjack(player3)

        check_hands(player1)
        check_hands(player2)
        check_hands(player3)

        print ''
        print "Dealer's hand: %s" % [str(x) for x in dealer]
        while True:
            if check_hands_size(dealer) < 17:
                dealer.append(new_deck.deck_list.pop())
                continue
            elif check_hands_size(dealer) > 21:
                print "Dealer busts. All players's current bet doubles!!!"
                player1.current_bet *= 2
                player2.current_bet *= 2
                player3.current_bet *= 2
                break
            else:
                compare_size(player1)
                compare_size(player2)
                compare_size(player3)
                break

        print ''
        print 'Game over.'
        print player1
        print player2
        print player3
        print ''
        print 'One more round ????'
        if check_one_more_round() == 'y':
            new_deck.reset()
            new_deck.shuffle_deck()
            player1.reset()
            player2.reset()
            player3.reset()
            continue
        else:
            print 'Thank you for playing. See you next time!!!'
            break

# A game starts here:
player1 = Player('Player 1')
player2 = Player('Player 2')
player3 = Player('Player 3')
dealer = []

new_deck = Deck()

new_deck.shuffle_deck()

introduction()

input_total_money(player1)
input_total_money(player2)
input_total_money(player3)

deal_cards()