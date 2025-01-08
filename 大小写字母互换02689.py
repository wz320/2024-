juzi=input()
juzi=list(juzi)
for i in range(len(juzi)):
    a=str(juzi[i])
    if a.islower():
        a=a.upper()

    elif a.isupper():
        a=a.lower()
    else:
        a=a
    juzi[i] = a
print("".join(juzi))
