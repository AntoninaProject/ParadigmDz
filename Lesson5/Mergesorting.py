#Напишите программу, которая сортирует список чисел методом сортировки слиянием.

def merge_sort(list1, left_index, right_index): 
    if left_index >= right_index: 
        return 
 
    middle = (left_index + right_index)//2 
    merge_sort(list1, left_index, middle) 
    merge_sort(list1, middle + 1, right_index) 
    merge(list1, left_index, right_index, middle) 
 
 
    # Определение функции для объединения списка 
def merge(list1, left_index, right_index, middle): 
 
 
   # Создание подразделов списков 
    left_sublist = list1[left_index:middle + 1] 
    right_sublist = list1[middle+1:right_index+1] 
 
    # Начальные значения переменных, которые мы используем для сохранения 
    # отслеживаем, где мы находимся в каждом списке 1 
    left_sublist_index = 0 
    right_sublist_index = 0 
    sorted_index = left_index 
 
    # просматриваем обе копии до тех пор, пока у нас не закончится один элемент 
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist): 
 
        # Если наш left_sublist содержит меньший элемент, поместите его в отсортированный 
        # Взять часть, а затем переместитесь вперед в left_sublist (увеличив указатель) 
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]: 
            list1[sorted_index] = left_sublist[left_sublist_index] 
            left_sublist_index = left_sublist_index + 1 
        # В противном случае добавьте его в нужный подсписок
        else: 
            list1[sorted_index] = right_sublist[right_sublist_index] 
            right_sublist_index = right_sublist_index + 1 
 
 
        # продвигайтесь вперед по отсортированной части 
        sorted_index = sorted_index + 1 
 
      
    # мы пройдемся по оставшимся элементам и добавим их 
    while left_sublist_index < len(left_sublist): 
        list1[sorted_index] = left_sublist[left_sublist_index] 
        left_sublist_index = left_sublist_index + 1 
        sorted_index = sorted_index + 1 
 
    while right_sublist_index < len(right_sublist): 
        list1[sorted_index] = right_sublist[right_sublist_index] 
        right_sublist_index = right_sublist_index + 1 
        sorted_index = sorted_index + 1 
 
list1 = [44, 65, 2, 3, 58, 14, 57, 23, 10, 1, 7, 74, 48] 
merge_sort(list1, 0, len(list1) -1) 
print(list1)