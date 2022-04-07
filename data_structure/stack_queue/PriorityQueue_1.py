# 우선 순위 큐는 데이터를 추가한 순서대로 제거하는 선입선출 특성을 가진 일반 Queue와 달리 데이터 추가는 어떤 순서를 해도 상관 없지만 제거 될 때는 가장 작은 값을 제거하는 아이임
# 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 있다는 뜻

from queue import PriorityQueue

q = PriorityQueue()

# 우선순위 큐의 디폴트 사이즈는 무한대이기 때문에 특정 최대 값을 가진 큐를 원하면 maxsize를 넘겨야함
q = PriorityQueue(maxsize = 8)

q.put(4)
q.put(7)
q.put(1)
q.put(40)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 정렬 기준 변경
# 오름 차순이 아닌 다른 기준으로 원소가 정렬되긴 원한다면 (우선순위, 값)의 튜플 형태로 데이터를 추가하고 제거하자

q.put((3, 'Apple'))
q.put((1, 'Banana'))
q.put((2, 'Cherry'))

print(q.get()[1])
print(q.get())
print(q.get())