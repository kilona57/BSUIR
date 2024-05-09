arguments = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]
FOUR = 4
TWO = 2
THREE = 3
FIVE = 5

def substractor():
    one_for_binary = [0, 0, 0, 1]
    residual = []
    for i in range(len(arguments) - 1):
        copy_list = arguments[i].copy()
        residual.append(copy_list)
        
    i = THREE
    while i < len(arguments[0]):
        minus_one = 0
        j = THREE
        while j > -1:
            minuend = arguments[j][i] - minus_one
            minus_one = 0
            if minuend < one_for_binary[j]:
                minus_one = 1
            if abs(minuend) == one_for_binary[j]:
                residual[j][i] = 0
            else:
                residual[j][i] = 1
            j -= 1
        i += TWO
    return residual

def compare(residual):
    rezult = [[0 for column in range(len(arguments[0]))] for string in range(FOUR)]
    for i in range(len(rezult)):
        for j in range(len(rezult[0])):
            if residual[i][j] != arguments[i][j]:
                rezult[i][j] = 1
    return rezult

def numeric_form(truth_table):
    rez_num_form = []
    for i in range(len(truth_table)):
        lists = []
        for j in range(len(arguments)):
            lists.append(arguments[j][i])
        if truth_table[i] == 1:
            rez_num_form.append(index_form(lists))
    return rez_num_form

def index_form(truth_table):
    rez_index = 0
    for i in range(len(truth_table)):
        if truth_table[i] == 1:
            rez_index += TWO**(len(truth_table)-1-i)
    return rez_index

def convert_to_list_constituents(number_form):
    constituents = []
    for number in number_form:
        constituent_list = []
        power = FOUR
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

def to_string(formula):
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

        
        if formula[i][3] == 1:
            brackets.append('D')
        elif formula[i][3] == 0:
            brackets.append('!D')
                
        if formula[i][4] == 1:
            brackets.append('V')
        elif formula[i][4] == 0:
            brackets.append('!V')

        brackets = '/\\'.join(brackets)
        if len(brackets)>TWO:
            brackets = '(' + brackets + ')'

        list_of_brackets.append(brackets)

    return '\\/'.join(list_of_brackets)

print('\nA:  ' + ' '.join(str(el) for el in arguments[0]))
print('B:  ' + ' '.join(str(el) for el in arguments[1]))
print('C:  ' + ' '.join(str(el) for el in arguments[2]))
print('D:  ' + ' '.join(str(el) for el in arguments[3]))
print('\nV:  ' + ' '.join(str(el) for el in arguments[4]))

residual = substractor()
print('\nA1: ' + ' '.join(str(el) for el in residual[0]))
print('B1: ' + ' '.join(str(el) for el in residual[1]))
print('C1: ' + ' '.join(str(el) for el in residual[2]))
print('D1: ' + ' '.join(str(el) for el in residual[3]))

rezult = compare(residual)
print('\nh1: ' + ' '.join(str(el) for el in rezult[0]))
print('h2: ' + ' '.join(str(el) for el in rezult[1]))
print('h3: ' + ' '.join(str(el) for el in rezult[2]))
print('h4: ' + ' '.join(str(el) for el in rezult[3]))                    
            
sdnf_h1 = convert_to_list_constituents(numeric_form(rezult[0]))
print('\nСДНФ for h1:' + to_string(sdnf_h1))
print('ТДНФ for h1:' + to_string(total_gluing(sdnf_h1, FIVE)))
logism = to_string(total_gluing(sdnf_h1, FIVE)).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ h1 for logism:' + logism)

sdnf_h2 = convert_to_list_constituents(numeric_form(rezult[1]))
print('\nСДНФ for h2:' + to_string(sdnf_h2))
print('ТДНФ for h2:' + to_string(total_gluing(sdnf_h1, FIVE)))
logism = to_string(total_gluing(sdnf_h2, FIVE)).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ h2 for logism:' + logism)

sdnf_h3 = convert_to_list_constituents(numeric_form(rezult[2]))
print('\nСДНФ for h3:' + to_string(sdnf_h3))
print('ТДНФ for h3:' + to_string(total_gluing(sdnf_h3, FIVE)))
logism = to_string(total_gluing(sdnf_h3, FIVE)).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ h2 for logism:' + logism)

sdnf_h4 = convert_to_list_constituents(numeric_form(rezult[3]))
print('\nСДНФ for h4:' + to_string(sdnf_h4))
print('ТДНФ for h4:' + to_string(total_gluing(sdnf_h4, FIVE)))
logism = to_string(total_gluing(sdnf_h4, FIVE)).replace('!', '~')
logism = logism.replace('/\\', '&')
logism = logism.replace('\\/', '+')
print('ТДНФ h4 for logism:' + logism)