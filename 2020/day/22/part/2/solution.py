import copy
from collections import deque

def recPlayToCompletion(decks, outcomes, game=1, debug=False):
    original_snapshot = repr(decks)
    if original_snapshot in outcomes.keys():
        dx, v = outcomes[original_snapshot]
        if debug:
            print("...and it's destiny that player {} should win.".format(v))
        decks = copy.deepcopy(dx)
        return v
    snapshots = set(original_snapshot)
    round = 1
    winner = None
    while decks[0] and decks[1]:
        if debug:
            print("-- Round {} (Game {}) --".format(round, game))
            print("Player 1's deck: {}".format(decks[0]))
            print("Player 2's deck: {}".format(decks[1]))
        snapshot = repr(decks)
        if snapshot in outcomes.keys():
            dx, v = outcomes[snapshot]
            if debug:
                print("...and it's destiny that player {} should win.".format(v))
            decks = copy.deepcopy(dx)
            return v

        # Rule #1
        if snapshot in snapshots:
            r = (copy.deepcopy(decks), 1)
            for sn in snapshots:
                outcomes[sn] = r
            return 1

        snapshots.add(snapshot)

        card1 = decks[0].popleft()
        card2 = decks[1].popleft()
        if debug:
            print("Player 1 plays: {}".format(card1))
            print("Player 2 plays: {}".format(card2))

        if card1 <= len(decks[0]) and card2 <= len(decks[1]):
            new_deck1 = deque([decks[0][i] for i in range(card1)])
            new_deck2 = deque([decks[1][i] for i in range(card2)])
            new_decks = (new_deck1, new_deck2)
            winner = recPlayToCompletion(new_decks, outcomes, game + 1, debug)
            if debug:
                print("...anyway, back to game {}.".format(game))
        elif card1 > card2:
            winner = 1
        elif  card2 > card1:
            winner = 2
        else:
            while true:
                Continue
        
        if winner == 1:
            if debug:
                print("Player 1 wins the round!")
            decks[0].append(card1)
            decks[0].append(card2)
            round += 1

        if winner == 2:
            if debug:
                print("Player 2 wins the round!")
            decks[1].append(card2)
            decks[1].append(card1)
            round += 1

    if decks[0]:
        r = (copy.deepcopy(decks), 1)
        for sn in snapshots:
            outcomes[sn] = r
        return 1
    else:
        r = (copy.deepcopy(decks), 2)
        for sn in snapshots:
            outcomes[sn] = r
        return 2

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

outcomes = dict() # maps repr(decks) -> resulting decks, victor
winner = recPlayToCompletion(decks, outcomes)
i = 1
sum = 0
winning = decks[0] if decks[0] else decks[1]
while winning:
    sum += i * (winning.pop())
    i += 1

print(repr(sum))
