"""
word = "Привет"
print (word)

a=0
for i in word:
        print (i,a)
    a += 1
"""
"""
print (a)
print ('='*10)

#print(word[0])
print(len(word))
print(word[len(word)-1])
print(word[-4])
"""
'''
word = "Добрый_день!"
print (word)

part = word[3:6]
print (word[:3] + '!' + part + '!' + word[6:])

a=0
for letter in word:
    if a % 2 !=0:
        print (letter)
    a += 1
'''
'''
word = "Добрый_день!"
print (word)

for i in range(3,20,2):
    print()
    print("i =", i)
    if i > 10 and i % 2 != 0:
        print(i**2)

print("End.")
'''
'''
word = "Добрый_день!"
print (word)
mysum = 0
for i in range (3,20, 2):
    mysum += i
    print (i, "mysum=", mysum)
print (mysum)
'''
'''
a = int(input ("введите а:") )

mysum = 0
for k in range (a+1):
    mysum += k
    print (k, "mysum=", mysum)
print (mysum)
'''
'''
i = 10
while i >= 5:
    print(i)
    i -=1
print("i =", i)
'''
'''
i = 2
while i**2 <= 100:
    print(i, i**2)
    i +=1
'''
'''
for i in range (10):
    print(i)
    if i **2 > 37:
        break
print ("end")
'''
'''
for i in range (10):
    print()
    print(i, end=", ")
    if i == 8:
        continue
    print(i**2)
print("end!")
'''
'''
print ("hello", end=', ')
print ("world!")
'''
'''
for i in range (5):
    word =  input ("введите слово:")
    print (len(word))
'''
a = int (input("сколько чисел проверим?"))
for i in range(a):
    x = int(input("Введите число:"))
    if x > 0:
        print("Больше 0")
    elif x < 0:
        print ("Меньше 0")
    else:
        print("Ноль")
print ("end")
ldld
