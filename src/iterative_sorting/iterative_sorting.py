# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            #check if ith is smallest, if not reassign jth to smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        #use a temp variable to assign the VALUE
        temp = arr[cur_index]
        #whatever index we are on will be replace to smallest value found. we already are holding the current index value
        arr[cur_index] = arr[smallest_index]
        #then whatever the current index value is will be swap to whatever smallest value we found
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = True
    while(swap_occured):
        swap_occured= False
        #a placeholder to determine what index we need to check.
        for x in range(len(arr)):
        #check if ith is bigger than ith+1
            for i in range(0, len(arr)-1):
                if arr[i+1] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    swap_occured = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
#need two array one for counts and a mapping for the count
    count = [0] * maximum

    return arr