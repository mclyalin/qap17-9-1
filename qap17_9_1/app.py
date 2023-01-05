def sort(items):
  sorted = items.copy()
  for i in range(1, len(sorted)):
    x = sorted[i]
    idx = i
    while idx > 0 and sorted[idx-1] > x:
        sorted[idx] = sorted[idx-1]
        idx -= 1
    sorted[idx] = x
  return sorted

def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находимо середину
    if (array[middle] < element) and (array[middle + 1] >= element): # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)

# element = int(input())
# array = [i for i in range(1,100)] # 1,2,3,4,...

# str = input('Введите последовательность целых чисел через пробел:\n')
# num = int(input('Введите любое целое число: '))

# items = [int(item) for item in str.split(' ')]
# sorted = sort(items)

array = [2, 3, 1, 4, 6, 9, 8, 7]
num = 5
sorted = sort(array)
print(sorted)

# запускаем алгоритм на левой и правой границе
print(binary_search(sorted, num, sorted[0], sorted[-1]))