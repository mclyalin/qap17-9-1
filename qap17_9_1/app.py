from utils import sort, binary_search

str = input('Введите последовательность целых чисел через пробел:\n')
num = int(input('Введите любое целое число: '))

items = [int(item) for item in str.split(' ')]
sorted = sort(items)
index = binary_search(sorted, num, 0, len(sorted) - 1)

if not index:
  print('Искомый индекс не найден.')
else:
  print(f'Искомый индекс равен: {index}')