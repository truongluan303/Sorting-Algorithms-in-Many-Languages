#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include "sort.h"

#define NUMBER_OF_TEST 500
#define SIZE 1000
#define MAX 10000
#define MIN 0

/**************** Prototypes *****************/

/**
 * @brief print an array of integer
 * @param int*  the given array of integer
 * @param int   the size of the given array
 */
void print_arr(int*, unsigned int);


/**
 * @brief check if an array of integer is sorted
 * @param int   the array of integer 
 * @return      true if the given array is sorted
 */
bool check_sorted(int*, unsigned int);

/*********************************************/



/********* Main - Test Code **********/

int main()
{
    srand(time(NULL));
    
    bool pass = true;
    int* arr = calloc(SIZE, sizeof(int));

    for (unsigned _ = 0; _ < NUMBER_OF_TEST; _++)
    {
        // generate an array of random numbers
        for (unsigned short i = 0; i < SIZE; i++)
        {
            int randnum = rand() % MAX + MIN;
            *(arr + i) = randnum;
        }

        /*

        bubble_sort(arr, SIZE);         // sorting using bubble sort

        selection_sort(arr, SIZE);      // sorting using selection sort
        
        */
        insertion_sort(arr, SIZE);      // sorting using insertion sort
        

        if (!check_sorted(arr, SIZE))
        {
            pass = false;
        }
    }

    if (pass)                           // output the result
    {
        printf("\nPASS\n");
    }
    else
    {
        printf("\nFAIL\n");
    }
    
    free(arr);                          // free the allocated memory

    return 0;
}

/**************** end of main */




void print_arr(int* arr, unsigned int size)
{
    for (unsigned int i = 0; i < size; i++)
    {
        printf("%d ", *(arr + i));
    }
    printf("\n");
}




bool check_sorted(int* arr, unsigned int size)
{
    for (unsigned int i = 0; i < SIZE - 1; i++)
    {
        if (*(arr + i) > *(arr + i + 1))
        {
            return false;
        }
    }
    return true;
}