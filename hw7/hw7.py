'''
сколько в тексте разных существительных с суффиксом -ness
и какое существительное из них имеет максимальную частотность.
'''
def textwords(file_name):
    with open (file_name, encoding = 'utf-8') as file:
        text = file.read()
        words = text.split()
    return words


def extract_constr(words):
    '''ищем слова, оканчивающиеся на -ness и заносим их в лист'''
    constr_list = []
    for i, word in enumerate(words):
        if word.endswith('ness'):
            constr_list.append(word.lower() + '\n')
                
    return  constr_list

def write_results(constr_list, fname):
    with open(fname, "w") as f:
        f.writelines(constr_list)

def frequency(constr_list):
    dic = {}
    import collections
    for wor in constr_list:
        if wor in dic:
            dic[wor] += 1
        else:
            dic[wor] = 1
    counter = collections.Counter(dic)  
    return print(counter.most_common(1))


'''
    from collections import Counter
    list1= constr_list
    counts = Counter(list1)
    print(counts)
    return print(counts)
'''
'''
    mydict= {}
    for i in range(len(constr_list)):
        mydict = constr_list.count(constr_list[i])
        print(mydict)
    return print(mydict)
'''
def main():
    maintext = textwords("Pride_and_Prejudice.txt")
    constr_list = extract_constr(maintext)
    write_results(constr_list, 'constr.txt')
    diction = frequency(constr_list)
    
main()

if __name__ == '__main__':
    main()
