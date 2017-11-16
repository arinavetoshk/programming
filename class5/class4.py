#print("пример\tстрока")
'''
HOW TO OPEN A FILE
fname = "C:\\Users\\student\\Desktop\\PY.txt"
print(fname)
with open(fname) as f:
    text = f.read()
print(type(text))

text = ""
f = open(fname)
text = f.read()
print(text)
f.close()
'''
'''
#Splitting by lines
fname = "C:\\Users\\student\\Desktop\\PY.txt"
print(fname)
with open(fname) as f:
    text = f.read()
print(text[:100])
lines = text.split("\n")
print(lines[:5])
'''
"""
#spliting by words
fname = "C:\\Users\\student\\Desktop\\PY.txt"
print(fname)
with open(fname) as f:
    text = f.read()
#print(text[:100])
lines = text.split("\n")
#print(lines[:5])
for line in lines:
    words = line.split()
    for word in words:
        print(word)
    print()
"""
'''
#spliting in list
fname = "C:\\Users\\student\\Desktop\\PY.txt"
print(fname)
with open(fname) as f:
    text = f.read()
lines = text.split("\n")
text_el = []
for line in lines:
    words = line.split()
    text_el.append(words)
    for word in words:
        print (word)
    print()
print(text_el[-2:])
'''
'''
lines = text.split("\n")
text_el = []
for line in lines:
    words = line.split()
    text_el.append(words)
    for word in words:
        print (word)
    print()
print(text_el[-2:])
print(len(text_el))
'''
fname = "C:\\Users\\student\\Desktop\\PY.txt"
print(fname)
with open(fname) as f:
    lines = f.readlines()
print(lines)
print(len(lines))
"""
>>> "HELLO".isupper()
True
>>> "heLLo".islower()
False
>>> 
