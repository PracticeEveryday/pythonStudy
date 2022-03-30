'''
  집합 : 순서가 없다, 중복이 없다.
'''

set1 = {1, 2, 3}
set2 = set([1, 2, 3])
set3 = {3, 2, 3, 1}
# 셋다 같은 셋
print(set1, set2, set3)

num_set = {1, 3 ,5 , 7}
# 추가! set을 직접 수정하는 함수
num_set.add(9)
# 여러개 한 번에 추가
num_set.update([3, 15, 4])
num_set.update({2, 18, 9})

num_set.remove(7)
num_set.discard(13)
# removs vs discard descard는 있으면 삭제하고 없으면 무시 remove는 무조건 존재해야함(error 띄움).
print(num_set)

print(6 in num_set)
print(len(num_set))


my_set = {3, 5}
my_set.add(7)
new_numbers = [1, 2, 3, 4, 5]
my_set.update(new_numbers)
my_set = {num for num in my_set if num%2 == 1}

