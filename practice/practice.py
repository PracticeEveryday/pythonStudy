class test :
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    self.lst = []

  def add(self):
    return self.num1 + self.num2

  def add_lst(self, n):
    self.lst.append(n)

test_num = test(3, 4)
print(test_num.num1, test_num.num2)
print(test_num.add())
test_num.add_lst(3)

print(test_num.lst)

# 감기걸린 사람 수 , 직원들을 관찰하는 시간
# 그 다음 N개의 줄에는 기침하는 주기를 한줄에 하나씩 입력
# 2개면 2줄, 3개면 3줄

persons, times = list(map(int,input().split()))

total = 0
lst = []
for i in range(persons):
    cycles = int(input())
    total = int(times/cycles)
    for j in range(1, total+1):
        if(j*cycles in lst) :
            pass
        else :
            lst.append(j * cycles)
print(len(lst))


# 직사각형 모안 초콜릿 각 칸에 문자가 한 개씩 쓰여있음.
# 이 때 초콜릿을 조각내어 각 조각에 적혀있는 문자를 읽어 단어를 만들 수 있다.
# 예를들어 'a', 'b', 'c', 'd' 는 'ab', 'bc', 'cd', 'abc', 'bcd'의 단어가 적힌 9개 만들 수 있음 단어 중복은 허용 x
# 쪼개기 전 초콜릿에 적힌 문자로 만든 단어를 줬을 때 초콜릿을 조각으로 쪼개고 읽은 서로 다른 단어의 개수를 출력하는 프로그램

# 첫번째 줄에 쪼개기 전 초콜릿에 적힌 문자로 만든 단어 입력

# 초콜릿을 조각으로 쪼개고 서로 다른 단어의 개수를 출력

text = input()

result = 0

def test(text) :
    test_list = []
    for i in text:
        if i in test_list :
            pass
        else :
            test_list.append(i)
    
    if len(test_list)==1:
        return 1
        
    else :
        global result
        for i in range(1, len(test_list) + 1):
            result += i
        return result -1
        
print(test(text))

# a => a 1개 1
# ab => a, b 2개 1 + 1
# abc => a, b, c, ab, bc 5개 3 + 2
# abcd => a, b, c, d, ab, bc, cd, abc, bcd 9개  4 + 3 + 2
# abcde => a, b, c, d, e, ab, bc, cd, de, abc, bcd, cde, abcd, bcde 14개  5 + 4 + 3 + 2

# 첫자리 수는 +1 씩 두개는 +1씩 3개도 +1씩 4개도 +1씩
