# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
# Задано единственное целое число N
3 Нtобходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.

chi = int(input())
a = 1
while a**2 <= chi :
    print(a**2)
    a = a + 1
