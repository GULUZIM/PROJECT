print('hello , vvedite svoe imya i operaciy')
name = input('enter yo0ur name : ')
oper = input('''Выберите оперцию : 
+ 
-
/
*
**
//
%
''')

a = float(input('первая цифра : '))
b = float(input('вторая цифра : '))

if oper == '+':
    c = a+b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} + {b} = {c}')
if oper == '-':
    c = a-b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} - {b} = {c}')
if oper == '/':
    c = a/b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} / {b} = {c}')
if oper == '*':
    c = a*b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} * {b} = {c}')
if oper == '//':
    c = a//b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} // {b} = {c}')
if oper == '%':
    c = a%b
    with open ('newtxt.txt', 'w') as file:
                    file.write (f'{name} сделал спрос на {a} % {b} = {c}')

