#Ветошкина Арина
#Вариант 2

a = input("Введите слово:")
wl = []
wl.append(a)
while a != "":
    a = input("Введите слово:")
    wl.append(a)
with open('text.txt', 'w', encoding="utf-8") as f:
    fwl = []
    for word in wl:
        if len(word) > 5:
            with open('text.txt', 'a', encoding="utf-8") as f:
                f.write(word + '\n')
