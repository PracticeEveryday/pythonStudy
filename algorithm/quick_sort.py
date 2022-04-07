from numpy import number


numbers_list = list(map(int, input().split()))

def quick_sort(numbers_list) :
  if len(numbers_list) <= 1:
    return numbers_list 
  pivot = numbers_list[0]
  left = []
  right = []
  for i in numbers_list[1:] :
    if i < pivot : 
      left.append(i)
    else :
      right.append(i)

  return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(numbers_list))