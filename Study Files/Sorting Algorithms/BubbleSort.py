# this defines the function so that it can be used elsewhere
def bubble_sort(array): 

  # this gets the total length of the array so it can be looped through later
  array_length = len(array) 

  # this loops through for every item in the array
  for i in range(array_length): 

    # this is defined so that the function can exit itself early if the array is sorted 
    sorted = True

    # this loops through all the items that aren't "Sorted" yet
    for index in range(array_length - i - 1):

      # this checks if the item at the current index is higher than the one at the index above it
      if array[index] > array[index + 1]:

        # this flips the items at the index with the one just above it
        array[index], array[index + 1] = array[index + 1], array[index]

        # this is used so that the function will continue to loop through items
        sorted = False

    # this will only call if the array is sorted and is used to stop the for loop so that it doesnt make unnecessary repeats 
    if sorted: break

  # this will return the sorted array
  return array