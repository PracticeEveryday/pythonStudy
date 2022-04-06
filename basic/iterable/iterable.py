print(help(sum))

lst = [1, 2, 3, 4, 5]

for i in lst:
  print(i, end= ' ')

from collections.abc import Container, Collection, Sequence

print(Container)
print(Collection)
print(Sequence)

print(Container.__abstractmethods__)
print(Collection.__abstractmethods__)
print(Sequence.__abstractmethods__)

l = [1, 2, 3]
t = (3, 4)
d = {'a': 1, 'b': 2}
s = set()

# assert는 뒤의 조건이 True가 아니면 AssertError를 발생한다.

assert len(l) == 3
assert len(t) == 2
assert len(d) == 2
assert len(s) == 0

assert issubclass(list, Collection)
assert issubclass(tuple, Collection)
assert issubclass(dict, Collection)
assert issubclass(set, Collection)


from collections import Iterable, Iterator, Generator

abs = (Iterable, Iterator, Generator)
basic = (list, tuple, set, dict)

for b in basic:
    for a in abs:
        print(f'{b.__name__}는 {a.__name__}를 상속 받나요?', issubclass(b, a))

string = 'abc'

for i in string:
  print(i)

import io

assert issubclass(str, Iterable)
assert issubclass(io.TextIOWrapper, Iterable)


print(Iterable.__abstractmethods__)


l = [1, 2, 3]
t = (3, 4)
d = {'a': 1, 'b': 2}
s = set()
r = range(10)

print(iter(l))
print(iter(t))
print(iter(d))
print(iter(s))
print(iter(r))


assert iter(l) != iter(l)

print(Iterator.__abstractmethods__)


iterator = iter([1, 2, 3, 4, 5])

print(next(iterator))
print(next(iterator))
print(next(iterator))

for n in iterator:
    print(n)