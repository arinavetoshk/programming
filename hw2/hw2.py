# Ветошкина Арина
# Вариант 2

word = input ("введите слово:")
cyrlet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
for letter in word:
    if (letter in cyrlet):
        break
    else:
        print ("Пожалуйста, используйте кириллицу")
        break       
a = 1
for letter in word:
    if (a % 2 != 0) and (letter in ('о','п','е')) :
        print (letter)
    a += 1
