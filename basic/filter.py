words = ['real', 'man', 'rhythm', 'man', 'wow']
r_words = [word for word in words if word.startswith('r')]

print(r_words)

def starts_with_r(word):
  # 맞으면 true, 틀리면 false반환
  return word.startswith('r')

# => filter(f, lst= [x, y, z]) = [f(x)== true? 줘, f(y)== false 안 줘, f(z)== true 줘!]
# true로 반환된 것들만 모아서 filter 타입으로 던져줌
r_words = filter(starts_with_r, words)
print(r_words)

# filter도 연산을 나중으로 미루기에 데이터를 사용하지 않으면 연산하지 않음 나중에 필요할 때 연산하여 돌려줌!
r_words = filter(lambda word: word.startswith("r"), words)
print(r_words)
