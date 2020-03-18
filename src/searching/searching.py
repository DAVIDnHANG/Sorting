# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  length = len(arr)
  for i in range(0,length):
    if(arr[i] == target):
      return i
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
#compare target with middle of array
#if target < then middle value, then start at index 0
#elif target > then middle value, then start middle of value.
#use linear search above
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  # TO-DO: add missing code
  #check mid
  while(low <= high):
    mid = low + (high - low) //2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid+1
    else:
      high = mid-1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if low <= high:
    mid = low + (high-low) // 2
    if (arr[mid] == target):
      return mid
    elif arr[mid] > target:
      return binary_search_recursive(arr, target, low, mid-1)
    else:
      return binary_search_recursive(arr, target, mid+1, high)
  else:
    return -1