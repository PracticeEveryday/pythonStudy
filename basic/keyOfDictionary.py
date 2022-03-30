'''
dhkim = ['dhkim', 'helloworld']

account = {
  dhkim : ('my', 'study', 'h!')
}

dhkim[0] = 'modify'

print(account)

# x 변할 수 없는 값만 키로 올 수 있다.
so 바꾸고 싶으면 키 벨류 삭제 후 만들어야함.
'''

accounts = {
  'a' : 'modified',

}

# key 확인하기!
print('a' in accounts)

for key, value in accounts.items():
  print(f'{key} + {value}')

print(accounts.items())

user_title = {
    1: [271, 318, 491],
    2: [318, 19, 2980, 475],
    3: [475],
    4: [271, 318, 491, 2980, 19, 318, 475],
    5: [882, 91, 2980, 557, 35],
}
def title_num(user_title):
    num_title = {}

    for key, value in user_title.items():
        num_title[key] = len(value)
    
    return num_title

print(title_num(user_title))