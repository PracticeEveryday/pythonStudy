number = [-1, 203, 23, 357, -129]
sort_number = sorted(number)
print(sort_number)

sort_number_abs = sorted(number, key=abs)
print(sort_number_abs)

fruits = ['cherry', 'apple', 'pear', 'banana']
sort_by_alphabet = sorted(fruits)
print(sort_by_alphabet)

def reverse(word):
  return str(reversed(word))


sort_by_last = sorted(fruits, key=reverse)
print(sort_by_last)



pairs = [
    ('time', 8),
    ('the', 15),
    ('turbo', 1),
]
   
def get_freq(pair):
    return pair[1]


def sort_by_frequency(pairs):
    return sorted(pairs, key = get_freq)


print(sort_by_frequency(pairs))