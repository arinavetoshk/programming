# Ветошкина Арина
# Вариант2
a = input ("Введите число a:")
a = int(a)
b = input("Введите число b:")
b = int(b)
c = input ("Введите число c:")
c = int(c)

if a * b == c:
        print ("a и b в сумме дают c")
else:
    print ("a и b в сумме НЕ дают c")

if (a == 0)and (b == 0):
    print ("а=0 и b=0, уравнения нет")
elif (a == 0):
    print ("a=0, уравнения нет")
elif (a*c == b) :    
        print ("c является решением линейного уравнения ax+b=0")
else:
    print ("c НЕ является решением линейного уравнения ax+b=0")
    