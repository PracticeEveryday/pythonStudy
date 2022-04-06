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

# dequq : double-ended-queue
# 양뱡향에서 추가 제거 가능한 자료구조

from collections import deque

q = deque([4, 5, 6])
q.append(7)
q.append(8)

print(q)

q.popleft()
q.popleft()

print(q)

q = deque([4, 5, 6])
q.appendleft(3)
q.appendleft(2)

print(q)

q.pop()
q.pop()

print(q)

from queue import Queue

que = Queue()

# Queue는 방향성이 없기에 추가는 put, 삭제는 get메서드 사용
que.put(4)
que.put(5)
que.put(6)

print(que.get())
print(que.get())
print(que.get())
