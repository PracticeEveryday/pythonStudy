
numbers, case = map(int,input().split())

numbers_list = list(map(int, input().split()))
check = []

results = []

for i in numbers_list :
  check.append(i)
  if len(check) <= 2 :
    results.append(-1)
  else :
    check.sort()
    results.append(check[2])

print(*results)
    
    
