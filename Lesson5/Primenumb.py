#Напишите программу, которая находит все простые числа в заданном диапазоне.

lower_value = int(input("Пожалуйста, введите наименьшее значение диапазона: ")) 
upper_value = int(input("Пожалуйста, введите наибольшее значение диапазона: ")) 
 
print("Простыми числами в этом диапазоне являются: ") 
for number in range(lower_value, upper_value + 1): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number) 