# .append()

number = []
number.append(1)
print(number)

number.append(2)
print(number)

numbers = [1, 2, 10, 17]

small_numbers = []
for num in numbers :
  if num < 10 :
    small_numbers.append(num)

print(small_numbers)

trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

def make_new_list(text):
    new_list = []
    for word in text:
        if word.startswith("b"):
            new_list.append(word)
    return new_list

new_list = make_new_list(trump_tweets)
print(new_list)