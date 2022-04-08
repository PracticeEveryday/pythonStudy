number_list = list(map(int, input().split()))

number = int(input())


def closest(number_list, number) :
  pivot = number_list[len(number_list)//2]
  print(pivot)
  if len(number_list) == 1 :
    return (number_list[0], number_list[0])
  elif len(number_list) == 2:
    return (number_list[0], number_list[1])
  
  if pivot <= number :
    return closest(number_list[len(number_list)//2:], number)
  else :
    return closest(number_list[:len(number_list)//2+1], number)

print(closest(number_list, number))
