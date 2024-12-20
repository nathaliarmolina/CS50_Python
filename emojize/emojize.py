import emoji

emo = input("Input: ")


print ('Output: ', end="")
print(emoji.emojize(emo, language="alias"))
