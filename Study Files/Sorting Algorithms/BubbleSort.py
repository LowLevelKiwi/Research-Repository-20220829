def bubble_sort(array):
  array_length = len(array)
  for i in range(array_length):
    sorted = True
    for index in range(array_length - i - 1):
      if array[index] > array[index + 1]:
        array[index], array[index + 1] = array[index + 1], array[index]
        sorted = False

    if sorted: break

  return array