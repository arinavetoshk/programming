#Ветошкина Арина
#Вариант 2
word = input("Введите слово: ")
wlist = list(word)
i = ""
for l, item in enumerate(wlist):
    item = wlist[l]
    i += i.join(item)
    print(i)


