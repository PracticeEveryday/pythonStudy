intro = "My name is DH!"

print(intro.upper())
print(intro.lower())

# append vs lower

words = ['hello']
words.append("world")
print(words, len(words))

# if...
intro = "My name is DH!"
intro.lower()
print(intro)
# 원래 문자열을 직접 수정하지 않는다.
# 실행했을 때 값이 리턴되는 것임!!

lower_intro = intro.lower()
print(lower_intro)

trump_tweets = [
    "FAKE NEWS - A TOTAL POLITICAL WITCH HUNT!",
    "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election.",
    "The Fake News media is officially out of control.",
]
def lowercase_all_characters(text):
    processed_text = []
    # 아래 코드를 작성하세요.
    for i in text :
        processed_text.append(i.lower())

    return processed_text

print('\n'.join(lowercase_all_characters(trump_tweets)))