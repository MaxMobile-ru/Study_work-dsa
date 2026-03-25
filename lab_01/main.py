# Выполнил: Ставецкий Максим Иванович
# 24-й вариант задания
'''
Структура: стек.
Проверка тегов HTML на корректность вложенности
(<div><p></p></div>).
'''
from my_stack import *

test_value = '<div><p></p></div>'
correct_stack = True
stack01 = Stack ()
new_entire = ''
for i in range (len (test_value)):
    if test_value [i] == '<':
        new_entire += test_value [i]
    elif test_value [i] == '>':
        new_entire += test_value [i]
        if '/' in new_entire:
            if new_entire [2:-1] == stack01.peek () [1:-1]:
                stack01.pop ()
            else:
                
        stack01.push (new_entire)
        new_entire = ''
    elif len (new_entire) != 0:
        new_entire += test_value [i]

print (stack01.items)
