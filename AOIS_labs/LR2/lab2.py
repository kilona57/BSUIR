args= 3
argument = {"A":[0, 0, 0, 0, 1, 1, 1, 1], "B":[0, 0, 1, 1, 0, 0, 1, 1], "C":[0, 1, 0, 1, 0, 1, 0, 1]}
TWO = 2
FOUR = 4

def lengh(formula):
    brackets = 1
    len_form = 0
    while brackets > 0:
        if formula[len_form] == "(":
            brackets += 1
        elif formula[len_form] == ")":
            brackets -= 1
        len_form += 1
    return len_form -1

def negation(formula):
    rez_neg = []
    for i in range(len(formula)):
        if formula[i] == 0: 
            rez_neg.append(1)
        else:
            rez_neg.append(0)
    return rez_neg

def conjunction(formula_1, formula_2):
    rez_conjunct = []
    for i in range(len(formula_1)):
        if formula_1[i] == 1 and formula_2[i] == 1:
            rez_conjunct.append(1)
        else:
            rez_conjunct.append(0)
    return rez_conjunct
            
def disjunction(formula_1, formula_2):
    rez_disjunct = []
    for i in range(len(formula_1)):
        if formula_1[i] == 0 and formula_2[i] == 0:
            rez_disjunct.append(0)
        else: 
            rez_disjunct.append(1)
    return rez_disjunct        

def implication(formula_1, formula_2):
    rez_implicat = []
    for i in range(len(formula_1)):
        if formula_1[i] == 1 and formula_2[i] == 0:
            rez_implicat.append(0)
        else:
            rez_implicat.append(1)
    return rez_implicat

def equivalence(formula_1, formula_2):
    rez_euival = []
    for i in range(len(formula_1)):
        if formula_1[i] == formula_2[i]:
            rez_euival.append(1)
        else: 
            rez_euival.append(0)
    return rez_euival

def operation(formula_1, formula_2, operator):
    if operator == "/\\" or operator == "*":
        result = conjunction(formula_1, formula_2)
    elif operator == "\\/" or operator == "+":
        result = disjunction(formula_1, formula_2)
    elif operator == "->":
        result = implication(formula_1, formula_2)
    elif operator == "~":
        result = equivalence(formula_1, formula_2)
    return result

def truth_table(formula):
    mas = []
    i = 0
    
    while i < len(formula):
        if formula[i] == "(":
            i+=1 
            mas.append(truth_table(formula[i:i+lengh(formula[i:])]))
            i+=lengh(formula[i:])
        elif formula[i] == "!":
            if formula[i+1].isalpha():
                i+=1
                mas.append(negation(argument[formula[i]]))
            else:
                i+=TWO
                mas.append(negation(truth_table(formula[i:i+lengh(formula[i:])])))
                i+=lengh(formula[i:])
        elif formula[i].isalpha():
            mas.append(argument[formula[i]])
        elif formula[i] == "~" or formula[i] == "+" or formula[i] == "*":
            operator = formula[i]
        else: 
            operator = formula[i: i+TWO]
            i+=1

        if len(mas) == TWO:
            mas[0] = operation(mas[0], mas[1], operator)
            mas.pop(1)
        i+=1
    return mas[0]

def index_form(truth_table):
    rez_index = 0
    for i in range(len(truth_table)):
        if truth_table[i] == 1:
            rez_index += TWO**(len(truth_table)-1-i)
    return rez_index

def numeric_form(truth_table, type_on_function):
    rez_num_form = []
    if type_on_function == "/\\":
        constituent = 0
    else: constituent = 1
            
    for i in range(len(truth_table)):
        if truth_table[i] == constituent:
            rez_num_form.append(index_form([argument["A"][i], argument["B"][i],argument["C"][i]]))
    return rez_num_form

def string_form(numeric_form, type_of_function):
    rez_string_form = ""
    if type_of_function == "/\\":
        inside = '\\/'
        outside = '/\\'
        one = "!"
        zero = ""
    else: 
        inside = '/\\'
        outside = '\\/'
        one = ""
        zero = "!"
    for i in range(len(numeric_form)):
        rez_string_form = rez_string_form + "("
        if numeric_form[i]>=FOUR:
            rez_string_form = rez_string_form + one
            numeric_form[i] -= FOUR
        else: rez_string_form += zero
        rez_string_form = rez_string_form + "A"
        rez_string_form = rez_string_form + inside
        if numeric_form[i]>=TWO:
            rez_string_form = rez_string_form + one
            numeric_form[i] -= TWO
        else: rez_string_form += zero
        rez_string_form = rez_string_form + "B"
        rez_string_form = rez_string_form + inside
        if numeric_form[i]>=1:
            rez_string_form = rez_string_form + one
        else: rez_string_form += zero
        rez_string_form = rez_string_form + "C"
        rez_string_form = rez_string_form + ")"
        rez_string_form = rez_string_form + outside
    rez_string_form = rez_string_form[:len(rez_string_form)-TWO]
    return rez_string_form

formula = input("Введите выражение: ")
result = truth_table(formula)
print('\nТаблица истинности:')
print('A:  ' + '  '.join(str(el) for el in argument['A']))
print('B:  ' + '  '.join(str(el) for el in argument['B']))
print('C:  ' + '  '.join(str(el) for el in argument['C']))
print('F:  ' + '  '.join(str(el) for el in result))
print('\nИндексная форма: ' + str(index_form(result)))
print('\nЧисловая форма: /\\(' + ', '.join(str(el) for el in numeric_form(result, '/\\')) + ')'  + '\nСКНФ:' + string_form(numeric_form(result, '/\\'), '/\\'))
print('\nЧисловая форма: \\/(' + ', '.join(str(el) for el in numeric_form(result, '\\/')) + ')'  + '\nСДНФ:' + string_form(numeric_form(result, '\\/'), '\\/'))


        
            
        
            
                
        
            
                

    

            
    
        

