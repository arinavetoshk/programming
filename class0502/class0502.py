def read_data(file_name):
    #читаем по строкам
    with open (file_name, encoding = 'utf-8') as file:
        lines = file.readlines()
    return lines
def character_text(raw_lines):
    #создаем словарь
    character_all_texts = {}
    #идем по строчкам, делим по запятым, смотрим с первого элемента до конца
    for line in raw_lines[1:]: # 0 is for shapka of table
        splitted = line.split(',')
        if len(splitted) > 3:
            name = splitted[2] #так как не считаем 1 строчку
            text = ','.join(splitted[3:])
            text = text[1:] #возвращаем строку с текстом с первого элемента
            if name in character_all_texts:
                character_all_texts[name] = character_all_texts[name] + '\n' + text
            else:
                character_all_texts[name] = text     
        
    return character_all_texts

def freq_d(person, character_texts):
    top_words = []
    freq = {}
    no_punct = character_texts.replace('.', ' ')
    no_punct = no_punct.replace(',', ' ')
    tokens = no_punct.split()
    
    return top_words
    
def main():
    raw_data = read_data('all-seasons1.txt')
    all_texts = character_text(raw_data)
    #for character in all_texts:
     #   print(character, len(all_texts[character]))
    texts_length = {}
    for character in all_texts:
        if character not in texts_length:
            texts_length[character] = len(all_texts[character])#считаем длину реплик героя
    main_characters_pre = texts_length.items()
    main_characters = [] #добавляем в лист героя и кол-во реплик
    for name, length in main_characters_pre:
        main_characters.append([length, name])
    print(sorted(main_characters, reverse=True)[:20]) #сортируем
    main_names = []
    for length, name in main_characters:
        main_names.append(name)
    print(main_names)
    for character in main_names:
        top = freq_d(character, all_texts[character])
        print(character)
        print(top)
        
        

if __name__ == "__main__" :
          main()
