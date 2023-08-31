#Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(15))