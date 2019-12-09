# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
#            print('j',j,'arr[j]',arr[j])
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             



        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    print('it',arr)
    return arr
# print(selection_sort( [3,2,5,7,99,66,44,55,2]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) == 0:
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
#print(bubble_sort( [3,59,97,5,83,46,7,99,66,44,55,2]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr