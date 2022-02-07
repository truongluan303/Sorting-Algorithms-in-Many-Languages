import random
import unittest
from typing import Tuple, List
from sorting_algorithms import *



class Test(unittest.TestCase):
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
    
    RANGE = 1000
    ARR_SIZE = 500
    

    def generate_arrays(self) -> Tuple[List[List[int]]]:
        
        res1 = []
        res2 = []
        
        for __ in range(self.RANGE):
            arr1 = []
            arr2 = []

            for _ in range (self.ARR_SIZE):
                rand_num = random.randint(0, 1000)
                arr1.append(rand_num)
                arr2.append(rand_num)
                
            res1.append(arr1)
            res2.append(arr2)
            
        return (res1, res2)
        
        
    
    def test_bubble_sort(self):
        print("\nTesting bubble sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(bubble_sort(arrs1[i]), sorted(arrs2[i]))



    def test_recursive_bubble_sort(self):
        print("\nTesting recursive bubble sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(bubble_sort_recursive(arrs1[i]), sorted(arrs2[i]))
          
            
            
    def test_insertion_sort(self):
        print("\nTesting insertion sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(insertion_sort(arrs1[i]), sorted(arrs2[i]))
    
    
    
    def test_selection_sort(self):
        print("\nTesting selection sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(selection_sort(arrs1[i]), sorted(arrs2[i]))
            
            
            
    def test_quicksort(self):
        print("\nTesting quicksort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(quick_sort(arrs1[i]), sorted(arrs2[i]))
            
            
            
    def test_merge_sort(self):
        print("\nTesting merge sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(merge_sort(arrs1[i]), sorted(arrs2[i]))
            
            
            
    def test_merge_sort_inplace(self):
        print("\nTesting in-place merge sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(merge_sort_inplace(arrs1[i]), sorted(arrs2[i]))
            
            
            
    def test_counting_sort(self):
        print("\nTesting counting sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(counting_sort(arrs1[i]), sorted(arrs2[i]))
            
            
            
    def test_heap_sort(self):
        print("\nTesting heap sort...")
        arrs1, arrs2 = self.generate_arrays()
        for i in range(self.RANGE):
            self.assertEqual(heap_sort(arrs1[i]), sorted(arrs2[i]))




if __name__ == "__main__":
    unittest.main()