# 스플릿은 괄호 안에 쪼개는 문자열 집어넣을 수 있고 빈 괄호를 넣어 모든 공백 문자를 없애줄 수 있다.

intro = "Hello World haha"
print(intro.split())

fruits = "apple, banana, pear"
print(fruits.split(','))

numbers = " 1            2     3  "
# 문자만 남겨줘
print(numbers.split())

# 뛰어쓰기도 만들어줘
print(numbers.split(' '))

# 대표적인 공백 문자
# 빈칸 ' '(스페이스바)
# '\t' Tab(Tab키)
# '\n' Newline(엔터키)
# .split() -> 모든 공백문자로 쪼갠다!!