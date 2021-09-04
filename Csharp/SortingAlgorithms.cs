using System;
using System.Collections.Generic;


namespace Csharp
{
    class SortingAlgorithm<T> where T : IComparable
    {
        
        /**********************************************************************
        Selection Sort
        --------------
        looks for the smallest value in every loop and
        moves it to the final location
        */
        public static void SelectionSort(T[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                int min_idx = i;

                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[j].CompareTo(arr[min_idx]) < 0)
                    {
                        min_idx = j;
                    }
                }
                if (min_idx != i)
                {
                    Swap(arr, min_idx, i);
                }
            }
        }




        /**********************************************************************
        Insertion Sort
        --------------
        works similar to the way you sort playing cards in your hands.
        The array is virtually split into a sorted and an unsorted part.
        Values from the unsorted part are picked and placed at the correct 
        position in the sorted part.
        */
        public static void InsertionSort(T[] arr)
        {
            for (int i = 1; i < arr.Length; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    if (arr[j].CompareTo(arr[i]) > 0)
                    {
                        Swap(arr, i, j);
                    }
                }
            }
        }




        /**********************************************************************
        Bubble Sort
        -----------
        works by repeatedly swapping the adjacent elements
        if they are not in the right order.
        */
        public static void BubbleSort(T[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                for (int j = 0; j < arr.Length - i - 1; j++)
                {
                    if (arr[j].CompareTo(arr[j + 1]) > 0)
                    {
                        Swap(arr, j + 1, j);
                    }
                }
            }
        }




        /**********************************************************************
        Quick Sort
        ----------
        */
        public static void QuickSort(T[] arr)
        {
            QuickSort(arr, 0, arr.Length - 1);
        }

        private static void QuickSort(T[] arr, int begin, int end)
        {
            if (begin < end)
            {
                int pivot_idx = end;

                int i = begin - 1;
                for (int j = begin; j < end; j++)
                {
                    if (arr[j].CompareTo(arr[pivot_idx]) < 0)
                    {
                        i++;
                        Swap(arr, i, j);
                    }
                }

                Swap(arr, i + 1, pivot_idx);
                pivot_idx = i + 1;

                // repeat the same process to the right and left partitions
                QuickSort(arr, begin, pivot_idx - 1);
                QuickSort(arr, pivot_idx + 1, end);
            }
        }




        /**********************************************************************
        Merge Sort
        ----------
        Divide the array in 2 halves, and keep repeating that process
        until all elements in the array are in its own array. Then put
        these elements back together in order.
        */
        public static void MergeSort(T[] arr)
        {
            if (arr.Length > 1)
            {
                int mid = arr.Length / 2;

                T[] left = new T[mid];
                T[] right = new T[arr.Length - mid];

                // divide the array into 2 subarrays

                Array.Copy(arr, 0, left, 0, mid);
                Array.Copy(arr, mid, right, 0, arr.Length - mid);

                // keep doing the same process on the subarrays
                
                MergeSort(left);
                MergeSort(right);

                // merge the subarrays back together

                int i = 0, r = 0, l = 0;               

                while (l < left.Length && r < right.Length)
                {
                    if (left[l].CompareTo(right[r]) <= 0)
                    {
                        arr[i] = left[l];
                        l++;
                    }
                    else
                    {
                        arr[i] = right[r];
                        r++;
                    }
                    i++;
                }

                // merge the leftover if there's any

                while (l < left.Length)
                {
                    arr[i] = left[l];
                    i++;
                    l++;
                }
                while (r < right.Length)
                {
                    arr[i] = right[r];
                    i++;
                    r++;
                }
            }
        }





        /**********************************************************************
        Swap
        ----
        A Helper function to swap two elements in an array
        */
        private static void Swap(T[] arr, int idx1, int idx2)
        {
            T temp = arr[idx1];
            arr[idx1] = arr[idx2];
            arr[idx2] = temp;
        }
    }





    ///////////////////////////////////////////////////////////////////////////

    //                          T  E  S  T  I  N  G                          //

    /**
    Run the test to check if the sorting algorithm passes
    ---------------------------------------------------------------------------------------
    * Generate 2 identical arrays of size 500 that contain random integers.
    * Call the built in sort function to sort the first array.
    * Then use a sorting method implemented above to sort the second array.
    * If both arrays are the same after sorting, the sorting method implemented is working.
    * Repeat this process 1000 times to make sure all edge cases are reached.
    */
    class Test
    {
        private const int REPEAT = 1000;
        private const int SIZE = 500;

        static void Main(string[] args)
        {   
            int[] arr1 = new int[SIZE];
            int[] arr2 = new int[SIZE];
            SortingAlgorithm<int> sort = new SortingAlgorithm<int>();

            Random rand = new Random();
            bool finalResult = true;
            
            Console.WriteLine("\n\nTesting...");

            for (int i = 0; i < REPEAT; i++) 
            {
                bool pass = true;

                // init 2 arrays with the same random numbers
                for (int j = 0; j < SIZE; j++) 
                {
                    int randNum = rand.Next(1, 100);
                    arr1[j] = randNum;
                    arr2[j] = randNum;
                }

                Array.Sort(arr1);

                // SortingAlgorithm<int>.InsertionSort(arr2);
                // SortingAlgorithm<int>.SelectionSort(arr2);
                // SortingAlgorithm<int>.BubbleSort(arr2);
                // SortingAlgorithm<int>.QuickSort(arr2);
                SortingAlgorithm<int>.MergeSort(arr2);

                // compare 2 arrays
                for (int k = 0; k < SIZE; k++)
                {
                    if (arr1[k] != arr2[k])
                    {
                        pass = false;
                        finalResult = false;
                        break;
                    }   
                }

                if (!pass)
                {
                    Console.WriteLine("\n\nFailed Case <<<<<<<<<<<<<<<\n");
                    Console.WriteLine("Expected:");
                    Console.WriteLine(string.Join(", ", arr1));
                    Console.WriteLine("Result:");
                    Console.WriteLine(string.Join(", ", arr2));
                }
            }


            Console.WriteLine("\n\n");
            if (finalResult)
            {
                Console.WriteLine("********** P A S S **********");
            }
            else
            {
                Console.WriteLine("********** F A I L **********");
            }
            Console.WriteLine("\n\n");
        }
    }
}