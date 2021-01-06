
def HighestCard(l):
    """l is a list with cards. The func returns
    the highest valued card
    For example. l = ['2','5','10','K','A']: HighestCard(l) -> 14 ('A') """
    return max(FigstoNumsList(l))

def getDups(list):
    """from a list of numbers, getDups returns
    a dictionary with the number as the key and
    the number of occurances as the number.
    Example: list = [1,1,5,6,'Q','Q']. getDups(list) --> {'1':2,'Q':2}"""
    seen_l = []
    dups = []
    for x in list:
        if x[:-1] not in excludeSuitlist(seen_l):
            seen_l.append(x)
        else:
            dups.append(x)
    return dups


def findIndex(list):
    for i in range(len(list)):
        if list[i] == 3:
            return i
    return False

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

def toInt(l):
    list = [int(a) for a in l]
    return list

def stripSuit(l):
    list = [x[:-1] for x in l]
    return list

def stripNum(card_list):
    list = [i[-1] for i in l]
    return list

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

def FigstoNumsList(l):
    return [FigstoNums(x) for x in l]


def ConvertBacktoFigs(x):
    if x == 14:
        return 'A'
    if x == 13:
        return 'K'
    if x == 12:
        return 'Q'
    if x == 11:
        return 'J'
    return str(x)

# def isConsecutive(list):
#     """Checks if the list contains 5 consecutive numbers
#     For example: [2,5,4,3,8,10,6] --> True because of 2,3,4,5,6"""
#     list = sorted(list)
#     subs = [list[i:i+5] for i in range(len(list)) if len(list[i:i+5]) == 5]
#     print(subs, range(min(list), max(list)+1))
#     for sub in subs:
#         print(sorted(sub))
#     return any([(set(sorted(sub)).issubset(set(range(min(list), max(list)+1)))) for sub in subs])
#
#
#
#
# def check(n, l):
#     subs = [l[i:i+n] for i in range(len(l)) if len(l[i:i+n]) == n]
#     print(subs)
#     for sub in subs:
#         print(sorted(sub))
#     return any([(sorted(sub) in range(min(l), max(l)+1)) for sub in subs])

# print(isConsecutive([2,5,4,3,8,10,6]))
# print(isConsecutive([1,1,1,1,1,1,10]))

# def isConsecutivewNew(l):
#     l = sorted(l)
#     subs = [l[i:i+5] for i in range(len(l)) if len(l[i:i+5]) == 5]
#     # for sub in subs:
#     #     print(sub)
#     #     print(list(range(min(sub),max(sub)+1)))
#     #     print(sub == list(range(min(sub),max(sub)+1)))
#
#     return any([sub == list(range(min(sub),max(sub)+1)) for sub in subs])


# isConsecutivewNew([4,6,8,5,10,7,12,111])




def isConsecutive(l):
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


def OnlyDuplicated(l):
    """ [1,1,2,2,3,4] --> [1,1,2,2]"""
    def isDuplicate(x,l):
        """Checks if the value "x" in list "l" is seen more than once"""
        FirstOccurance = l.index(x)
        return x in l[(FirstOccurance+1):]

    DupsOnly = [x for x in l if isDuplicate(x[:-1],excludeSuitlist(l))]
    return DupsOnly

def straightPreProcess(hand):
    hand = stripSuit(hand)
    hand = FigstoNums(hand)
    hand = toInt(hand)
    return hand

def excludeSuitlist(l):
    return [x[:-1] for x in l]


def findKicker(l):
    """findKicker returns the highest Card after the pairs (one-pairs or two pairs)
    are removed!"""
    Pairs = OnlyDuplicated(l)
    for crd in BestFIve:
        l.remove(crd)
    #Search for the next highest Card!
    nextHighestCard = [x for x in l if x[:-1] == ConvertBacktoFigs(HighestCard(stripSuit(l)))] # A bit Complex!
    return nextHighestCard[0]

def findBestFive(l):
    """Pass a list of 7 and return find the best 5 Cards"""
    BestFIve = OnlyDuplicated(l)
    for crd in BestFIve:
        l.remove(crd)
    remaining_cards = 5 - len(BestFIve)
    for i in range(remaining_cards):
        # print( HighestCard(stripSuit(l)))
        nextHighestCard = [x for x in l if x[:-1] == ConvertBacktoFigs(HighestCard(stripSuit(l)))]
        # print(nextHighestCard,l)
        BestFIve.append(nextHighestCard[0])
        # print(l,nextHighestCard)
        l.remove(nextHighestCard[0])
    return BestFIve
# straightwithSuits = [value for value in table_cards+myhand if int(FigstoNums(value[:-1]))  in candidate_straght ]


def FindOnePair(myhand,table_cards):
    l = myhand+table_cards
    dups = getDups(l)
    print(dups)

# HighestCard(['KD','KD','2D','QD','9H']+ ['KH','AH'])
# FindOnePair(['KH','AH'],['KC','KD','2D','QD','9H'])
print(findBestFive(['KD','KD','2D','7D','9H']+ ['3H','AH']))
