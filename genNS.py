cards = "ABCDE98765432"
suits = "shdc"

def fix(x):
    if x == 'A':
        return 'T'
    if x == 'B':
        return 'J'
    if x == 'C':
        return 'Q'
    if x == 'D':
        return 'K'
    if x == 'E':
        return 'A'
    return x

def HCP(deck):
    cnt = 0
    for c in deck:
        if c[0] == 'E':
            cnt += 4
        if c[0] == 'D':
            cnt += 3
        if c[0] == 'C':
            cnt += 2
        if c[0] == 'B':
            cnt += 1
    return cnt

deck = []
for c in cards:
    for s in suits:
        deck.append(c+s)

import random, sys

print (int(sys.argv[1]))

for t in range(0, int(sys.argv[1])):

    if (t % 10) == 0:
        random.shuffle(deck)
        while ((HCP(deck[:13]) < 16) or (HCP(deck[26:39]) < 9)):
            random.shuffle(deck)
        
    d1 = deck[:13] + deck[26:39]
    d2 = deck[13:26] + deck[39:]
    random.shuffle(d2)
    deck = d1[:13] + d2[:13] + d1[13:] + d2[13:]

    p = [[], [], [], []]
    for i in range(0,4):
        for s in suits:
            ps = ''
            for j in range(13 * i, 13 * (i + 1)):
                if deck[j][1] == s:
                    ps += deck[j][0]
            ps = sorted(ps, reverse=True)
            p[i] += ps
            if s != "c":
                p[i] += ["."]

    for i in range(0, 4):
        if i == 0:
            sys.stdout.write('')
        else:
            sys.stdout.write(' ')
        for j in p[i]:
            sys.stdout.write(fix(j))
    sys.stdout.write("\n")