alphabet_latter = 33

def number_value(key_word):
    first_latter = ord(key_word[0]) - ord('а')
    second_latter = ord(key_word[1]) - ord('а')
    rezult = first_latter*alphabet_latter + second_latter
    return rezult

def hash_address(rezult, string_table):
    hash_address = rezult % string_table+1
    return hash_address

def add_string(table, key_word, information):
    number = number_value(key_word)
    hash = hash_address(number, len(table))
    
    if table[hash-1][1] == None:
       table[hash-1] = [hash, key_word, number, hash, None, information]
    else:
        for i in range(len(table)):
            if table[i][1] == None:
                table[i] = [i+1, key_word, number, hash, None, information]
                break
        if table[hash-1][4] == None:
            table[hash-1][4] = i+1
        else:
            not_empty = True
            address = hash
            while not_empty:
                if table[address-1][4] == None:
                    table[address-1][4] = i+1
                    not_empty = False
                else:
                    address = table[address-1][4]
    return table

def search(table, key_word):
    number = number_value(key_word)
    hash = hash_address(number, len(table))
    if table[hash-1][1] == key_word:
        print (table[hash-1])
    else:
        not_key_word = True
        address = hash
        while not_key_word:
            if table[address-1][1] == None:
                print('Нет такого слова!')
                not_key_word = False  
            elif table[address-1][1] == key_word:
                not_key_word = False  
                print (table[address-1])   
            else:
                address = table[address-1][4]
                
def search_previous(table, address):
    for i in range(len(table)):
        if table[i][4] == address:
            return i

def delete(table, key_word):
    number = number_value(key_word)
    hash = hash_address(number, len(table))
    if table[hash-1][1] == key_word:
        if table[hash-1][4] == None:
            table[hash-1] = [hash, None, None, None, None, None]
        else:
            next_address = table[hash-1][4]
            table[hash-1] = table[next_address-1]
            table[next_address-1] = [hash, None, None, None, None, None]
    else:
        not_key_word = True
        address = hash
        while not_key_word:
            if table[address-1][1] == key_word:
                previous = search_previous(table, address)
                table[previous][4] = table[address-1][4]   
                table[address-1] = [table[address-1][0], None, None, None, None, None]
                not_key_word = False
            else:
                address = table[address-1][4] 
    return table       

string_table = int(input('Введите количесвто строк:'))
table = [[i+1, None, None, None, None, None] for i in range(string_table)]


while True:
    comand = input('Выберите команду:\n 1 - Добавить строку \n 2 - Найти информацию \n 3 - Удалить строку \n 4 - Отобразить таблицу \n')
    match(comand):
        case '1':
            key_word = input('Введите слово:')
            information = input('Введите информацию о строке:')
            table = add_string(table, key_word, information)
        case '2':
            key_word = input('Введите слово:')
            search(table, key_word)
        case '3':
            key_word = input('Введите слово:')
            table = delete(table, key_word)
        case '4':
            for i in range(len(table)):
                print(table[i])