from extensions import UserInputException

def validate(user_str, user_num):
  try:
    items = [int(item) for item in user_str.split(' ')]
  except ValueError:
    raise UserInputException(f'Невозможно обработать последовательность: {user_str}')

  try:
    num = int(user_num)
  except ValueError:
    raise UserInputException(f'Невозможно обработать число: {user_num}')

  return items, num

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
    if left > right:
        return False

    middle = (right+left) // 2
    if (array[middle] < element) and (array[middle + 1] >= element):
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)
