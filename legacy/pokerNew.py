import itertools


#Create Deck
def createDeck():
    x = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    y = ['C','D','S','H']
    deck = []
    for suit in y:
        for num in x:
            deck.append(num+suit)
    return deck

deck = createDeck()

# if 1 -> 0, and if 0 -> 1. To reserver we multiply by (-1) and add 1

# Helper Functions

def HighestCard(l):
    """l is a list with cards. The func returns
    the highest valued card
    For example. l = ['2','5','10','K','A']: HighestCard(l) -> 14 ('A') """
    return max(FigstoNumsList(l))

def allEqual(l):
    return all([l[0]== ele for ele in l])

def straightPreProcess(hand):
    hand = stripSuit(hand)
    hand = FigstoNumsList(hand)
    hand = toInt(hand)
    return hand

def FigstoNums(x):
    """returns a list that converts figures to nums
    For Example: ['1','4','K','J'] -> ['1','4','13','11']"""
    if x == 'J':
        x = 11
        return x
    elif x == 'Q':
        x = 12
        return x
    elif x == 'K':
        x = 13
        return x
    elif x == 'A':
        x = 14
        return x
    else:
        return int(x)

def ConvertBacktoFigs(x):
    """Coverts numbers to Figures"""
    if x == 14:
        return 'A'
    if x == 13:
        return 'K'
    if x == 12:
        return 'Q'
    if x == 11:
        return 'J'
    return str(x)


def FigstoNumsList(l):
    return [FigstoNums(x) for x in l]



def toInt(list):
    list = [int(a) for a in list]
    return list


def findIndex(list, target):
    """Returns the index which first satisfies the condition:
    list[index] == target . The func is used in the isFullHouse Func, in
    order to find the strength of the FullHouse"""
    for i in range(len(list)):
        if list[i] == target:
            return i
    return False

def stripSuit(card_list):
    list = [x[:-1] for x in card_list]
    return list

def stripNum(card_list):
    list = [i[-1] for i in card_list]
    return list




def isConsecutive(l): #THIS FUNC IS NOT USED!
    """Returns True if a list contains 5 consecutive numbers, the order notwithstanding
    For Example: [2,3,5,7,100,6,4] -> True because 2,3,4,5,6 are consecutive
    #2 Example: [2,4,5,6,9,10,7] -> False because 3 is missing from 2,3,4,5,6
    This Function is used to determine is there is a Straight on the table"""
    l = list(set(l))
    l = sorted(l)
    if len(l)<5:
        return False
    subs = [l[i:i+5] for i in range(len(l)) if len(l[i:i+5]) == 5]
    return any([sub == list(range(min(sub),max(sub)+1)) for sub in subs])

def getDups(list):
    """from a list of numbers, getDups returns
    a dictionary with the number as the key and
    the number of occurances as the number.
    Example: list = [1,1,5,6,'Q','Q']. getDups(list) --> {'1':2,'Q':2}"""
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

def getDuplicates(l):
    """['1','J','5','5','J','A'] -> ['J','5']
       ['J','J','5','5','J','A'] -> ['J','J','5']"""
    seen = []
    dups = []
    for x in l:
        if x not in seen:
            seen.append(x)
        else:
            dups.append(x)

    return dups

def count_iterable(i):
    """this func is used to count the number of total possible combinations.
    The func is used to calculate probabilities"""
    return sum(1 for e in i)

def removeCardsfromDeck(card_list,deck):
    d = deck.copy()
    cards = []
    for card in d:
        if card in card_list:
            cards.append(card)
    for card in cards:
        d.remove(card)
    return d


def FindStraight(l):
    l = list(set(l))
    l = sorted(l)
    if len(l)<5:
        return False
    subs = [l[i:i+5] for i in range(len(l)) if len(l[i:i+5]) == 5]
    for sub in subs:
        if sub == list(range(min(sub),max(sub)+1)):
            return sub
    return False

def findFlush(l):
    """ List is the table and hand cards.
    Finds and returns the flush if there is One
    ['2H','5H','JC','KH','2S','8H','7H'] -> ['2H','5H','KH',7H','8H']"""
    dups = getDups(stripNum(l))
    for occurs,suit in zip(dups.values(),dups.keys()):
        if occurs>=5:
            return [x for x in l if x[-1] == suit]

def findKicker(l):
    def OnlyDuplicated(l):
        """ ['2C','2D','2H','5H','5C','10S'] --> ['2C','2D','2H','5H','5C']"""
        def isDuplicate(x,l):
            """Checks if the value "x" in list "l" is seen more than once"""
            FirstOccurance = l.index(x)
            return x in l[(FirstOccurance+1):]
        DupsOnly = [x for x in l if isDuplicate(x[:-1],stripSuit(l))]
        return DupsOnly
    """findKicker returns the highest Card after the pairs (one-pairs or two pairs)
    are removed!"""
    Pairs = OnlyDuplicated(l)
    print("list is {}".format(l))
    # print(Pairs)
    for crd in Pairs:
        l.remove(crd)
    # print(l)
    #Search for the next highest Card!

    nextHighestCard = [x for x in l if x[:-1] == ConvertBacktoFigs(HighestCard(stripSuit(l)))] # A bit Complex!
    print("next HighestCard is {}".format(nextHighestCard))
    # print("next HighestCard{}".format(nextHighestCard))
    return nextHighestCard[0]

#Poker logic

def noPair(my_hand,table_cards):
    # print(my_hand,table_cards)
    # myhand = stripSuit(myhand)
    # table_cards = stripSuit(table_cards)
    dups = getDups(stripSuit(my_hand) + stripSuit(table_cards))
    cards = list(dups.keys())
    occurs = list(dups.values())
    if len(cards) == 0:
        return FigstoNums(findKicker(my_hand+table_cards)[:-1])


def isOnePair(myhand,table_cards):
    """myhand is a list of two elements.
    table_cards is the flop,turn or river and is also a list of 3-5 elemements
    e.g myhand = ['3C','4C']. This Func returns the strenght of the hand, based
    on my arbitrary number system, or 0 if my_hand+table_cards does not contain OnePair"""

    # myhand = stripSuit(myhand)
    # table_cards = stripSuit(table_cards)
    dups = getDups(stripSuit(myhand) + stripSuit(table_cards))
    cards = list(dups.keys())
    occurs = list(dups.values())
    # print(cards,occurs)
    if len(cards) == 1 and occurs[0] == 2 and not isFlush(myhand,table_cards) and not isStraight(myhand,table_cards):
        # print("We have one pair of {}{}".format(cards[0],cards[0]))
        # print(findKicker(myhand+table_cards))
        return 100 +FigstoNums(cards[0]) + FigstoNums(findKicker(myhand+table_cards)[:-1])
    else:
        return 0

def isTwoPair(myhand,table_cards):
    # myhand = stripSuit(myhand)
    # table_cards = stripSuit(table_cards)
    dups = getDups(stripSuit(myhand) + stripSuit(table_cards))
    cards = list(dups.keys())
    occurs = list(dups.values())
    if len(cards) >=2 and not any([x=>3 for x in occurs ]):
        # print("We have two pair of {} {}, {} {}".format(cards[0],cards[0],cards[1],cards[1]))
        cards.sort()
        return 200 + FigstoNums(cards[0]) + FigstoNums(cards[1])/100 + FigstoNums(findKicker(myhand+table_cards)[:-1])
    else:
        return 0

def isThreeOfaKind(myhand,table_cards):
    # myhand = stripSuit(myhand)
    # table_cards = stripSuit(table_cards)
    dups = getDups(stripSuit(myhand) + stripSuit(table_cards))
    cards = list(dups.keys())
    occurs = list(dups.values())
    if len(cards) == 1 and sum(occurs) ==3:
        # print("We have three of a kind of {} {} {}".format(cards[0],cards[0],cards[0]))
        # print(myhand,table_cards)
        return 300 + FigstoNums(cards[0]) + FigstoNums(findKicker(myhand+table_cards)[:-1])
    else:
        return 0
def isFourOfaKInd(myhand,table_cards):
    isFourOfaKInd = False
    myhand = stripSuit(myhand)
    table_cards = stripSuit(table_cards)
    dups = getDups(myhand + table_cards)
    cards = list(dups.keys())
    occurs = list(dups.values())
    if len(cards) == 1 and sum(occurs) ==4:
        # print("We have Four of a kind of {} {} {} {}".format(cards[0],cards[0],cards[0],cards[0]))
        # print(myhand,table_cards)
        isFourOfaKInd = True
        return 800 + FigstoNums(cards[0])
    else:
        return 0

def isFullHouse(myhand,table_cards):
    myhand = stripSuit(myhand)
    table_cards = stripSuit(table_cards)
    dups = getDups(myhand + table_cards)
    cards = list(dups.keys())
    occurs = list(dups.values())
    if len(cards) => 2 and sum(occurs) > 5 and any([x>2 for x in occurs]):
        FullHouseIndex = findIndex(occurs,3)
        reverseIndex = (-1)*FullHouseIndex +1
        # print("We have full house {} {} {} {} {}".format(cards[FullHouseIndex],cards[FullHouseIndex],cards[FullHouseIndex],cards[reverseIndex],cards[reverseIndex]))
        # print(myhand,table_cards)
        return 700 + FigstoNums(cards[FullHouseIndex]) + FigstoNums(cards[reverseIndex])
    else:
        return 0

def isStraight(myhand,table_cards):

    myhand = stripSuit(myhand)
    table_cards = stripSuit(table_cards)
    myhand = FigstoNumsList(myhand) #Converts 'J' to 11, 'Q' for 12 for straight purposes
    table_cards = FigstoNumsList(table_cards)
    # myhand = toInt(myhand)
    # table_cards = toInt(table_cards)

    # print(myhand,table_cards)
    # print(isConsecutive(myhand+table_cards))
    if FindStraight(myhand+table_cards):
        straight = FindStraight(myhand+table_cards)
        return 500 + straight[-1]
    return 0

def isFlush(myhand,table_cards):
    # myhand, table_cards = stripNum(myhand) , stripNum(table_cards)
    dups = getDups(stripNum(myhand) + stripNum(table_cards))
    suits = list(dups.keys())
    occurs = list(dups.values())
    # print(occurs,suits)
    if findFlush(myhand + table_cards):
        Flush = findFlush(myhand + table_cards)
        # FlushIndex = findIndex(occurs,5)
        # print("We have a flush on {}".format(suits[FlushIndex]))
        # print(myhand+table_cards)
        return 600 + HighestCard(stripSuit(Flush))
    return False


def isStraightFlush(myhand,table_cards):
    candidate_straght = FindStraight(straightPreProcess(myhand) +straightPreProcess(table_cards))
    if candidate_straght:
        straightwithSuits = [value for value in table_cards+myhand if int(FigstoNums(value[:-1]))  in candidate_straght ]
        # for value in table_cards+myhand:
        #     if int(FigstoNums(value[:-1]))  in candidate_straght:
        #         if not Suit:
        #             Suit = value[-1]
        # print(stripNum(straightwithSuits))
        if allEqual(stripNum(straightwithSuits)):
            return 900 + HighestCard(stripSuit(straightwithSuits))
    return False

#Get probability Function given the player's hand and the table cards
def getProbability(myhand,table_cards,logic_func,deck):
    """my hand is a list of the player's hand. table_cards is as list
    containing either the flop,turn or river"""
    cards_left = 5 - len(table_cards)
    Occurances = 0
    for comb in itertools.combinations(deck,cards_left):
        # print(comb)
        if logic_func(myhand,table_cards+list(comb)):
            Occurances += 1
    total_combinations = count_iterable(itertools.combinations(deck,cards_left))
    Prob = Occurances/total_combinations
    # print(Prob)
    return round(Prob,3)


def strengthOfHand(hand,tableCards):

    if isStraightFlush(hand,tableCards):
        return  isStraightFlush(hand,tableCards)
    if isFourOfaKInd(hand,tableCards):
        return isFourOfaKInd(hand,tableCards)
    if isFullHouse(hand,tableCards):
        return isFullHouse(hand,tableCards)
    if isFlush(hand,tableCards):
        return isFlush(hand,tableCards)
    if isStraight(hand,tableCards):
        return isStraight(hand,tableCards)
    if isThreeOfaKind(hand,tableCards):
        return isThreeOfaKind(hand,tableCards)
    if isTwoPair(hand,tableCards):
        return isTwoPair(hand,tableCards)
    if isOnePair(hand,tableCards):
        return isOnePair(hand,tableCards)
    if noPair(hand,tableCards):
        return noPair(hand,tableCards)
    print("We have a bug at {} {}".format(hand,tableCards))

def isWinning(l1,l2,tableCards):
    """This func gets two lists of lenght 7 and returns true if
    l1 hand wins l2"""
    return strengthOfHand(l1,tableCards) > strengthOfHand(l2,tableCards)


def getStrongestHandProbability(myhand,tableCards):
    Win = 0
    sumOfHands = 0
    for comb in itertools.combinations(removeCardsfromDeck(myhand+tableCards,deck),2):
        cards_left = 5 - len(tableCards)
        # removeCardsfromDeck(comb,deck)

        for tcCombs in itertools.combinations(removeCardsfromDeck(myhand+tableCards+list(comb),deck),cards_left):
            # print(type(list(tcCombs)))
            # print("My hand is {}".format(myhand),"opposite hand {}".format(comb),"table cards {}".format(list(tcCombs)+tableCards))
            if isWinning(myhand,list(comb),list(tcCombs)+tableCards):
                Win += 1
            sumOfHands += 1
    winProbability = round(win/sumofHands,3)
    return winProbability

hand = ['JD','QH']
# # hand = random.sample(deck, k=2)
# deck = removeCardsfromDeck(hand,deck)
flop = ['KH','JC','10C']
# # flop = random.sample(deck,k = 3)
# deck = removeCardsfromDeck(flop,deck)

# print(HighestCard(['2','5','10','K','A']))
# # print("The flop is {} and our hand is {}".format(flop,hand))
# print("the kicker is {}".format(findKicker(hand+flop)))
# print(isOnePair(flop,hand))
# print(hand,flop,getProbability(hand,flop,isOnePair))
# print(OnlyDuplicated(['JD','QH']+['KH','JH','10C']))

print(sorted(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],key =FigstoNums ))
# print(getStrongestHandProbability(hand,flop))
# print(findKicker(['JD','QH'] + ['QC','JC','10C',]))
def GetProbabilities(hand,flop):
    FUNCTIONS = [isStraightFlush,isFourOfaKInd,isFullHouse,isFlush,isStraight,isThreeOfaKind,isTwoPair,isOnePair,noPair]
    print("Probability for No-Pair {}%".format(round(getProbability(hand,flop,noPair),2)))
    print("Probability for OnePair {}%".format(round(getProbability(hand,flop,isOnePair),2)))
    print("Probability for Two-Pair {}%".format(round(getProbability(hand,flop,isTwoPair),2)))
    print("Probability for ThreeOfaKind {}%".format(round(getProbability(hand,flop,isThreeOfaKind),2)))
    print("Probability for Straight {}%".format(round(getProbability(hand,flop,isStraight),2)))
    print("Probability for Flush {}%".format(round(getProbability(hand,flop,isFlush),2)))
    print("Probability for FullHouse {}%".format(round(getProbability(hand,flop,isFullHouse),2)))
    print("Probability for isFourOfaKInd {}%".format(round(getProbability(hand,flop,isFourOfaKInd),2)))
    print("Probability for isStraightFlush {}%".format(round(getProbability(hand,flop,isStraightFlush),2)))

    ProbSum = 0
    for func in FUNCTIONS:
        ProbSum += getProbability(hand,flop,func)
    print("Sum of Probabilities {}".format(ProbSum))


# GetProbabilities(hand,flop)
