#Функция-редуктор: 
#Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список чисел, 
# а затем возвращает произведение всех чисел в списке. 
#Используйте эту функцию для вычисления произведения чисел в списке.

def f(a):
	d = 1
	i = 0
	while i<len(a):
		d = int(a[i]) * d
		i += 1
	return d

a = list(input())
print(f(a))