#Рекурсивная сумма: Напишите рекурсивную функцию, которая вычисляет сумму всех чисел от 1 до n. 
#Например, для n = 5 результат должен быть 1 + 2 + 3 + 4 + 5 = 15.

#sum_numbers(5) ➞ 15 
#// 1 + 2 + 3 + 4 + 5 = 15 
#sum_numbers(1) ➞ 1 
#sum_numbers(12) ➞ 78

def sum_numbers(n):
     if n == 1:
         return 1
     return n + sum_numbers(n-1)