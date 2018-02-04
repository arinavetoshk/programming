'''
сколько в тексте разных существительных с суффиксом -ness
и какое существительное из них имеет максимальную частотность.
'''
def inputfile():
    file_name = input("Введите имя файла:")
    return file_name
def textwords(file_name):
    with open (file_name, encoding = 'utf-8') as file:
        text = file.read()
        words = text.split()
    return words


def wordlist(words):
    '''ищем слова, оканчивающиеся на -ness и заносим их в лист'''
    wlist = []
    for i, word in enumerate(words):
        if word.endswith('ness'):
            wlist.append(word.lower())                
    return  wlist

def dictionary(wlist):
    '''создаем словарь слов с ness'''
    dic = {}
    for wor in wlist:
        if wor in dic:
            dic[wor] += 1
        else:
            dic[wor] = 1
    return dic

def freq(dic):
    '''ищем сумму слов в словаре'''
    import collections
    counter = collections.Counter(dic)
    wordcount = sum(counter.values())
    return wordcount

def themostfreq(dic):
    '''ищем самое частотное'''
    import collections
    counter = collections.Counter(dic)
    themostfreq = counter.most_common(1)
    return themostfreq

def main():
    file_name = inputfile()
    maintext = textwords(file_name)
    #maintext = textwords("Pride_and_Prejudice.txt")
    wolist = wordlist(maintext)
    diction = dictionary(wolist)
    wordfreq = freq(diction)
    print('Количество слов с -ness:', wordfreq)
    mostfreq = themostfreq(diction)
    print("Самое частотное слово:", mostfreq)

if __name__ == '__main__':
    main()
