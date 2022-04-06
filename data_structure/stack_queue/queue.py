# queue 는 FIFO(First In First Out) 기반

# case 1 list (범용 자료구조)
# 앞으로 뺴기
q = [4, 5, 6]
q.append(7)
q.append(8)
print(q)

q.pop(0)
q.pop(0)

print(q)

# 뒤로 빼기

q = [4, 5, 6]
q.insert(0, 3)
q.insert(0, 2)
q.insert(0, 1)

print(q)

q.pop()
q.pop()

print(q)
