movies = [
  '다크나이트, The Dark Knight, 2008',
  '겨울왕국, Frozen, 2013',
  '슈렉, Shrek, 2001',
  '슈퍼맨, Superman, 1978'
]

def get_eng_title(row) :
  split = row.split(',')
  return split[1]

eng_title = [get_eng_title(row) for row in movies]

print(eng_title)

eng_titles = map(get_eng_title, movies)
# => map(f, lst= [x, y, z]) = [f(x), f(y), f(z)]

eng_titles = map(lambda row: row.split(',')[1], movies)
print(eng_titles)


# map ==? list??
# map은 리스트가 아닌 map이라는 타입을 가짐 맵은 리스트로 바로 만들어 주지 않음.
# 꺼내 갈때 함수를 적용시켜서 내어주어라 라고 하는 것임
# 리스트가 10만개일때 map쓰고 사용을 안함. list를 쓰면 1000만개 만들고 다음꺼함
# 하지만 100만개 정의만 해놓고 쓸때 바꿔줌!
# list(map)할때 그 즉시 바꾸고 넘겨줌!

print(eng_titles)
print(list(eng_titles)[0])