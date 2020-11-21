def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins += 1
            elif i < j:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    for i, dice in enumerate(dices):
        opponents = filter(lambda x: x != dice, dices)

        dice_is_best = True
        for o in opponents:
            res = count_wins(dice, o)
            if res[0] <= res[1]:
                dice_is_best = False
                break

        if dice_is_best:
            return i

    return -1


def find_winning_dice_index(opponent_dice_index, dices):
    opponent_dice = dices[opponent_dice_index]

    for i, our_dice in enumerate(dices):
        if i == opponent_dice_index:
            continue

        res = count_wins(our_dice, opponent_dice)
        if res[0] > res[1]:
            return i

    raise Exception('Should not reach here')


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()

    best_dice_index = find_the_best_dice(dices)
    if best_dice_index != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = best_dice_index
        return strategy

    strategy["choose_first"] = False
    for i in range(len(dices)):
        strategy[i] = find_winning_dice_index(i, dices)

    return strategy


# input = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
input = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]

print(compute_strategy(input))
