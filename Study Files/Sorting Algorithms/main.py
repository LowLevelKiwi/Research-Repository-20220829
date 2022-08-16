from random import randint
from BubbleSort import bubble_sort
from QuickSort import quick_sort

def check_sorted (array):
  array_sorted = True
  error_index = 0
  for index in range(0, len(array) -1):
    if index > 0:
      if array[index] < array[index - 1]:
        array_sorted = False
        error_index = index
        break

  if array_sorted:
    return "Array Sorted"
  else:
    return "Array Unsorted, Error at Index: " + str(error_index)

array = []
for x in range(0,100):
  array.append(randint(0,1000))

print(array)
print(check_sorted(array))
print(check_sorted(bubble_sort(array)))
print(check_sorted(quick_sort(array)))