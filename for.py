fruits = ['apple', 'banana', 'kiwi']

# fruits에 있는 원소들을 fruit에 저장(in)해서 돌려라@
for fruit in fruits :
  print(fruit + "는 맛있어")

# range
# 0 ~ 9까지 한 줄씩 출력한다.
for num in range(10):
  print(num)

for i in range(len(fruits)):
  print("과일" + str(i+1) + ":" + fruits[i])

trump_tweets = [
    'Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!',
    'Companies are giving big bonuses to their workers because of the Tax Cut Bill. Really great!',
    'MAKE AMERICA GREAT AGAIN!'
]

for i in range(len(trump_tweets)):
  print("trump_twwts 2018년 1월 " + str(i+1)+ "일" +trump_tweets[i] )