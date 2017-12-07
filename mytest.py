#Вариант1
'''
#1
fname = "C:\\Users\\Арина\\Desktop\\quotes.txt"
with open(fname, encoding="utf-8") as f:
    quote = f.readlines()
for line in quote:
    word = line.split()
for q in quote:
    if len(quote) > 10 and len(q.split(' ', 1)[0]) < 5:
        print(q)
'''
#2
fname = "C:\\Users\\Арина\\Desktop\\quotes.txt"
wl = []
with open(fname, encoding="utf-8") as f:
    for line in f:
        for part in line.split():
            if "разум" in part:
                wl.append(line)
print (len(wl))
  
