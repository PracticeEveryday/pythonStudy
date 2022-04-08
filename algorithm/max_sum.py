number_list = list(map(int, input().split()))
sum_number_list = []

print(number_list)
for i in range(len(number_list)) :
  for j in range(len(number_list)) :
    if i == j :
      pass
    elif j > i : 
      sum_number_list.append(sum(number_list[i:j+1]))

print(sum_number_list)
print(max(sum_number_list))
