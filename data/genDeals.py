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

deck = []
for c in cards:
    for s in suits:
        deck.append(c+s)

import random, sys

print(int(sys.argv[1]))

for t in range(0, int(sys.argv[1])):

    random.shuffle(deck)

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