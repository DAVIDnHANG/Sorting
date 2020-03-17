# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    arrA_index=0
    arrB_index=0
    while(arrA_index < len(arrA) and arrB_index < len(arrB)):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index +=1
    merged_arr += arrA[arrA_index:]
    merged_arr += arrB[arrB_index:]
    return merged_arr
# TO-DO: implement the Merge Sort function below USING RECURSION
#split array in half, keep doing into len is one.
def merge_sort( arr ):

    if (len(arr) <= 1):
        return arr
    midpoint = len(arr) // 2

    left=merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])
    arr=merge(left,right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    if(len(arr) < 1):
        return arr

    return pass

#def merge_sort_in_place(arr, l, r):
    # TO-DO

#    return pass


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
#def timsort( arr ):

#    return pass
