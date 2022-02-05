import time


##################################################################
######################### SELECTION SORT #########################

def selection_sort(array: list) -> None:
    ''' 
    Selection sort 
    ---------------------
    looks for the smallest value in every loop and
    puts it at the beginning of the array
    '''

    for i in range (0, len(array) - 1):
        min_idx = i

        for j in range (i + 1, len(array)):

            if array[j] < array[min_idx]:
                min_idx = j

        temp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp

                



###################################################################
######################### BUBBLE SORT #############################

def bubble_sort(array: list) -> None:
    ''' 
    Bubble sort 
    --------------------
    works by repeatedly swapping the adjacent elements
    if they are not in the right order.
    '''

    for i in range (0, len(array)):

        for j in range (0, len(array) - i - 1):

            # compare the elements by pair
            if array[j] > array[j + 1]:

                # swap 
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp





def bubble_sort_recursive(array: list) -> None:
    ''' 
    A Recursive version of bubble sort
    '''

    def bubble_sort_recursive(array, n):
        ''' Inner helper function '''

        if n == 0:
            return

        for i in range (0, n - 1):

            if array[i] > array[i + 1]:

                # swap
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

        bubble_sort_recursive(array, n - 1)


    bubble_sort_recursive(array, len(array))





######################################################################
########################## INSERTION SORT ############################

def insertion_sort(arr: list) -> None:
    ''' 
    Insertion sort 
    -------------------
    works similar to the way you sort playing cards in your hands.
    The array is virtually split into a sorted and an unsorted part.
    Values from the unsorted part are picked and placed at the correct 
    position in the sorted part.
    '''

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1

        while j >= 0 and key < arr[j] :

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key







#######################################################################
################################# MERGE SORT ##########################

def merge_sort(arr: list) -> None:
    ''' 
    Merge sort 
    ---------------
    Divide the array in 2 halves, and keep repeating that process
    until all elements in the array are in its own array. Then put
    these elements back together in order.
    '''

    if len(arr) > 1:

        # find the mid point
        mid = len(arr) // 2

        # divide the array into 2 subarrays
        sub_left = arr[:mid]
        sub_right = arr[mid:]

        # keep dividing the subarrays into smaller chunks
        merge_sort(sub_left)
        merge_sort(sub_right)


        l = r = i = 0
        # merge the 2 halves together in sorted order
        while l < len(sub_left) and r < len(sub_right):

            if sub_left[l] <= sub_right[r]:
                arr[i] = sub_left[l]
                l += 1

            else:
                arr[i] = sub_right[r]
                r += 1

            i += 1

        # merge the leftover from the left subarray
        while l < len(sub_left):
            arr[i] = sub_left[l]
            i += 1
            l += 1

        # merge the leftover from the right subarray
        while r < len(sub_right):
            arr[i] = sub_right[r]
            i += 1
            r += 1






def merge_sort_inplace(arr: list) -> None:
    ''' 
    A slightly different way to do merge sort.
    In this version, we are not breaking the original array into subarrays.
    Instead, we partitioning right on the original array itself.
    '''

    def merge_sort(arr, begin, end):
        ''' Inner helper function '''

        if begin < end:

            # find the mid point
            mid = (begin + end) // 2

            # keeps dividing the partitions in halves
            merge_sort(arr, begin, mid)
            merge_sort(arr, mid + 1, end)

            #####------- merge process -------####

            l = begin
            r = mid + 1

            left_lim = mid
            right_lim = end

            temp = []

            while l <= left_lim and r <= right_lim:

                # compare and put the smaller values in first
                if arr[l] <= arr[r]:
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[r])
                    r += 1

            # adding the leftover from the left subarray
            while l <= left_lim:
                temp.append(arr[l])
                l += 1

            # adding the leftover from the right subarray
            while r <= right_lim:
                temp.append(arr[r])
                r += 1

            i, j = begin, 0

            # copy the temp to the array
            while i < right_lim + 1:
                arr[i] = temp[j]
                i += 1
                j += 1

    merge_sort(arr, 0, len(arr) - 1)







#######################################################################
############################### QUICK SORT ############################

def quick_sort(arr: list) -> None:
    ''' 
    Quick sort 
    ---------------------------
    Pick an element in the array as a pivot (last element in this implementation).
    Partitions the given array around the pivot so that all the elements on the
    left of the pivot are less than the pivot, and all on the right are bigger
    than or equal to the pivot. Then keep repeating this process on the partitions
    created.
    '''

    def quick_sort(arr, begin, end):
        ''' Inner helper function '''

        if (begin < end):

            pivot = arr[end]
            j = begin - 1

            for i in range (begin, end):

                if arr[i] < pivot:
                    # increase j
                    j += 1
                    # then swap arr[j] with arr[i]
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

            # the position for the pivot is where left values are less than and
            # the right values are greater than the value at the pivot position
            arr[end] = arr[j + 1]
            arr[j + 1] = pivot
            pivot_index = j + 1

            # do the same process to the left partition and right partition
            quick_sort(arr, pivot_index + 1, end)
            quick_sort(arr, begin, pivot_index - 1)


    quick_sort(arr, 0, len(arr)-1)







#######################################################################
############################ COUNTING SORT ############################

def counting_sort(arr: list) -> list:
    '''
    Counting sort works by iterating through the input, counting the 
    number of times each item occurs, and using those counts to compute 
    an item's index in the final, sorted array.
    Counting sort is the only sorting algorithm that is linear in time.
    However, counting sort is only useful when the largest number in
    the input is small. Otherwise, it will take up a large space
    '''
    result = list(range(len(arr)))

    # find the largest number
    largest = max(arr)

    # use an array to keep track of the occurence of each number
    count = [0] * (largest + 1)

    # count the occurence for each number in the array
    for i in arr:
        count[i] += 1

    # get the running sum at each cell for count
    # also decrease each cell's value by 1 since array index is 0-based
    count[0] -= 1
    for i in range(1, len(count)):
        count[i] += count[i - 1] 

    # insert the values to its correspoding index to the result array
    for i in range(len(arr) - 1, -1, -1):
        val = arr[i]
        idx = count[val]
        result[idx] = val
        count[val] -= 1

    return result







#########################################################################################

import random

def main():
    '''
    ==================
    T E S T   C O D E
    ==================
    
    Generate 2 identical arrays of size 500 that contain random integers.
    Call the built in sort function to sort the first array.
    Then use a sorting method implemented above to sort the second array.
    If both arrays are the same after sorting, the sorting method implemented is working.
    Repeat this process 1000 times to make sure all edge cases are reached.

    '''

    print("\nTesting...")

    RANGE = 1000

    total_time = 0

    for __ in range(RANGE):

        arr1 = []
        arr2 = []
        passed = True

        for _ in range (500):
            rand_num = random.randint(0, 100)
            arr1.append(rand_num)
            arr2.append(rand_num)

        arr1.sort(reverse=False)

        start_t = time.time()

        # un-comment to test the desired sorting algorithm.

        # bubble_sort(arr2)
        # bubble_sort_recursive(arr2)
        # insertion_sort(arr2)
        # selection_sort(arr2)
        # quick_sort(arr2)
        # merge_sort_inplace(arr2)
        # arr2 = counting_sort(arr2)
        merge_sort(arr2)

        end_t = time.time()

        executed_t = (end_t - start_t)
        total_time += executed_t


        for i in range(len(arr1)):

            if arr1[i] != arr2[i]:

                passed = False
                print("\n\nFailed Case <<<<<<<<<<<<<<<<<<<<<<<<")
                print("Expected:")
                print(arr1)
                print("Result:")
                print(arr2)
                break

    if not passed:
        print('\n\n>>> F A I L E D <<<\n\n')
    else:
        print('\n\n>>> P A S S E D   A L L  C A S E S <<<\n')
        print('>>> Total elapsed sorting time: ', round(total_time, 6), 'seconds\n\n')

if __name__ == "__main__":
    main()