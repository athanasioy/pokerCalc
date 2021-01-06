import random
import itertools

#Create Deck
def createDeck():
    x = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    y = ['C','D','H','S']
    deck = []
    for suit in y:
        for num in x:
            deck.append(num+suit)
    return deck

deck = createDeck()
##print(deck, len(deck))

def stripSuit(card_list):
    list = []
    for i in card_list:
        list.append(i[:-1])
    return list

def stripNum(card_list):
    list = []
    for i in card_list:
        list.append(i[-1])
    return list

def getDups(list):
    """from a list of numbers, getDups returns
    a dictionary with the number as the key and
    the number of occurances as the number.
    Example: list = [1,1,5,6]. getDups(list) --> {1:2}"""
    seen_dict = {}
    dups = {}
    for x in list:
        if x not in seen_dict:
            seen_dict[x] = 1
        else:
            seen_dict[x] += 1
    for key in seen_dict:
        if seen_dict[key] > 1:
            dups[key] = seen_dict[key]
    return dups

def count_iterable(i):
    return sum(1 for e in i)

def removeCardsfromDeck(card_list,deck):
    cards = []
    for card in deck:
        if card in card_list:
            cards.append(card)
    for card in cards:
        deck.remove(card)
    return deck

#add poker logic


def isOnePair(myhand,table_cards):
    """myhand is a list of two elements.
    table_cards is the flop,turn or river and is also a list of 3-5 elemements
    e.g myhand = ['3C','4C'] """

    myhand = stripSuit(myhand)
    table_cards = stripSuit(table_cards)

    isOnePair = False
    if myhand[0] == myhand[1]:
        isOnePair = True
        return isOnePair
    if myhand[0] in table_cards or myhand[1] in table_cards:
        isOnePair = True
        return isOnePair
        #print("We have a Pair of {} {}".format(card[0],tablecard[0]))
    return isOnePair


def isTwoPair(myhand,table_cards):
    isTwoPair = False
    if myhand[0] in table_cards and myhand[1] in table_cards:
        isOnePair = True
        return isOnePair
                #print("We have a Pair of {} {}".format(card[0],tablecard[0]))
    return isTwoPair



#hand = ['10H','KS']
hand = random.sample(deck, k=2)
deck = removeCardsfromDeck(hand,deck)
#flop = ['KH','AD','QH']
flop = random.sample(deck,k = 3)
deck = removeCardsfromDeck(flop,deck)

def getProbability(myhand,table_cards):
    """my hand is a list of the player's hand. table_cards is as list
    containing either the flop,turn or river"""
    Occurances = 0
    for comb in itertools.combinations(deck,2):

        if isOnePair(myhand,table_cards+list(comb)):
            Occurances += 1
    total_combinations = count_iterable(itertools.combinations(deck,2))
    return Occurances/total_combinations


print(hand,flop,getProbability(hand,flop))
print(deck,len(deck))
