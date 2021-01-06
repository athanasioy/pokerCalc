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


print(getDuplicates(['J','J','5','5','J','A']))
# ['KC', '10D'] ['KD', '10S', 'KH', 'JC', '10C']
# ['JD', 'QH', 'KD', '10S', 'KH', 'JC', '10C']

print(sorted(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],key = ))
