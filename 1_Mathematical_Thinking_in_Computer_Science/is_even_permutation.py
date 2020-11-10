# a = [0, 1]
# a = [1, 0]
# a = [1, 2, 0]
# a = [2,5,1,3]
# a = [1,5,2,8,4,9,0,2]
# a = [0,3,2,4,5,6,7,1,9,8]

def is_even(p):
  n = len(p)
  sign = 0
  
  i = 0
  while (i < n):
    # find min
    i2 = i + 1
    min_idx = -1
    while (i2 < n):
      if min_idx == -1 or p[i2] < p[min_idx]:
        min_idx = i2
      i2 += 1

    # transposition
    if p[i] > p[min_idx]:
      # swap
      tmp = p[i]
      p[i] = p[min_idx]
      p[min_idx] = tmp
      # toggle sign
      sign = 1 - sign

    i += 1
  
  return True if sign == 0 else False

print(is_even(a))
