import random

num_list = list(map(int, input().split()))

print(num_list)
add_abs = []
while True :
  random.shuffle(num_list)
  if len(add_abs) > 1000 :
    break
  for i in range(len(num_list)) :
    value = abs(sum(num_list[:i+1]) - sum(num_list[i+1:]))
    if value in add_abs :
      pass
    elif value not in add_abs :
      add_abs.append(value)
    

  
print(min(add_abs))