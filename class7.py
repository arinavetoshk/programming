'''
#задаем функцию 
def hello():
    print("Hello")
hello()
'''
'''
#задаем переменную функции
def hello(user1, user2, user3):
    print('hello,' + user1 + '!')
    print(user2.title())
    print(user3.title())
hello("Anna", "Bob", "John")
'''
'''
def hello(user1, age):
    print('hello,' + user1 + '!')
    if age > 10:
        print('older than 10')
    else:
        print(age)
    sum_ = 0
    for i in range(16):
        sum_ += 1
    print(sum_)
hello("Anna", 15)
'''
'''
def hello(user1, age):
    print('hello,' + user1 + '!')
    if age > 10:
        print('older than 10')
    else:
        print(age)
    new_name = user1.title()
    return new_name
user_title = hello('ann', 10)
print(user_title)
'''
'''
def hello(user1):
    ''''''
    print('hello,' + user1 + '!')
    return user1.title()
user_title = hello('ann')
print(user_title)
'''
'''
#пишем сочетание, делим его по строчкам и указываем длину
def elements(word):
    for l in word:
        print(l)
    print(len(word))
sent = 'something happened here'
els = sent.split()
elements(els)
'''
'''
def tokenize(sentence):
    words = sentence.split()
    return words
sent = 'something happened here'
tok_result = tokenize(sent)
print(tok_result)
for w in tok_result:
    print(w.upper())
'''
'''
def lines_div(fname):
    
    with open(fname, encoding="utf-8") as f:
        lines_raw = f.readlines()
    lines = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            lines.append(clear_line)
    return lines
lines = lines_div('at.txt')
print(lines)
'''
def lines_div(fname):
    '''открыть файл, прочесть, разделить на строки,
вернуть мин длину строки в символах
'''
    with open(fname, encoding="utf-8") as f:
        lines_raw = f.readlines()
    lines_lengths = []
    for line in lines_raw:
        clear_line = line.strip()
        if clear_line:
            print(len(clear_line), clear_line)
            lines_lengths.append(len(clear_line))
    return min(lines_lengths)
min_l = lines_div('at.txt')
print(min_l)
