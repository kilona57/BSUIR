arguments = {"A":[0, 0, 0, 0, 1, 1, 1, 1], "B":[0, 0, 1, 1, 0, 0, 1, 1], "C":[0, 1, 0, 1, 0, 1, 0, 1]}
TWO = 2
THREE = 3
FOUR = 4

def to_string(formula, arguments_number):
    list_of_brackets = []
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

        if arguments_number == FOUR:
            if formula[i][3] == 1:
                brackets.append('D')
            elif formula[i][3] == 0:
                brackets.append('!D')

        brackets = '/\\'.join(brackets)
        if len(brackets)>TWO:
            brackets = '(' + brackets + ')'

        list_of_brackets.append(brackets)

    return '\\/'.join(list_of_brackets)

def substractor_table():
    b = []
    d = []
    for i in range(len(arguments['A'])):
        minuend = arguments['A'][i] - arguments['C'][i]
        if minuend >= arguments['B'][i]:
            b.append(0)
        else:
            b.append(1)
        if abs(minuend) == arguments['B'][i]:
            d.append(0)
        else:
            d.append(1)
    return d,b

def numeric_form(truth_table, arguments_number):
    rez_num_form = []
    if arguments_number == FOUR:
        arguments = {"A":[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], "B":[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], "C":[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], "D":[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    else:
        arguments = {"A":[0, 0, 0, 0, 1, 1, 1, 1], "B":[0, 0, 1, 1, 0, 0, 1, 1], "C":[0, 1, 0, 1, 0, 1, 0, 1]}
    for i in range(len(truth_table)):
        lists = [arguments["A"][i], arguments["B"][i],arguments["C"][i]]
        if arguments_number == FOUR:
            lists.append(arguments["D"][i])
        if truth_table[i] == 1:
            rez_num_form.append(index_form(lists))
    return rez_num_form

def index_form(truth_table):
    rez_index = 0
    for i in range(len(truth_table)):
        if truth_table[i] == 1:
            rez_index += TWO**(len(truth_table)-1-i)
    return rez_index

def convert_to_list_constituents(number_form, arguments_number):
    constituents = []
    for number in number_form:
        constituent_list = []
        if arguments_number == FOUR:
            power = FOUR-1
        else:
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

def number_of_arguments_in_brackets(brackets):
    number = 0
    for i in range(len(brackets)):
        if brackets[i] != -1:
            number += 1 
    return number
        

def total_gluing(formula, number_of_arguments):
    i = number_of_arguments
    while i > 1:
        formula = gluing_formulas(formula, i)
        i -= 1
    return formula       

def identical_find(implicant, implicants):
    for other in implicants:
        if implicant == other: 
            return True
    return False

def gluing_formulas(constituents, arguments_number):
    implicants = []
    first_bracket_index = 0
    i = 0
    for i in range(len(constituents)):
        if number_of_arguments_in_brackets(constituents[i]) == arguments_number:
            first_bracket_index = i
            break
           
    mas = [False for i in range(len(constituents))]
    for i in range(first_bracket_index, len(constituents)): #текущая
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
            implicants.insert(0, constituents[i])
    return implicants

def plus_four():
    number_of_arguments = FOUR
    four_in_binary_system = [0, 1, 0, 0]
    four_in_decimal_system = FOUR
    arguments = {1:[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 2:[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], 3:[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 4:[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    rezult = [[0 for column in range(len(arguments[1]))] for string in range(number_of_arguments)]
    for i in range(len(arguments[1]) - four_in_decimal_system):
        index = number_of_arguments
        plus_one = 0
        while index > 0 :
            summa = arguments[index][i] + four_in_binary_system[index - 1] + plus_one
            plus_one = 0
            if summa >= TWO:
                summa -= 2
                plus_one = 1
            rezult[index - 1][i] = summa
            index -= 1
    return rezult
        
         
    

print('Задание 1.')
d,b = substractor_table()
print('A: ' + ' '.join(str(el) for el in arguments['A']))
print('B: ' + ' '.join(str(el) for el in arguments['B']))
print('C: ' + ' '.join(str(el) for el in arguments['C']))
print('d: ' + ' '.join(str(el) for el in d))
print('b: ' + ' '.join(str(el) for el in b))

sdnf_d = convert_to_list_constituents(numeric_form(d, THREE), THREE)
print('\nСДНФ for d:' + to_string(sdnf_d, THREE))
print('ТДНФ for d:' + to_string(total_gluing(sdnf_d, THREE), THREE))
logism = to_string(total_gluing(sdnf_d, THREE), THREE).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ d for logism:' + logism)

sdnf_b = convert_to_list_constituents(numeric_form(b, THREE), THREE)
print('\nСДНФ for b:' + to_string(sdnf_b, THREE))
print('ТДНФ for b:' + to_string(total_gluing(sdnf_b, THREE), THREE))
logism = to_string(total_gluing(sdnf_b, THREE), THREE).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ b for logism:' + logism)


plus = plus_four()
arguments = {1:[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 2:[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], 3:[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 4:[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
print('\nЗадание 2.')
print('A:  ' + ' '.join(str(el) for el in arguments[1]))
print('B:  ' + ' '.join(str(el) for el in arguments[2]))
print('C:  ' + ' '.join(str(el) for el in arguments[3]))
print('D:  ' + ' '.join(str(el) for el in arguments[4]))
print('--------------------------------------------------------------->')
print('A1: ' + ' '.join(str(el) for el in plus[0]))
print('B1: ' + ' '.join(str(el) for el in plus[1]))
print('C1: ' + ' '.join(str(el) for el in plus[2]))
print('D1: ' + ' '.join(str(el) for el in plus[3]))

print('\nАргумент 1:')
sdnf_A = convert_to_list_constituents(numeric_form(plus[0], FOUR), FOUR)
print('СДНФ:' + to_string(sdnf_A, FOUR))
print('ТДНФ:' + to_string(total_gluing(sdnf_A, FOUR), FOUR))
logism = to_string(total_gluing(sdnf_A, FOUR), FOUR).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ for logism:' + logism)

print('\nАргумент 2:')
sdnf_B = convert_to_list_constituents(numeric_form(plus[1], FOUR), FOUR)
print('СДНФ:' + to_string(sdnf_B, FOUR))
print('ТДНФ:' + to_string(total_gluing(sdnf_B, FOUR), FOUR))
logism = to_string(total_gluing(sdnf_B, FOUR), FOUR).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ for logism:' + logism)

print('\nАргумент 3:')
sdnf_C = convert_to_list_constituents(numeric_form(plus[2], FOUR), FOUR)
print('СДНФ:' + to_string(sdnf_C, FOUR))
print('ТДНФ:' + to_string(total_gluing(sdnf_C, FOUR), FOUR))
logism = to_string(total_gluing(sdnf_C, FOUR), FOUR).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ for logism:' + logism)

print('\nАргумент 4:')
sdnf_D = convert_to_list_constituents(numeric_form(plus[3], FOUR), FOUR)
print('СДНФ:' + to_string(sdnf_D, FOUR))
print('ТДНФ:' + to_string(total_gluing(sdnf_D, FOUR), FOUR))
logism = to_string(total_gluing(sdnf_D, FOUR), FOUR).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ for logism:' + logism)
