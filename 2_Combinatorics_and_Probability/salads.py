import itertools as it

s = set()
for c in it.product('ABC', repeat=4):
  l = sorted(list(c))
  s.add("".join(l))

print(len(s))

### Example Answer
#
# from itertools import combinations_with_replacement
# for c in combinations_with_replacement("TBL", 4):
#     print("".join(c))
