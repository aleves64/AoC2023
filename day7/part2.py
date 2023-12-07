import os

with open("input", "r") as infile:
    myinput = infile.read()
myinput = myinput.split("\n")[:-1]

cards = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
    'J' : 1
}

def hand_key(hand):
    if 1 in hand:
        original = hand.copy()
        best_type = -18
        for swap in range(2,15):
            hand[hand.index(1)] = swap
            hand_type, hand = hand_key(hand)
            if hand_type > best_type:
                best_type = hand_type
            hand = original.copy()
        return best_type, hand
    counts = {n : [] for n in range(6)}
    ordered = sorted(hand)
    ordered.append(-1)
    prev = ordered[0]
    count = 0
    jokers = 0
    for card in ordered:
        if prev == card:
            count += 1
        else:
            counts[count].append(prev)
            count = 1
            prev = card
    five = len(counts[5])
    four = len(counts[4])
    pairs = len(counts[2])
    three = len(counts[3])
    two_pair = pairs // 2
    full_house = (pairs + three - two_pair) // 2
    high = ordered[-2]
    types = [five, four, full_house, three, two_pair, pairs, high]
    for j in range(len(types)):
        if types[j] > 0:
            return (-j, hand)
    return (None, hand)

types = []
bids = []
for line in myinput:
    hand, bid = line.split()
    hand = [cards[x] for x in hand]
    types.append(hand_key(hand))
    bid = int(bid)
    bids.append(bid)
rank_indices = sorted(range(len(bids)), key = lambda i: types[i])

total = 0
for i in range(len(rank_indices)):
    total += (i + 1) * bids[rank_indices[i]]
print(total)
