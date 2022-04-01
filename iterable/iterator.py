from random import randint

class RandomIntIterator:
    def __init__(self, n):
        self.count = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            return randint(1, 100)
        else:
            raise StopIteration


class RandomIntIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return RandomIntIterator(self.n)

able = RandomIntIterable(3)
tor1 = iter(able)
tor2 = iter(able)

assert tor1 != tor2

# 1. Iterator에 iter 함수 적용
assert tor1 is iter(tor1)


# 2. next를 통해 각 값을 반환
print(next(tor1))
print(next(tor1))
print(next(tor1))
# 3을 인자로 줬으니 터짐
# print(next(tor1))

for n in RandomIntIterable(5):
    print(n)