# Using the idea of induction.
# 24 - 29(24+5), 29 ~ 34(29+5) are all dividable via 5 & 7
def change(amount):
    if amount < 5:
        raise Exception

    if amount == 5:
        return [5]
    if amount == 7:
        return [7]
    if amount == 10:
        return [5, 5]
    if amount == 12:
        return [5, 7]
    if amount == 14:
        return [7, 7]
    if amount == 15:
        return [5, 5, 5]
    if amount == 17:
        return [5, 5, 7]
    if amount == 19:
        return [5, 7, 7]
    if amount == 20:
        return [5, 5, 5, 5]
    if amount == 21:
        return [7, 7, 7]
    if amount == 22:
        return [5, 5, 5, 7]
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]
    if amount == 29:
        return [5, 5, 5, 7, 7]

    coins = change(amount - 5)
    coins.append(5)
    return coins

for i in range(1, 1000):
    print(f"""start: {i}""")
    try:
        print(change(i))
    except Exception:
        print(f"""{i} was impossible""")
    
