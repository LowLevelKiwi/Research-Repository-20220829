# these import the required files so that i can create a random array and also use the quick and bubble sorts functions i defined in the other files in this folder
from random import randint
from BubbleSort import bubble_sort
from QuickSort import quick_sort


# this is used to check whether the array thats passed in is sorted or not
def check_sorted (array):

  # this is defined so that it can check later if its sorted
  array_sorted = True

  # this is defined so that it can say where the first unsorted index was in the array
  error_index = 0

  # this loops through every index in the array
  for index in range(0, len(array) -1):

    # this makes it skip the first item in the array
    if index > 0:

      # this compares the item in the array with the one before it and if the item before it is larger that itself the runs the inner code
      if array[index] < array[index - 1]:

        # this changes the array sorted to false, saves the unsorted items index the breaks the for loop so that there arnt unnecessary comparison
        array_sorted = False
        error_index = index
        break

  # this checks to see if there were any unsoreted items and returns the appropriate string so that it can be printed
  if array_sorted:
    return "Array Sorted"
  else:
    return "Array Unsorted, Error at Index: " + str(error_index)


# this generates a array with 100 random items with values between 0 - 1000
array = []
for x in range(0,100):
  array.append(randint(0,1000))

print(array) # this prints the array so that the user can see the begining array
print(check_sorted(array)) # this prints the result of if the begining array is already sorted, this is so that the user can know if the begining array isn't alrady sorted
print(check_sorted(bubble_sort(array))) # this prints the result of the check of weather the bubble sort actually sorted the begining array
print(check_sorted(quick_sort(array))) # this prints the result of the check of weather the Quick sort actually sorted the begining array