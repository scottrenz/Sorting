# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    while arrA != [] and arrB != []:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            if len(arrA) == 1:
                arrA = []
            else:    
                arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            if len(arrB) == 1:
                arrB = []
            else:    
                arrB = arrB[1:]
    while arrA != []:
        merged_arr.append(arrA[0])
        if len(arrA) == 1:
            arrA = []
        else:    
            arrA = arrA[1:]
    while arrB != []:
        merged_arr.append(arrB[0])
        if len(arrB) == 1:
            arrB = []
        else:    
            arrB = arrB[1:]
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    left = merge_sort(left)
    right =merge_sort(right)
    arr = merge(left,right)
    return arr
print(merge_sort([99,8,3,88,1,0,4,5,7,43,9,2]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
