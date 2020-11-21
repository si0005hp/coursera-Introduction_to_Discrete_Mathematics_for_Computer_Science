def pascal_triangle_next_layer(nums):
  head = nums[0]
  tail = nums[-1]

  result = list()
  for i in range(0, len(nums) - 1):
    left = nums[i]
    right = nums[i + 1]

    result.append(left + right)

  result.insert(0, head)
  result.append(tail)
  return result


def print_layer(i, nums):
  print(f"""{i}:\t{nums}""")

def calc_near_center_fraction(layers):
  next_layer = [1]
  print_layer(1, next_layer)
  for i in range(2, layers + 1):
    next_layer = pascal_triangle_next_layer(next_layer)
    # print_layer(i, next_layer)
  
  fraction = sum(next_layer[40:60]) / sum(next_layer)
  print(fraction)

# calc_near_center_fraction(100)
calc_near_center_fraction(1000)
