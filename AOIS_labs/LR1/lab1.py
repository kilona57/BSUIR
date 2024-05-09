SEVEN = 7
TWO =2
ONE_TWENTY_SEVEN =127
TWENTY_THREE = 23
THIRTY_FIVE = 35
EIGHT = 8
def to_binary_system(number):
    arr = []
    while number > 0:
        arr.insert(0, int(number%TWO))
        number = number//TWO
    return arr

def convert_to_binary_system(arr, sign):
    while len(arr) < SEVEN:
        arr.insert(0, 0)
    if sign == '-':
        arr.insert(0, 1)
    else:
        arr.insert(0, 0)
    return  arr  

def reverse_code(arr):
    for i in range(1, len(arr)):
        if arr[i] == 0:
            arr[i] = 1 
        else: arr[i] = 0
    return arr

def summa(arr, mas, plus_one):
    i = len(arr) - 1
    sum = []
    while i > -1:
        if arr[i] + mas[i] < TWO:
            sum.insert(0, arr[i] + mas[i])
        else:
            sum.insert(0, arr[i] + mas[i] - TWO)
            if i > 0:
                arr[i-1] += 1
            elif plus_one:
                one = [0 for i in range(len(arr) - 1)]
                one.append(1)
                sum = summa(sum, one, False)
        i -= 1
    return sum
           

def additional_code(arr):
    mas = [0 for i in range(len(arr) - 1)]
    mas.append(1)
    arr = summa(mas, arr, False)
    return arr

def convert_to_decimal_code(arr):
    decimal_number = 0
    for i in range(len(arr)):
        decimal_number += (TWO**(len(arr) - i-1))*arr[i]
    return decimal_number

def from_direct_to_decimal(arr):
    sign = arr[0]
    arr.pop(0)
    number = convert_to_decimal_code(arr)
    if sign == 1:
        number = -number
    return number

def from_fractional(int_section, fract_section):
    number = convert_to_decimal_code(int_section)
    number += convert_to_decimal_code(fract_section)/2**35
    return number
    

def shift(arr):
    arr.pop(0)
    arr.append(0)
    return arr

def not_smaller(arr_1, arr_2):
    i = 0
    arr = arr_2.copy()
    if len(arr_1) < len(arr_2):
        return False
    while len(arr_1) > len(arr):
        arr.insert(0,0)
    while i < len(arr_1):
        if arr_1[i] > arr[i]:
            return True
        elif arr_1[i] == arr[i]:
            i +=1
        else:
            return False
    return True
         

def multiply(arr_1, arr_2):
    mas = [0 for i in range(len(arr_1) + len(arr_2))]
    i = len(arr_2)-1
    arr = arr_1.copy()
    while len(arr) != len(mas):
        arr.insert(0,0)
    while i > -1:
        if arr_2[i] == 1:
            mas = summa(arr, mas, False)
        arr = shift(arr) 
        i -=1 
    return mas

def reduction(arr_1, arr_2):
    arr1 = arr_1.copy()
    arr2 = arr_2.copy()
    while len(arr2) < len(arr1):
        arr2.insert(0,0)
    arr1.insert(0,0)
    arr2.insert(0,1)
    arr2 = additional_code(reverse_code(arr2))
    result = summa(arr1 , arr2,False)
    result.pop(0)
    return result

def fraction_section(arr_1, arr_2):
    fract_section = []
    for i in range(THIRTY_FIVE):
        arr_1.append(0)
        if not_smaller(arr_1, arr_2):
            fract_section.append(1)
            arr_1 = reduction(arr_1, arr_2)
        else:
            fract_section.append(0)
    return fract_section
    

def devision(arr_1, arr_2):
    if len(arr_1) >= len(arr_2) and not_smaller(arr_1, arr_2):
        count = 1
        while len(arr_1) > len(arr_2):
            arr_2.append(0)
            count += 1
        int_section = []
        for i in  range(count):
            if not_smaller(arr_1, arr_2):
                int_section.append(1)
                arr_1 = reduction(arr_1, arr_2)
            else:
                int_section.append(0)
            if i != count - 1:
                arr_2.pop(-1)
    else: int_section = [0]
    fraction_sec = fraction_section(arr_1, arr_2)
    return int_section, fraction_sec

def to_floating_point(number):
    if number < 0:
        sign = [1] 
        number = -number
    else:
        sign = [0]
            
    int_number = number//1
    fraction_number = number - int_number
    mantica = to_binary_system(int_number)
    two_in_power = 0.5    
    if len(mantica) > 0:
        exponenta = len(mantica)-1
        mantica.pop(0)
    else:
        exponenta = -1
        while fraction_number < two_in_power:
            exponenta -= 1
            two_in_power = two_in_power / TWO
        fraction_number -= two_in_power  
        two_in_power = two_in_power / TWO  
    while len(mantica) < TWENTY_THREE:
        if fraction_number >= two_in_power:
            mantica.append(1)
            fraction_number -= two_in_power
        else:
            mantica.append(0)
        two_in_power = two_in_power / TWO
    exponenta = to_binary_system(exponenta+ONE_TWENTY_SEVEN)
    while len(exponenta) < EIGHT:
        exponenta.insert(0,0)
    floating_number = sign + exponenta + mantica
    return floating_number  

def get_exponenta(floating_number):
    exponenta = []
    for i in range(1,9):
        exponenta.append(floating_number[i])
    return  exponenta
def get_mantica(floating_number):
    mantica = []
    for i in range(9,32):
        mantica.append(floating_number[i])
    return  mantica

def from_floating_to_decimal(floating_number):
    exponenta = convert_to_decimal_code(get_exponenta(floating_number))-ONE_TWENTY_SEVEN
    mantica = convert_to_decimal_code(get_mantica(floating_number))
    number = (2**exponenta)*(1+mantica/2**23)
    if floating_number[0] == 1:
        number = -number
    return number 

def summa_of_floating_number(num_1, num_2):
    deffernce = convert_to_decimal_code(get_exponenta(num_1)) - convert_to_decimal_code(get_exponenta(num_2))
    mantica_1 = [0,1]+get_mantica(num_1)
    mantica_2 = [0,1]+get_mantica(num_2)
    exponenta = get_exponenta(num_1)
    for i in range(deffernce):
        mantica_2.insert(0,0)
        mantica_2.pop(-1)
    mantica = summa(mantica_1, mantica_2,False)
    if mantica[0] == 1:
        exponenta = to_binary_system(convert_to_decimal_code(exponenta) + 1)
        while len(exponenta) < 8:
            exponenta.insert(0,0)        
        mantica.pop(-1)
    else:
        mantica.pop(0) 
    mantica.pop(0)
    
    return [0] + exponenta + mantica          
        
        
    
    
      


while True:  
    opt = input('\nВыберите операцию:\n+ - сложение\nx - умножение\n/ - деление\n& - сложение с плавающей точкой\n')
    match opt:
        case '+':
            print('\nВведите первое число:')
            num_1 = int(input())
            print('Введите второе число:')
            num_2 = int(input())
            if num_1<=0:
                sign_num_1 = '-'
                num_1 = - num_1
            else:
                sign_num_1 = '+'
                
            if num_2<=0:
                sign_num_2 = '-'
                num_2 = - num_2
            else:
                sign_num_2 = '+'
            a = to_binary_system(num_1)
            b = to_binary_system(num_2)
            
                    
            a = convert_to_binary_system(a, sign_num_1)
            b = convert_to_binary_system(b, sign_num_2)
            if num_1 <= 0 and num_2 <= 0:
                a = additional_code(a)
                b = additional_code(b)
                sum = summa(a, b, False)
                sum = additional_code(sum)
            else:
                if sign_num_1 == '-':
                    a = reverse_code(a)
                if sign_num_2 == '-':
                    b = reverse_code(b)
                sum = summa(a,b,True)
                if sum[0] == 1:
                    sum = reverse_code(sum)
            print('\nОтвет:')
            print('1) Двочная система счисления')
            print(sum)
            print('\n2) Десятичная система счисления')
            print(from_direct_to_decimal(sum))
        
        case 'x':    
            print('\nВведите первое число:')
            num_1 = int(input())
            print('Введите второе число:')
            num_2 = int(input())
            sign = 0
            if num_1<=0:
                sign += 1 
                num_1 = - num_1
            else:
                sign_num_1 = '+'
                
            if num_2<=0:
                sign += 1                
                num_2 = - num_2
            else:
                sign_num_2 = '+'
            a = to_binary_system(num_1)
            b = to_binary_system(num_2)
            
            rezult = multiply(a, b)
            print('\nОтвет:')
            print('1) Двочная система счисления')
            print (rezult)
            rezult = convert_to_decimal_code(rezult) 
            if sign == 1:
                rezult = - rezult 
            print('\n2) Десятичная система счисления')    
            print(rezult)
        
        case '/': 
            print('\nВведите первое число:')
            num_1 = int(input())
            print('Введите второе число:')
            num_2 = int(input())
            sign = 0
            if num_1<=0:
                sign += 1 
                num_1 = - num_1
            else:
                sign_num_1 = '+'
                
            if num_2<=0:
                sign += 1                
                num_2 = - num_2
            else:
                sign_num_2 = '+'
            a = to_binary_system(num_1)
            b = to_binary_system(num_2)
            
            int_rezult, fract_rezult = devision(a,b)
            print('\nОтвет:')
            print('1) Двочная система счисления')
            print('\nЦелая часть числа:')
            print(int_rezult)
            print('\nЧисло после запятой:')
            print(fract_rezult)
            rezult = from_fractional(int_rezult, fract_rezult)
            if sign == 1:
                rezult = - rezult 
            print('\n2) Десятичная система счисления')       
            print(round(rezult, 5))
        
        case '&':    
            print('\nВведите первое число:')
            num_1 = float(input())
            print('Введите второе число:')
            num_2 = float(input())
            if num_1 > num_2:
                bigger_number = num_1
                smaller_number = num_2
            else:
                bigger_number = num_2
                smaller_number = num_1
            bigger_number = to_floating_point(bigger_number)
            smaller_number = to_floating_point(smaller_number)
            print('\nОтвет:')
            print('1) Двочная система счисления')
            print('\nБольшее число:')
            print(bigger_number) 
            print('\nМеньшее число:')
            print(smaller_number)
            
            summ = summa_of_floating_number(bigger_number, smaller_number)
            print('\nРезультат:')
            print(summ)
            print('\n2) Десятичная система счисления')  
            print(from_floating_to_decimal(summ))
            
            
                
            
       