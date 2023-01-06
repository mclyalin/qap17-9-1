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

  if index:
    print(f'Искомый индекс равен: {index}')
  else:
    print('Искомый индекс не найден.')
