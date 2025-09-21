
#спеисок
all_operators = ['+', '-', '*', '/', '//', '%', '**',
                '==', '!=', '>', '<', '>=', '<=',
                'and', 'or', 'not',
                '&', '|', '^', '~', '<<', '>>',
                'in', 'not in',
                'is', 'is not'
                 ]
print()
a = input("Введите первое число или строку: ")
print(all_operators)
operator = input("Введите оператор: ")
b = input("Введите второе число или строку : ")



if operator not in ['in', 'not in', 'is', 'is not']:
    num1 = int(a)
    num2 = int(b)
else: 
    str1 = str(a)
    str2 = str(b)



#код для арифметических операторов
if operator == "+":
    result = num1 + num2
    print("Результат: ", result)
elif operator == "-":
    result = num1 - num2
    print("Результат:", result)
elif operator == "*":
    result = num1 * num2
    print("Результат:", result)
elif operator == "/":
    if num2 == 0:
        print("делить на ноль нельзя  ")
    else:
        result = num1 / num2
        print("Результат: ", result)
elif operator == "//":
    if num2 == 0:
        print("делить на ноль нельзя ") 
    else:
        result = num1 // num2
        print("Результат: ", result)
elif operator == "%":
    if num2 == 0:
        print("делить на ноль нельзя ")
    else:
        result = num1 % num2
        print("Результат:", result)
elif operator == "**":
    result = num1 ** num2
    print("Результат: ", result)



#далее сделано для операторов сравнения
elif operator == "==":
    result = num1 == num2
    print("Результат: ", result)
elif operator == "!=":
    result = num1 != num2
    print("Результат: ", result)
elif operator == ">":
    result = num1 > num2
    print("Результат: ", result)
elif operator == "<":
    result = num1 < num2
    print("Результат: ",result)
elif operator == ">=":
    result = num1 >= num2
    print("Результат: ",result)
elif operator == "<=":
    result = num1 <= num2
    print("Результат: ",result)



#логические операторы
elif operator == 'and':
        bool1 = (num1 != 0)
        bool2 = (num2 != 0)
        result = bool1 and bool2
        print("Результат:", result)
elif operator == 'or':
        bool1 = (num1 != 0)
        bool2 = (num2 != 0)
        result = bool1 or bool2
        print("Результат:", result)
#для оператора Not Требуется одно число, следовтательно:
elif operator == 'not':
    num3 = int(input("Введите число для оператора not: "))
    if num3 == 0:
        result = True
    else: 
        result = False
    print("Результат :", result)



#побитовые операторы
elif operator == '&':
        result = num1 & num2
        print("результат:", result)
elif operator == '|':
        result = num1 | num2
        print("результат: ", result)
elif operator == '^':
        result = num1 ^ num2
        print("Результат:", result)
elif operator == '<<':
        result = num1 << num2
        print("Результат:", result)
elif operator == '>>':
        result = num1 >> num2
        print("результат:", result)




#операторы принадлежности
elif operator == 'in':
        result = str1 in str2
        print(str1, "находится в ", str2)
        
elif operator == 'not in':
        result = str1 not in str2
        print(str1, "не находится в ", str2 )




#операторы тождественности
elif operator == 'is':
        result = str1 == str2
        print("Результат", result)
        
elif operator == 'is not':
        result = str1 != str2
        print("Результат:", result)


else:
    print("Неизвестный оператор!")