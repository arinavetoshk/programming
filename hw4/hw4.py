#Арина Ветошкина
#Вариант 2
fname = "C:\\Users\\Арина\\Desktop\\text.txt"
with open(fname, encoding="utf-8") as f:
    alist = [line.rstrip() for line in f]
len_max =  len(max(alist,key = len).split())
len_min =  len(min(alist,key = len).split())
print("Самая  длинная строка: ", len_max)
print ("Самая короткая строка: ", len_min)
m = len_max/len_min
print("Самая короткая строка меньше самой длинной в", m, "раз(-а).")
