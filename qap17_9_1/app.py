from utils import validate, sort, binary_search
from extensions import UserInputException

user_str = input('Введите последовательность целых чисел через пробел: ')
user_num = input('Введите любое целое число: ')

try:
  items, num = validate(user_str, user_num)
except UserInputException as e:
  print(f'Ошибка ввода.\n{e}')
else:
  sorted = sort(items)
  index = binary_search(sorted, num, 0, len(sorted) - 1)

  if not index:
    print('Искомый индекс не найден.')
  else:
    print(f'Искомый индекс равен: {index}')

# 1 2 d 4 56 78
# 23 -45 43 0.5 34
# 1 2 3 -4 5 7 54