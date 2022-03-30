# xor = exclusive of 베재한 or 둘 중 하나만 만족한다면 A-B + B - A

set1 = {1, 3, 5, 7}
set2 = {1, 3, 9, 27}

union = set1 | set2         # 합집합
intersection = set1 & set2  # 교집합
diff = set1 - set2          # 차집합
xor = set1 ^ set2           # XOR

print(union, intersection, diff, xor)