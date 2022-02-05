#include "sort.h"
#include <string.h>


/************* Prototypes ************/

/**
 * @brief swap 2 elements in an array
 * 
 * @param arr   the array containing the elements
 * @param idx1  the 1st element's index
 * @param idx2  the 2nd element's index
 */
void swap(int*, unsigned int, unsigned int);


/**
 * @brief helper function for quicksort
 * 
 * @param int*  the array to be sorted
 * @param int   the starting index
 * @param int   the ending index
 */
void quick_sort_helper(int*, unsigned int, unsigned int);

/*************************************/




void bubble_sort(int* arr, unsigned int size)
{
    for (unsigned int i = 0; i < size; i++)
    {
        for (unsigned int j = 0; j < size - i; j++)
        {
            if (*(arr + j) > *(arr +j + 1))
            {
                swap(arr, j, j + 1);
            }
        }
    }
}



void selection_sort(int* arr, unsigned int size)
{
    for (unsigned int i = 0; i < size; i++)
    {
        int min_idx = i;
        for (unsigned int j = i; j < size; j++)
        {
            if (*(arr + j) < *(arr + min_idx))
            {
                min_idx = j;
            }
        }
        swap(arr, i, min_idx);
    }
}




void insertion_sort(int* arr, unsigned int size)
{
    for (unsigned int i = 1; i < size; i++)
    {
        int key = *(arr + i);
        unsigned int j = i - 1;
        for (j; j > 0; j--)
        {
            if (key >= *(arr + j))
            {
                break;
            }
            *(arr + j + 1) = *(arr + j);
        }
        *(arr + j) = key;
    }
}




void quick_sort(int* arr, unsigned int size)
{
    quick_sort_helper(arr, 0, size - 1);
}



void merge_sort(int* arr, unsigned int size)
{
    /*
    unsigned int mid = size / 2;

    int* fhalf = malloc(mid * sizeof(int));
    if (!fhalf)
    {
        return;
    }
    int* shalf = malloc((size - mid) * sizeof(arr));
    if (!shalf)
    {
        return;
    }

    memcpy(fhalf, arr, mid * sizeof(int));
    memcpy(shalf, arr, (size - mid) * sizeof(int));

    merge_sort(fhalf, mid);
    merge_sort(shalf, size - mid);

    for (unsigned int i = 0; i < size; i++)
    {
        printf("%d ", *(arr + i));
    }
    */
}



void quick_sort_helper(int* arr, unsigned int s_idx, unsigned int e_idx)
{
    
}



void swap(int* arr, unsigned int idx1, unsigned int idx2)
{
    int temp = arr[idx1];
    arr[idx1] = arr[idx2];
    arr[idx2] = temp;
}