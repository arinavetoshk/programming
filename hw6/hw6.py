#Вариант 2
#Ветошкина Арина
#Трехстопный дактиль
import random
def get_text(file_name):
    with open (file_name, encoding = 'utf-8') as file:
        text = file.read()
        words = text.split()
        return words

def clitics():
    clitics = get_text('clitics.txt')
    return random.choice(clitics)

def verbs1():
    verbs1 = get_text('verbs1.txt')
    return random.choice(verbs1)

def negverb():
    verbs2 = get_text('verbs2.txt')
    return random.choice(verbs2)

def clitics2():
    clitics2 = get_text('clitics2.txt')
    return random.choice(clitics2)

def adj():
    adj = get_text('adj5.txt')
    return random.choice(adj)

def nouns2():
    nouns2 = get_text('nouns2.txt')
    return random.choice(nouns2)

def verbs3():
    verbs3 = get_text('verbs3.txt')
    return random.choice(verbs3)

def nouns4():
    nouns4 = get_text('nouns4.txt')
    return random.choice(nouns4)

def verbs4():
    verbs4 = get_text('verbs4.txt')
    return random.choice(verbs4)

def verbs2():
    verbs2 = get_text('verbs2.txt')
    return random.choice(verbs2)

def pronouns():
    pronouns = get_text('pronouns.txt')
    return random.choice(pronouns)

def punctuation():
    punctuation = get_text('punctuation.txt')
    return random.choice(punctuation)

def verse1():
    return pronouns() + ' ' + clitics() + ' ' + clitics() + ' ' + verbs1() + ' - ' + 'не' + ' ' + verbs2() + punctuation()
def verse2():
    return clitics2() + ' ' + adj() + ' ' + nouns2() + punctuation()
def verse3():
    return pronouns() + ' ' + verbs3() + ' ' + nouns4() + punctuation()
def verse4():
    return clitics() + ', ' +  verbs4() + ', ' + verbs2() + punctuation()

def make_verse():   
    verse = random.choice([1,2,3,4])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    elif verse == 3:
        return verse3()
    else:
        return verse4()
    
def main():
    for n in range(4):
        print(make_verse().capitalize())

if __name__ == "__main__":
    main()
    
