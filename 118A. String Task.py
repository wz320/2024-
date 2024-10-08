word=input()
word=word.lower()
word=list(word)
for i in range(len(word)):
    if word[i] in 'aeiouy':
        word[i]=''
    else:
        word[i]='.'+word[i]
print(''.join(word))