import truth_table 

TWO=2
FOUR = 4
args= 3

def convert_to_list_constituents(number_form):
    constituents = []
    for number in number_form:
        constituent_list = []
        power = TWO
        while power>=0:
            if number >= TWO**power:
                constituent_list.append(1)
                number -= TWO**power
            else:
                constituent_list.append(0)
            power -= 1
        constituents.append(constituent_list)
    return constituents

def is_gluable(constituent_1, constituent_2):
    different = 0    
    for i in range(len(constituent_1)):
        if constituent_1[i] != constituent_2[i]:
            different += 1
            unnecessary = i
    if different != 1:
        unnecessary = -1 #лишний аргумент                     
    return unnecessary

def gluing_formulas(constituents, all):
    implicants = []
    mas = [False for i in range(len(constituents))]
    for i in range(len(constituents)):  #текущая
        for j in range(i, len(constituents)): #последующая
            if is_gluable(constituents[i], constituents[j]) != -1:
                implicant = constituents[i].copy()
                implicant[is_gluable(constituents[i],constituents[j])] = -1
                if not(identical_find(implicant, implicants)):
                    implicants.append(implicant)
                mas[i] = True
                mas[j] = True 
    for i in range(len(mas)):
        if mas[i] == False:
            if all:
                return None
            else:
                implicants.append(constituents[i])                                         
    return implicants 

def identical(implicants_1, implicants_2):
    for i in range(len(implicants_1)):
        if implicants_1[i] != implicants_2[i]:
            return False
    return True

def identical_find(implicant, implicants):
    for other in implicants:
        if identical(implicant, other): 
            return True
    return False

def missing_index(implicant):
    for i in range(len(implicant)):
        if implicant[i] == -1:
            return i
        
def delete_unncessary(implicants, type_of_function):
    i = 0   
    while i < len(implicants):
        false = False
        true = False
        substituted = []    
        miss = missing_index(implicants[i])
        for j in range(len(implicants)):            
            if implicants[j][miss] != -1:
                for k in range(len(implicants[j])):
                    if k != miss and implicants[j][k] != -1:
                        if type_of_function == '\\/':
                            substituted.append(implicants[i][k] == implicants[j][k])
                        else: 
                            substituted.append(implicants[i][k] != implicants[j][k])
        for element in substituted:
            if element == False:
                false = True
            if element == True:
                true = True
        if false and true:
            implicants.pop(i)
        else: 
            i += 1
    return implicants               

def to_string(formula, type_of_function):
    list_of_brackets = []
    if type_of_function == '/\\':
        inside = '\\/'
    else:
        inside = '/\\'
    for i in range(len(formula)):
        brackets = []
        if formula[i][0] == 1:
            brackets.append('A')
        elif formula[i][0] == 0:
            brackets.append('!A')
        
        if formula[i][1] == 1:
            brackets.append('B')
        elif formula[i][1] == 0:
            brackets.append('!B')
            
        if formula[i][2] == 1:
            brackets.append('C')
        elif formula[i][2] == 0:
            brackets.append('!C')
        brackets = inside.join(brackets)
        if len(brackets)>TWO:
            brackets = '(' + brackets + ')'
        
        list_of_brackets.append(brackets)
        
    return type_of_function.join(list_of_brackets)   

def is_included (constituent, implicant):
    for i in range(len(constituent)):
        if implicant[i] != -1 and implicant[i] != constituent[i]:
            return False
    return True
#------------------------------------------------------------------------------------------------->
def calculation_tabular_method(constituents, implicants):
    table = [[' ' for j in range(len(constituents))] for i in range(len(implicants))]
    for i in range(len(implicants)):
        for j in range(len(constituents)):
            if is_included(constituents[j], implicants[i]):
                table[i][j] = 'X'
    return table

def serch_X(table, implicant_index, column):
    for i in range(len(table)):
        if implicant_index != i:
            if table[i][column] == 'X':
                return True
    return False               

def delete_unnecessary_implicant(table, implicants):
    i = 0 
    while i < len(table):
        unnecessary = True
        for j in range (len(table[i])):
            if not(serch_X(table, i, j)):
                unnecessary = False
        if unnecessary:
            table.pop(i)
            implicants.pop(i)
        else: i+=1
    return implicants                
#---------------------------------------------------------------------------------------------------->
def table_method(constituents, type_of_function):
    dictionary_for_BC = {'00': 0, '01': 1, '11': 2, '10': 3}
    if type_of_function == '/\\':
        fill_graphic = '0'
    else: 
        fill_graphic = '1'
        
    graphic = [[' ' for j in range(FOUR)] for i in range(TWO)]
    for i in range(len(constituents)):
        BC = str(constituents[i][1]) + str(constituents[i][2])
        BC = dictionary_for_BC[BC]
        A = constituents[i][0]
        graphic[A][BC] = fill_graphic
        
    return graphic

def last_element(index, max_index):
    if index == max_index:
        return 0
    else:
        return index+1
    

def table_implicants(graphic):
    dictionary_for_str = {0: [0,0], 1: [0,1], 2: [1,1], 3: [1,0]}
    used = [[False for j in range(FOUR)] for i in range(TWO)]
    implicant = []
    for i in range(TWO):
        for j in range(FOUR):
            if graphic[i][j] != ' ' and graphic[i][last_element(j, FOUR-1)] != ' ':
                if not(used[i][j] and used[i][last_element(j, FOUR-1)]):
                    str_1 = [i] + dictionary_for_str[j]
                    str_2 = [i] + dictionary_for_str[last_element(j, FOUR-1)]
                    implicant.append(gluing_formulas([str_1, str_2], False)[0])
                    used[i][j] = True
                    used[i][last_element(j, FOUR-1)] = True
    for i in range(FOUR):
        if graphic[0][i] != ' ' and graphic[1][i] != ' ':
                if not(used[0][i] and used[1][i]):
                    column_1 = [0] + dictionary_for_str[i]
                    column_2 = [1] + dictionary_for_str[i]
                    implicant.append(gluing_formulas([column_1, column_2], False)[0])
                    used[0][i] = True
                    used[1][i] = True

    return implicant
#--------------------------------------------------------------------------------------------->  

line = input('Введите выражение: ')
table = truth_table.truth_table(line)
print('Таблица истинности:') 
print (table)

for i in range(TWO):
    if i == 0:
        formula_type = '/\\'
        print('\nСКНФ:')
    else:
        formula_type = '\\/'
        print('\n\nСДНФ:')
    number = truth_table.numeric_form(table, formula_type)
    list_form = convert_to_list_constituents(number)
    if formula_type == '/\\':        
        for i in range(len(list_form)):
            list_form[i] = truth_table.negation(list_form[i])
    print('\nРасчетный метод:')
    print('Конституенты:' + to_string(list_form, formula_type))
   
    formula = gluing_formulas(list_form, True)
    if formula == None:
        print('Склеивание не выполнено, не возможно склеить все конституенты!')
    else:
        print('Импликанты:' + to_string(formula,formula_type))
        tupic = delete_unncessary(formula, formula_type)
        print('ТНФ:' + to_string(tupic, formula_type))
        print('ТТНФ:' + to_string((gluing_formulas(tupic, False)),formula_type))
        
        print('\nРасчетно табличный метод:')       
        constituents = convert_to_list_constituents(number)
        if formula_type == '/\\':        
            for i in range(len(constituents)): 
                constituents[i] = truth_table.negation(constituents[i])
        print('Конституенты:' + to_string(constituents, formula_type))
        
    
        implicans = gluing_formulas(constituents, True)
        print('Импликанты:' + to_string(implicans,formula_type))
        
        
        tablica =calculation_tabular_method(constituents, implicans)
        print('Таблица:')
        string =''
        for constituent in constituents:
            string += to_string([constituent], formula_type).center(14)
        print('\t   '+'Конституенты'.center(len(string)))
        print('Импликанты'.ljust(11) + string)
        for i in range(len(implicans)):
            print(to_string([implicans[i]], formula_type).ljust(11), end = '')
            for j in range(len(tablica[i])):
                print(tablica[i][j].center(14), end = '')
            print('')
                  
        
        print('\nТНФ:')
        reduced = delete_unnecessary_implicant(tablica, implicans)
        print(to_string(reduced, formula_type))
        print('ТTНФ:' + to_string((gluing_formulas(reduced, False)),formula_type))
        
        print('\nТабличный метод:')
        constituents = convert_to_list_constituents(number)
        print('Конституенты:' + to_string(constituents, formula_type))
        tabl = table_method(constituents, formula_type) 
        print('График:')
        print ('\nA^', end = '')
        i = len(tabl)-1
        while i>= 0:
            print('\n' + str(i) + '|', end = ' ')
            for j in range(len(tabl[i])):
                print(tabl[i][j], end = '  ')
            i -=1
        print('\n  ------------->\n   00 01 11 10   BC')
        tupic = table_implicants(tabl)
        if formula_type == '/\\':
            for i in range(len(tupic)): 
                tupic[i] = truth_table.negation(tupic[i]) 
        print('\nТНФ:' + to_string(tupic, formula_type))
        print('ТTНФ:' + to_string((gluing_formulas(tupic, False)),formula_type))    
    
