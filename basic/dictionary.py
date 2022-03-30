# {key : value}
# key : 값을 찾기 위해 넣어 주는 데이터
# value : 찾고자 하는 데이터


dict = {}
new_dict = {
  'apple' : '사과',
  "book" : '책',
  'human' : '사람'
}

dict['apple'] = '사과'
dict['boo'] = '책'
dict['human'] = '사람'

print(dict)

arr = [('apple', '사과'), ('book', '책'), ('human', '사람')]
print(arr)

print([i for i in arr if i[0]=='apple'])
# 모든 아이디를 확인해야 하므로 데이터가 많을 경우 수십배 까지도 성능 차이가 남

