
import random

def compare(first_word, second_word):

    g = 0
    l = 0

    word_first = [bool(first_word[i]) for i in range (len(first_word))]
    word_second = [bool(second_word[i]) for i in range(len(second_word))]

    for i in range(len(first_word)):
        g = g or (not(word_second[i]) and word_first[i] and not(l))
        l = l or (word_second[i] and not(word_first[i]) and not(g))
    
    if g == 0 and l == 0:
        return '='
    elif g == 1 and l == 0:
        return '>'
    else:
        return '<'

def most_big(mas_word):
    if mas_word == []:
        return None
    copy_mas = mas_word.copy()
    for i in range(len(copy_mas[0])):
        biggest_word = []
        for j in range(len(copy_mas)):
            if copy_mas[j][i] == 1:
                biggest_word.append(copy_mas[j])
        if biggest_word != []:
            copy_mas = biggest_word

    return copy_mas

def most_little(mas_word):
    if mas_word == []:
        return None
    copy_mas = mas_word.copy()
    for i in range(len(copy_mas[0])):
        smallest_word = []
        for j in range(len(copy_mas)):
            if copy_mas[j][i] == 0:
                smallest_word.append(copy_mas[j])
        if smallest_word != []:
            copy_mas = smallest_word
            
    return copy_mas

def find_down(mas_word, key_word):
    smaller_word = []
    for i in range((len(mas_word))):
        if compare(key_word, mas_word[i]) == '>':
            smaller_word.append(mas_word[i])
    
    biggest = most_big(smaller_word)
    return biggest            

def find_up(mas_word, key_word):
    bigger_word = []
    for i in range((len(mas_word))):
        if compare(key_word, mas_word[i]) == '<':
            bigger_word.append(mas_word[i])
    
    smallest = most_little(bigger_word)
    return smallest   

def number_one(key_word):
    one = 0
    for i in range(len(key_word)):
        if key_word[i] == 1:
            one += 1
    return one
    
def bool_operation(mas_word, operation): 
    rezult = [] 
    if operation == '/\\' or operation =='&':
        for i in range(len(mas_word)):
            if number_one(mas_word[i]) == len(mas_word[i]):
                rezult.append(mas_word[i])
    elif operation == '\\/' or operation =='*':
        for i in range(len(mas_word)):
            if number_one(mas_word[i]) > 0:
                rezult.append(mas_word[i])
    elif operation == '^' or operation =='+':
        for i in range(len(mas_word)):
            if number_one(mas_word[i]) == 1:
                rezult.append(mas_word[i])
    elif operation == '~':
        for i in range(len(mas_word)):
            if number_one(mas_word[i]) == 0 or number_one == len(mas_word[i]):
                rezult.append(mas_word[i])  
    return rezult      
        
    

mas_words = []
while True:
    if mas_words == []:
        number_words = int(input('Введите количество слов:'))
        bits_of_words = int(input("Введите количество бит в слове:"))
        mas_words = [[random.randint(0,1) for n in range(bits_of_words)] for m in range(number_words)]
        for word in mas_words:
            print(word)
    comands = input('\n1 - Новый масив \n2 - Поиск ближайшего с низу значения \n3 - Поиск ближайшего с верху значения\n4 - Поиск по основе булевых функций\n')
    match(comands):
        case '1':
            number_words = int(input('Количество слов: '))
            bits_of_words = int(input('Количество бит в словах: '))
            mas_words = [[random.randint(0,1) for n in range(bits_of_words)] for m in range(number_words)]
            for word in mas_words:
                print(word)
        case '2':
            key_word = input('Введите свое слово: ')
            key_word = key_word.replace(' ','')
            key_word = [int(el) for el in key_word.split(',')]
            smallest = find_down(mas_words, key_word)
            if smallest == []:
                print('Нет слова меньше заданного!')
            else:
                for word in smallest:
                    print(word)
        case '3':
            key_word = input('Введите свое слово: ')
            key_word = key_word.replace(' ','')
            key_word = [int(el) for el in key_word.split(',')]
            bigger_word = find_up(mas_words, key_word)
            if bigger_word == []:
                print('Нет слова больше заданного!')
            else:
                
                for word in bigger_word:
                    print(word)
        case '4':
            bool_function = input('Введите функцию: ')
            rezult = bool_operation(mas_words, bool_function)
            if rezult == []:
                print('Нет подходящего слова!')
            else:               
                for word in rezult:
                    print(word)
            