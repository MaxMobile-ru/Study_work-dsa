# Выполнил: Ставецкий Максим Иванович
# 24-й вариант задания
'''
Структура: стек.
Проверка тегов HTML на корректность вложенности
(<div><p></p></div>).
'''
from my_stack import *

def process_string (i, value):
    entire = ''
    while value [i] != '>':
        entire += value [i]
        i += 1
    return entire + '>', i + 1

def check_stack (stack, entire):
    if entire [2:-1] == stack.peek () [1:-1]:
        stack.pop ()
        return stack, True
    else:
        return stack, False

test_value = '<div><p></p></div>'
correct_stack = True
stack01 = Stack ()
i = 0
while True:
    if i >= len (test_value) or i == -1:
        break
    if test_value [i] == '<':
        new_entire, i = process_string (i, test_value)
        if not ('/' in new_entire):
            stack01.push (new_entire)
            new_entire = ''
        elif '/' in new_entire:
            stack01, correct_stack = check_stack (stack01, new_entire)
            new_entire = ''
    else:
        i = test_value.find ('<', i, -1)
    if not correct_stack:
        break

if correct_stack:
    print ('Теги HTML вложены корректно.')
else:
    print ('Теги HTML вложены некорректно.')
