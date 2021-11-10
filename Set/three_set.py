# Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом регистр букв необходимо учитывать.
#
# Входные данные
# Программа получает на вход строку, состоящую из заглавных и строчных символов, цифр и знаков препинания.
#
# Выходные данные
# Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.
#
n = input() #на вход получаем строку
a = set(n) #заводим новое множество
for i in n: #циклом for обходим все элменты строки
    if i in a: #и если элемент встречается в a
        a.discard(i) #удаляем его из множества а
        print(i, end = '')
