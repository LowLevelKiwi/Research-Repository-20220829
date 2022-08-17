# this is requied so that the pivot can be picked randomly
from random import randint

# this defines the function so that it can be used elsewhere and within itself
def quick_sort(array):

  # this checks wether the incoming array has 0 -1 items and makes the function return the array
  if len(array) < 2 : return array

  # this is used to define some arrays that will be used later
  low,same,high = [],[],[]

  # this is used to get a random item in the array so that it can be used as a pivot,
  # it is chosen randomly as this will increase the chance that the chosen item will be the array median value,
  # as the median value is place randomly in the array as well
  # this also helps to reduce the worst case senario that ethier the lowest or highest item in the array is repeatedly selected
  pivot = array[randint(0, len(array) - 1)]

  # this loops through every item in the array and sorts the into three groups
  # Low: all the items that are lower than the selected pivot
  # Same: all items that have the same value as the pivot including the pivot
  # High all items higher than the pivot
  for item in array:
    if item < pivot: low.append(item)
    elif item == pivot: same.append(item)
    else : high.append(item)

  # this will repeatedly call itself until the function reachs the point where the childeren functions start returning an array with 0 - 1 items
  return quick_sort(low) + same + quick_sort(high)

  # This is a small diagram of the order of operations that the function/s go through
  #
  #                 1 first call
  #        2nd      |         9th
  #    3rd |   6th      10th  |   13th
  # 4th|5th 7th|8th  11th|12th 14th|15th
  