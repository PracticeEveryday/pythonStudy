# .startwith()
# 문자열의 앞에 어떤 단어가 등장하는 지 알려주는 문자열 내장 함수



word = "HelloWolrd"

print(word.startswith("H"))

if(word.startswith("hello")):
  print("hello로 시작한답니다.")
else :
  print(word.startswith("hello"))
  print("hello가 아니라 Hello입니다")


trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(tweet):

  for text in tweet:
      if(text.startswith("k")):
          print(text)
  
print_korea(trump_tweets)