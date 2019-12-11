import sys
#sys.setrecursionlimit(3000)
#print(sys.getrecursionlimit())
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
#print(merge_sort([99,8,3,88,1,0,4,5,7,43,9,2]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start +=1
        else:
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                index -=1
            arr[start] = value
            start +=1
            mid +=1
            start2 +=1

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l < r:
        # m = (l + r) // 2
        m = ( l + (r -1) )// 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr
# print(merge_sort_in_place([99,8,9,1,2], 0, 4))
# print(merge_sort_in_place([99,8,3,88,1,0,4,5,7,43,9,2], 0, 11))
# print(merge_sort_in_place(['xz','ax','d','tree','m'], 0, 4))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
