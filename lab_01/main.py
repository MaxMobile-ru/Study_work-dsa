# Выполнил: Ставецкий Максим Иванович
# 24-й вариант задания
'''
Структура: стек.
Проверка тегов HTML на корректность вложенности
(<div><p></p></div>).
'''
import my_stack

test_st = Stack ()
test_st.push ('hello!')
test_st.push ('goodbye!')
print (test_st.peek ())
