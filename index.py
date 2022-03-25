# 인덱싱?
# 리스트 또는 문자열 순서가 있는 자료열에서 이 순서가 몇번째인가?

fruits = ['apple', 'banana', 'kiwi', 'pear']

last_fruit = fruits[-1]
tropical_fruits = fruits[1:3]
no_apple = fruits[1:]
no_pear = fruits[:3]

print(last_fruit,tropical_fruits,no_apple,no_pear)

word = "HelloWorld"

print(word[3])
print(word[-2])
print(word[5:])
print(word[:5])

trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(text):
    # 아래 코드를 작성하세요.
    for i in range(len(text)):
        if(text[i][0] == "k"):
            print(text[i])
    
    
print_korea(trump_tweets)
