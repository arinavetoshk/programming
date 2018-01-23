#вариант2 трехстопный дактиль
import random
def get_text(file_name):
    with open (file_name, encoding = 'utf-8') as file:
        text = file.read()
        words = text.split(',')
    return words

def clitics():
    clitics = get_text('clitics.txt')
    clitic = random.choice(clitics)
    return clitic
def verbs1():
    verbs1 = get_text('verbs1.txt')
    return verbs1
def negverb():
    verbs2 = get_text('verbs2.txt')
    return 'не' + ' ' + 'verbs2'
def clitics2():
    clitics2 = get_text('clitics2.txt')
    return clitics2
def adj():
    adj = get_text('adj5.txt')
    return adj
def nouns2():
    nouns2 = get_text('nouns2.txt')
    return nouns2
def verbs3():
    verbs3 = get_text('verbs3.txt')
    return verbs3
def nouns4():
    nouns4 = get_text('nouns4.txt')
    return nouns4
def verbs4():
    verbs4 = get_text('verbs4.txt')
    return verbs4
def verbs2():
    verbs2 = get_text('verbs2.txt')
    return verbs2
def pronouns():
    pronouns = get_text('pronouns.txt')
    return pronouns
def punctuation():
    punctuation = get_text('punctuation.txt')
    return punctuation
def verse1():
    return pronouns() + ' ' + clitics() + ' ' + clitics() + ' ' + verbs1() + ' ' + '-' + ' ' + negverb()
def verse2():
    return clitics2() + ' ' + adj() + ' ' + nouns2()
def verse3():
    return verbs2() + ' ' + verbs3() + ' ' + nouns4()
def verse4():
    return pronouns() + ',' + ' ' + verbs4() + ',' + ' ' + verbs2()
def make_verse():
    verse = random.choice([1,2,3,4])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()
make_verse()
