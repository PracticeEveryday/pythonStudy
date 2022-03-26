# 문자열 함수는 문자열을 직접 수정하지 않고 새로운 값을 return 해낸다!!

intro = "mY name is DH"
print(intro.replace("mY", "My"))

print(intro.replace(" ", ""))

# if...
intro.replace(' ','')
print(intro)

# if replace
replace_intro = intro.replace(' ','')
print(replace_intro)


trump_tweets = [
    "i hope everyone is having a great christmas, then tomorrow it's back to work in order to make america great again.",
    "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
    "merry christmas!!!",
]

def remove_special_characters(text):
    processed_text = []

    for i in text:
        processed_text.append(i.replace("!","").replace("'","").replace(",",""))

    return processed_text

print('\n'.join(remove_special_characters(trump_tweets)))