def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    i = 0
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Write your code here

        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice

        if currentHusband == None:
            womanSpouse[she] = he
            manSpouse[he] = she

            unmarriedMen.remove(he)
        elif herPreferences.index(he) > herPreferences.index(currentHusband):
            # he is rejected
            nextManChoice[he] += 1
        else:
            # currentHusband is rejected and replaced to he
            womanSpouse[she] = he
            manSpouse[he] = she

            manSpouse[currentHusband] = None
            nextManChoice[currentHusband] += 1

            unmarriedMen.remove(he)
            unmarriedMen.append(currentHusband)

    # Note that if you don't update the unmarriedMen list,
    # then this algorithm will run forever.
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse


# You might want to test your implementation on the following two tests:
assert (stableMatching(1, [[0]], [[0]]) == [0])

assert (stableMatching(2, [[0, 1], [0, 1]], [[0, 1], [0, 1]]) == [0, 1])
assert (stableMatching(2, [[0, 1], [1, 0]], [[0, 1], [0, 1]]) == [0, 1])
assert (stableMatching(2, [[1, 0], [0, 1]], [[0, 1], [0, 1]]) == [1, 0])
assert (stableMatching(2, [[1, 0], [1, 0]], [[0, 1], [0, 1]]) == [1, 0])

assert (stableMatching(2, [[0, 1], [0, 1]], [[0, 1], [1, 0]]) == [0, 1])
assert (stableMatching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]]) == [0, 1])
assert (stableMatching(2, [[1, 0], [0, 1]], [[0, 1], [1, 0]]) == [1, 0])
assert (stableMatching(2, [[1, 0], [1, 0]], [[0, 1], [1, 0]]) == [0, 1])

assert (stableMatching(2, [[0, 1], [0, 1]], [[1, 0], [0, 1]]) == [1, 0])
assert (stableMatching(2, [[0, 1], [1, 0]], [[1, 0], [0, 1]]) == [0, 1])
assert (stableMatching(2, [[1, 0], [0, 1]], [[1, 0], [0, 1]]) == [1, 0])
assert (stableMatching(2, [[1, 0], [1, 0]], [[1, 0], [0, 1]]) == [1, 0])

assert (stableMatching(2, [[0, 1], [0, 1]], [[1, 0], [1, 0]]) == [1, 0])
assert (stableMatching(2, [[0, 1], [1, 0]], [[1, 0], [1, 0]]) == [0, 1])
assert (stableMatching(2, [[1, 0], [0, 1]], [[1, 0], [1, 0]]) == [1, 0])
assert (stableMatching(2, [[1, 0], [1, 0]], [[1, 0], [1, 0]]) == [0, 1])

assert (stableMatching(3, [[0, 1, 2], [1, 0, 2], [2, 1, 0]], [[0, 1, 2], [1, 0, 2], [2, 1, 0]]) == [0, 1, 2])
assert (stableMatching(3, [[1, 0, 2], [0, 1, 2], [2, 1, 0]], [[1, 0, 2], [0, 1, 2], [2, 1, 0]]) == [1, 0, 2])
assert (stableMatching(3, [[2, 0, 1], [0, 1, 2], [1, 2, 0]], [[1, 0, 2], [2, 1, 0], [0, 1, 2]]) == [2, 0, 1])
assert (stableMatching(3, [[0, 2, 1], [2, 1, 0], [1, 2, 0]], [[0, 1, 2], [2, 1, 0], [1, 0, 2]]) == [0, 2, 1])
assert (stableMatching(3, [[1, 2, 0], [2, 1, 0], [0, 2, 1]], [[2, 1, 0], [0, 1, 2], [1, 0, 2]]) == [1, 2, 0])
assert (stableMatching(3, [[2, 1, 0], [1, 2, 0], [0, 2, 1]], [[2, 1, 0], [1, 0, 2], [0, 1, 2]]) == [2, 1, 0])

assert (stableMatching(4, [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]],
                       [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]) == [1, 2, 3, 0])
