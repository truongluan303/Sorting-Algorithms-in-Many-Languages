##################################################################
######################### SELECTION SORT #########################

def selection_sort(array: list) -> list:
    ''' 
    Selection sort 
    ---------------------
    looks for the smallest value in every loop and
    puts it at the beginning of the array
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
    '''

    for i in range (0, len(array) - 1):
        min_idx = i

        for j in range (i + 1, len(array)):

            if array[j] < array[min_idx]:
                min_idx = j

        # swap the elements at i and min_idx
        array[i], array[min_idx] =  array[min_idx], array[i]
        
    return array





###################################################################
######################### BUBBLE SORT #############################

def bubble_sort(array: list) -> list:
    ''' 
    Bubble sort 
    --------------------
    works by repeatedly swapping the adjacent elements
    if they are not in the right order.
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
    '''

    for i in range (0, len(array)):

        for j in range (0, len(array) - i - 1):

            # compare the elements by pair
            if array[j] > array[j + 1]:
                # swap 
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array





def bubble_sort_recursive(array: list) -> list:
    ''' 
    A Recursive version of bubble sort
    '''

    def bubble_sort_recursive(array: list, n: int):
        """ Inner helper function

        Args:
            array (list):   the array
            n (int):        current index 
        """
        if n == 0:
            return

        for i in range (0, n - 1):

            if array[i] > array[i + 1]:

                # swap
                array[i], array[i + 1] = array[i + 1], array[i]

        bubble_sort_recursive(array, n - 1)


    bubble_sort_recursive(array, len(array))
    return array





######################################################################
########################## INSERTION SORT ############################

def insertion_sort(arr: list) -> list:
    ''' 
    Insertion sort 
    -------------------
    works similar to the way you sort playing cards in your hands.
    The array is virtually split into a sorted and an unsorted part.
    Values from the unsorted part are picked and placed at the correct 
    position in the sorted part.
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
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

    return arr






#######################################################################
################################# MERGE SORT ##########################

def merge_sort(arr: list) -> list:
    ''' 
    Merge sort 
    ---------------
    Divide the array in 2 halves, and keep repeating that process
    until all elements in the array are in its own array. Then put
    these elements back together in order.
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
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
            
    return arr






def merge_sort_inplace(arr: list) -> list:
    ''' 
    A slightly different way to do merge sort.
    In this version, we are not breaking the original array into subarrays.
    Instead, we partitioning right on the original array itself.
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
    '''

    def merge_sort(arr, begin, end):
        """ Inner helper function
        Args:
            arr ([type]):   the array
            begin ([type]): the beginning index
            end ([type]):   the ending index
        """
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
    return arr






#######################################################################
############################### QUICK SORT ############################

def quick_sort(arr: list) -> list:
    ''' 
    Quick sort 
    ---------------------------
    Pick an element in the array as a pivot (last element in this implementation).
    Partitions the given array around the pivot so that all the elements on the
    left of the pivot are less than the pivot, and all on the right are bigger
    than or equal to the pivot. Then keep repeating this process on the partitions
    created.
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
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
                    arr[i], arr[j] = arr[j], arr[i]

            # the position for the pivot is where left values are less than and
            # the right values are greater than the value at the pivot position
            arr[end] = arr[j + 1]
            arr[j + 1] = pivot
            pivot_index = j + 1

            # do the same process to the left partition and right partition
            quick_sort(arr, pivot_index + 1, end)
            quick_sort(arr, begin, pivot_index - 1)


    quick_sort(arr, 0, len(arr)-1)
    return arr






#######################################################################
############################ COUNTING SORT ############################

def counting_sort(arr: list) -> list:
    '''
    Counting sort works by iterating through the input, counting the 
    number of times each item occurs, and using those counts to compute 
    an item's index in the final, sorted array
    Counting sort is the only sorting algorithm that is linear in time.
    However, counting sort is only useful when the largest number in
    the input is small. Otherwise, it will take up a large space
    
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
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





#######################################################################
############################## HEAP SORT ##############################

def heap_sort(arr: list) -> list:
    """
    Sort an array by creating a max heap using the elements of the
    given array. Heap sort basically recursively performs 2 main
    operations including building a heap and repeatedly delete the
    root element of the heap formed after the build
        
    Args:
        arr (list): the array to be sorted
        
    Returns:
        list: the sorted array
    """
    
    def heapify(size: int, idx: int):
        """
        An inner helper function to perform max heapify process
        Args:
            arr (list): the array
            size (int): the size limit
            idx (int):  current index
        """
        max_idx = idx               # set the max index to be the current index
        lidx = idx * 2 + 1          # the left child's index
        ridx = idx * 2 + 2          # the right child's index
        
        # find the biggest element among the root and 2 children
        if lidx < size and arr[lidx] > arr[max_idx]:
            max_idx = lidx
        if ridx < size and arr[ridx] > arr[max_idx]:
            max_idx = ridx
            
        # if the max index has been changed
        if max_idx != idx:
            # swap the elements at current index and max index
            arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
            # continue heapifying the affected subtree
            heapify(size, max_idx)
            
            
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(len(arr), i)
        
    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i] # move the root to the end of the array
        heapify(i, 0)                   # max heapify the reduced heap
        
    return arr