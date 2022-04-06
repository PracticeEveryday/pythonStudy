words = ['Hello', 'World']

first_spelling = []

for i in words:
  first_spelling.append(i[0])

print(first_spelling)

# list Comprehension
# [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]

first_spelling = [word[0] for word in words]
print(first_spelling)

numbers = [1, 239, 4123, 13]
new_number = []

for num in numbers:
  new_number.append(num+1000)

print(new_number)

new_number = [num+100 for num in numbers]
print(new_number)

numbers = [1, 3, 5, 6, 10, 22]

even = []
for num in numbers:
  if num % 2 == 0:
    even.append(num)

print(even)

even = [n for n in numbers if n % 2 == 0]
print(even)

words = [
    'apple',
    'banana',
    'alpha',
    'bravo',
    'cherry',
    'charlie',
]

def filter_by_prefix(words, prefix):
    # 아래 코드를 작성하세요.
    prefix_word = [word for word in words if word[0] == prefix]
    
    return prefix_word

a_words = filter_by_prefix(words, 'a')
print(a_words)
