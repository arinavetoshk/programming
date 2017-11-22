#Арина Ветошкина
#Вариант 2
fname = "text.txt"
with open(fname, encoding="utf-8") as f:
    alist = [line.rstrip() for line in f]
len_str1 =  len(max(alist,key = len).split())
len_str2 =  len(min(alist,key = len).split())
print("Самая  длинная строка: ", len_str1)
print ("Самая короткая строка: ", len_str2)
m = len_str1/len_str2
print("Самая короткая строка меньше самой длинной в", ("%.2f" % m), "раз(-а).")
