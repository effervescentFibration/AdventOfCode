from collections import deque

def playToCompletion(decks, debug=False):
    round = 1
    while decks[0] and decks[1]:
        if debug:
            print("-- Round {} --".format(round))
            print("Player 1's deck: {}".format(decks[0]))
            print("Player 2's deck: {}".format(decks[1]))
        card1 = decks[0].popleft()
        card2 = decks[1].popleft()
        if debug:
            print("Player 1 plays: {}".format(card1))
            print("Player 2 plays: {}".format(card2))
        
        if card1 > card2:
            if debug:
                print("Player 1 wins the round!")
            decks[0].append(card1)
            decks[0].append(card2)

        if  card2 > card1:
            if debug:
                print("Player 2 wins the round!")
            decks[1].append(card2)
            decks[1].append(card1)            

    return decks

player = 1
decks = [deque(), deque()]

with open('input') as file:
    for l in file:
        if l == "\n":
            continue
        if l == "Player 1:\n":
            player = 1
            continue
        if l == "Player 2:\n":
            player = 2
            continue
        decks[player - 1].append(int(l[:-1]))

playToCompletion(decks)
i = 1
sum = 0
winning = decks[0] if decks[0] else decks[1]
while winning:
    sum += i * (winning.pop())
    i += 1

print(repr(sum))
