#Декларативное программирование
#Задача 3: Вычисление факториала числа. 
#Напишите программу, которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
 
 
print(fac(7))