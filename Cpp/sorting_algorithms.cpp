#include <iostream>
#include <ctime>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <chrono>

using namespace std;




//------------------------------------------------------
// A helper function that swaps 2 elements in the array
//
template <typename T>
void swap(vector<T>& arr, int idx1, int idx2)  
{  
    T temp = arr[idx1];

    arr[idx1] = arr[idx2];

    arr[idx2] = temp;
}  





//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Insertion sort
//
// Insertion sort works similar to the way you sort playing cards in your hands.
// The array is virtually split into a sorted and an unsorted part.
// Values from the unsorted part are picked and placed at the correct position 
// in the sorted part.
//

template <typename T>
void insertion_sort(vector<T>& arr)
{
    int size = arr.size();

	for (int i = 1; i < size; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[j] > arr[i])
            {
                swap(arr, i, j);
            }
        }
    }
}
//------------------------------------------------- end of insertion sort





//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Selection sort
//
// Selection sort looks for the smallest value in every loop and
// puts it at the beginning of the array
//

template <typename T>
void selection_sort(vector<T>& arr)
{
    int size = arr.size();

	for (int i = 0; i < size - 1; i++)
	{
		int min_idx = i;
		for (int j = i + 1; j < size; j++)
		{
			if (arr[j] < arr[min_idx])
			{
				min_idx = j;
			}
		}
		if (min_idx != i)
        {
			swap(arr, min_idx, i);
        }
	}
}
//------------------------------------------------- end of selection sort





//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Bubble sort
//
// Bubble sort works by repeatedly swapping the adjacent elements
// if they are not in the right order.
//

template <typename T>
void bubble_sort(vector<T>& arr)
{
    int size = arr.size();

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size - i - 1; j++) 
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr, j, j + 1);
            }
        }
    }
}
//-------------------------------------------------- end of bubble sort






//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Quick sort
//
// Pick an element in the array as a pivot (last element in this implementation).
// Partitions the given array around the pivot so that all the elements on the
// left of the pivot are less than the pivot, and all on the right are bigger
// than or equal to the pivot. Then keep repeating this process on the partitions
// created.
//

template <typename T>
void quick(vector<T>& arr, int begin, int end)
{
    if (begin < end)
    {
        int pivot_idx = end - 1;
        int k = begin - 1;

        for (int i = begin; i < end; i++)
        {
            if (arr[i] < arr[pivot_idx])
            {
                k++;
                swap(arr, i, k);
            }
        }

        swap(arr, pivot_idx, k + 1);
        pivot_idx = k + 1;

        quick(arr, begin, pivot_idx);
        quick(arr, pivot_idx + 1, end);
    }
}


template <typename T>
void quick_sort(vector<T>& arr)
{
    quick(arr, 0, arr.size());
}
//---------------------------------------------------- end of quick sort





//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Merge sort
//
// Divide the array in 2 halves, and keep repeating that process
// until all elements in the array are in its own array. Then put
// these elements back together in order.
//

template <typename T>
void merge_sort(vector<T>& arr, int begin, int end)
{
    if (begin < end)
    {
        int mid = (begin + end) / 2;

        merge_sort(arr, begin, mid);
        merge_sort(arr, mid + 1, end);

        ///----- Merge process ------///

        int l = begin;
        int r = mid + 1;
        int i = 0;

        int left_lim = mid;
        int right_lim = end;

        T temp[end - begin + 1];

        while (l <= left_lim and r <= right_lim)
        {
            if (arr[l] <= arr[r])
            {
                temp[i] = arr[l];
                l++;
            }
            else
            {
                temp[i] = arr[r];
                r++;   
            }
            i++;
        }

        // merge the leftover from the left and right subarrays

        while (l <= left_lim)
        {
            temp[i] = arr[l];
            l++;
            i++;
        }
        while (r <= right_lim)
        {
            temp[i] = arr[r];
            r++;
            i++;
        }

        // copy the temp array to the original array

        int m = begin, n = 0;

        while (m < right_lim + 1)
        {
            arr[m] = temp[n];
            m++;
            n++;
        }
    }
}

template <typename T>
void merge_sort(vector<T>& arr)
{
    merge_sort(arr, 0, arr.size() - 1);
}






//-------------------------------------------------------------------------
//-------------------------------------------------------------------------
// Counting Sort
// Counting sort works by iterating through the input, counting the 
// number of times each item occurs, and using those counts to compute 
// an item's index in the final, sorted array.
// Counting sort is the only sorting algorithm that is linear in time.
// However, counting sort is only useful when the largest number in
// the input is small. Otherwise, it will take up a large space
//
vector<int> counting_sort(vector<int> arr)
{
    int size = arr.size();
    int largest = 0;
    vector<int> result(size);

    // get the largest value in the array
    for (int i = 0; i < size; i++)
    {
        if (arr[i] > largest)
            largest = arr[i];
    }

    // count the number of occurence for each number
    vector<int> count(largest + 1);
    for (int i = 0; i < largest; i++)
    {
        count[i] = 0;
    }
    for (int i = 0; i < size; i++)
    {
        count[arr[i]]++;
    }

    // get the running sum at each cell for the count
    // also decrease each cell's value by 1 since array is 0-indexed
    count[0]--;
    for (int i = 1; i < count.size(); i++)
    {
        count[i] += count[i - 1];
    }

    // now each value of count represents the last index that the number
    // appears in the result array
    // insert the values at the right index to the result array
    for (int i = size - 1; i >= 0; i--)
    {
        int val = arr[i];
        int idx = count[val];

        result[idx] = val;
        count[val]--;
    }

    return result;
}
//-------------------------------------------------- end of counting sort






////////////////////////////////////////////////////////////////////////////
//                          T  E  S  T  I  N  G                           //
////////////////////////////////////////////////////////////////////////////


bool compare_arr(vector<int> arr1, vector<int> arr2);
void display_arr(vector<int> arr);

//---------------------------------
// M A I N   ==   T E S T I N G
//----------------------------------

int main()
{
    const int num_of_arr = 1000;
    const int size = 500;
    time_t timer;
    time(&timer);
    srand(unsigned(timer));
    bool passed = true;
    double total_elapsed_t = 0.0;

    vector<int> arr1(size);
    vector<int> arr2(size);

    cout << "\n\nTesting..." << endl;

    for (int n = 0; n < num_of_arr; n++)
    {  
        for (int i = 0; i < size; i++)
        {
            int rand_num = 1 + (rand() % 500);
            arr1[i] = rand_num;
            arr2[i] = rand_num;
        }

        sort(arr1.begin(), arr1.end());

        auto start = chrono::high_resolution_clock::now();

        // selection_sort(arr2);
        // bubble_sort(arr2);
        // insertion_sort(arr2);
        // quick_sort(arr2);
        // merge_sort(arr2);
        arr2 = counting_sort(arr2);

        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start); 

        total_elapsed_t += duration.count();

        if (!compare_arr(arr1, arr2))
        {
            cout << "\n\n\nFAIL" << endl;
            cout << "\nExpected:" << endl;
            display_arr(arr1);
            cout << "\nResult:" << endl;
            display_arr(arr2);
            passed = false;
        }
    }

    if (passed)
    {
        cout << "\n\n***** P A S S E D *****\n\n";
        total_elapsed_t /= 1000000;
        cout << ">>>>> Total Elapsed Sorting Time: " << total_elapsed_t << " milliseconds\n\n";
    }
    else
    {
        cout << "\n\n***** F A I L E D *****\n\n";
    }
}



void display_arr(vector<int> arr)
{
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << "  ";
    }
    cout << endl;
}



bool compare_arr(vector<int> arr1, vector<int> arr2)
{
    if (arr1.size() != arr2.size())
        return false;

    for (int i = 0; i < arr1.size(); i++) 
    {
        if (arr1[i] != arr2[i])
        {
            return false;
        }
    }
    return true;
}
