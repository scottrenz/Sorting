# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    if len(arr) < 2:
        return arr
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) < 2:
        return arr
    d = True
    while d:
        for i in range(1, len(arr) ):
            if i == 1:
                d = False
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                d = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if maximum < 0:
        maximum = max(arr) + 1
    else:
        maximum +=1    
    count =[]
    for i in range(0, maximum):
        count.append(-1)
    for key in arr:
        if key < 0:
            return "Error, negative numbers not allowed in Count Sort"    
        count[key] +=1
    arr = []
    for i in range(0, maximum):
        if count[i] != -1:
            for j in range(0, count[i] + 1):
                arr.append(i)
    return arr
