# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for v in range(0,len(arr)):
      if arr[v] == target:
          return v
  return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  mid = len(arr)//2

  # TO-DO: add missing code
  while len(arr):
    if arr[mid] == target:
      return mid
    if target < arr[mid]:
      mid = mid//2
    else:
      mid +=mid//2
  return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] == target:
    return middle
  if arr[middle] > target:
    high = middle
  else:
    low = middle
  return binary_search_recursive(arr,target,low,high)
