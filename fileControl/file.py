import os
currentPath = os.getcwd()
  

filename = currentPath + '\\fileControl\\data.txt'
print(filename)
def print_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        line_number = 1    

        for line in file:
            print(line_number, line)
            line_number += 1


print_lines(filename)


'''

file = open('data.txt')

content = file.read()
print(content)

file.close()

# with as?!
with open('data.txt') as file:
  content = file.read()

# 들여쓰기가 사라지면 파일이 닫히고 끝남!

contents = []

with open('data.txt') as file:
  for line in file:
    content.append(line)
    print(contents)

# 파일의 모드!
# 쓰기 (Write) 모드로 파일을 연다
# 기본적으로 2번재 인자에 주지 않으면 읽기 모드로 연다!
'''