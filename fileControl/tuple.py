# 튜플 (Tuple)

hello = ("hello", "world", "haha")

apple = ("사과", 'apple')

red = ("빨갛다", "red")

# 공통점 : 순서가 있는 원소들의 집합
# 차이점 : 각 원소의 값을 수정할 수 없음, 원소의 개수를 바꿀 수 없음 (Tuple)

# Tuple 직접 변형 불가!!

filename = 'corpus.txt'

def import_as_tuple(filename):
    tuples = []
    with open(filename) as file:
        for line in file:
            split = line.strip().split(',')
            word = split[0]
            freq = split[1]
            new_tuples = (word, freq)
            tuples.append(new_tuples)
            
    return tuples

print(import_as_tuple(filename))
'''
 strip : 문자열 whitespace라는 개념을 알고 넘어가도록 하자.
whitespace란, 띄어쓰기(' '), 탭('\t'), 엔터('\n') 까지, 포괄적으로 이야기 하는것이다.
이 whitespace를 제거하기 위해선, strip 함수를 사용하면 된다.
문자열의 끝에 .strip()을 붙이면,문자열의 '맨앞'과, '맨뒤' 의 whitespace가 제거가 된다.
 단, 중간중간의 whitespace는 제거가 되지 않는다.
'''