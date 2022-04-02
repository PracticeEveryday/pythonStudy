def square1(x):
  return x * x

square2 = lambda x: x * x

print(square2(2))

# assert(어떤 구문) 구문이 true면 통과, 아니면 에러!

print(square2(3), square1(3))
assert(square1(3)== square2(3))

# 함수를 만드는 또다른 방식, 조금 더 짧게 이름 없이 만들 수 있는 것이다!

def _first_letter(string):
    return string[0] if string else ''

first_letter = lambda x: x[0] if x else ''

condition = '123'
answer = ''
if condition :
  answer =  'a'
else:
  answer =  'b'

answer = 'b' if condition else 'a' # >> 동일함 
print(answer)