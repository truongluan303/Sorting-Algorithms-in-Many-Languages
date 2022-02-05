import java.util.Arrays;
import java.lang.Math;
import java.util.Random;

public class SortingAlgorithms<T extends Comparable<? super T>> {


    /**************************************************************************************************
     * M A I N  ===  T E S T   C O D E
     * Generate 2 identical arrays of size 500 that contain random integers.
     * Call the built in sort function to sort the first array.
     * Then use a sorting method implemented above to sort the second array.
     * If both arrays are the same after sorting, the sorting method implemented is working.
     * Repeat this process 1000 times to make sure all edge cases are reached.
     *
     **************************************************************************************************/

    public static void main(String[] args) {

        SortingAlgorithms<Integer> sorter = new SortingAlgorithms<Integer>();

        boolean pass = true;

        for (int i = 0; i < 1000; i++) {

            int size = 500;

            Integer[] arr = new Integer[size];
            int[] copy_arr = new int[size];

            Random rand = new Random();

            for (int k = 0; k < size; k++) {
                int randnum = rand.nextInt(500);
                arr[k] = randnum;
                copy_arr[k] = randnum;
            }

            Arrays.sort(copy_arr);

            // sorter.quickSort(arr);
            // sorter.mergeSort(arr);
            // sorter.insertionSort(arr);
            // sorter.selectionSort(arr);
            // sorter.bubbleSort(arr);
			arr = sorter.countingSort(arr);

            for (int j = 0; j < size; j++) {
                if (copy_arr[j] != arr[j]) {
                    pass = false;
                    System.out.println("\nFailed case\t<<<<<<<<<<<<<<<<<<<<\n");
                    System.out.println("Expected:");
                    System.out.println(Arrays.toString(copy_arr));
                    System.out.println("Result:");
                    System.out.println(Arrays.toString(arr));
                    System.out.println();
                    break;
                }
            }
        }

        System.out.println("\n");
        if (pass) {
            System.out.println("********* P A S S **********");
        }
        else {
            System.out.println("********* F A I L **********");
        }
        System.out.println("\n");
    }






    /**************************************************************************************************
     * Selection sort looks for the smallest value in every loop and
     * puts it at the beginning of the array
     * 
     * @param arr the array to be sorted
     */
    public void selectionSort(T[] arr) {

        for (int i = 0; i < arr.length; i++) {

            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {

                // look for the smallest index
                if (arr[j].compareTo(arr[minIndex]) == -1) {
                    minIndex = j;
                }
            }

            // then swap arr[i] with arr[minIndex]
            swap(arr, minIndex, i);
        }
    }





    /**************************************************************************************************
     * Insertion sort works similar to the way you sort playing cards in your hands.
     * The array is virtually split into a sorted and an unsorted part.
     * Values from the unsorted part are picked and placed at the correct position in the sorted part.
     * 
     * @param arr the array to be sorted
     */
    public void insertionSort(T[] arr) {

        for (int i = 1; i < arr.length; i++) {

            // pick the first index of each loop to be key index
            T key = arr[i];

            // shift the segment greater than the key to the right by 1 unit
            // then put the key at the beginning of that segment
            int j = i - 1;
            while (j >= 0 && key.compareTo(arr[j]) == -1) {

                arr[j + 1] = arr[j];
                j -= 1;
            }

            arr[j + 1] = key;
        }
    }





    /**************************************************************************************************
     * Bubble sort works by repeatedly swapping the adjacent elements
     * if they are not in the right order.
     * 
     * @param arr the array to be sorted
     */
    public void bubbleSort(T[] arr) {

        for (int i = 0; i < arr.length; i++) {

            for (int j = 0; j < arr.length - i - 1; j++) {

                if (arr[j].compareTo(arr[j + 1]) == 1) {
                    swap(arr, j, j + 1);
                }
            }
        }
    }





    /**************************************************************************************************
     * Pick an element in the array as a pivot (last element in this implementation).
     * Partitions the given array around the pivot so that all the elements on the
     * left of the pivot are less than the pivot, and all on the right are bigger
     * than or equal to the pivot. Then keep repeating this process on the partitions
     * created.
     * 
     * @param arr the array to be sorted
     */
    public void quickSort(T[] arr) {
        partition(arr, 0, arr.length - 1);
    }

    /** helper function for quick sort */
    private void partition(T[] arr, int beginIndex, int endIndex) {

        if (beginIndex < endIndex) {

            // pick the last element in the partition as a pivot
            int pivotIndex = endIndex;
            T pivot = arr[pivotIndex];

            /*
            locate the correct position for the pivot,
                where the left of the pivot is less than the pivot,
                and the right of the pivot is greater than the pivot.
            */
            /*
            in order to do that, we'll have 2 running values called i and j.
                We'll set i = beginIndex - 1 and j = beginIndex
                We will use j to loop through the partition.
                If arr[j] < pivot -> increase i and swap arr[i] and arr[j].
            */
            int i = beginIndex - 1;
            for (int j = beginIndex; j < endIndex; j++) {
                if (arr[j].compareTo(pivot) == -1) {
                    i++;
                    swap(arr, i, j);
                }
            }

            /*
            after the process above,
                the left side of i will all be less than the pivot,
                and the right side of i will all be greater than the pivot.
                So, i + 1 will be the correct position for the pivot.
                Therefore, we swap arr[i+1] with the pivot.
            */
            swap(arr, i + 1, pivotIndex);
            pivotIndex = i + 1;

            /*
            We then can continue the partitioning process to the partitions on
                the left side and the right side of the pivot
            */
            partition(arr, beginIndex, pivotIndex - 1);
            partition(arr, pivotIndex + 1, endIndex);
        }
    }





    /**************************************************************************************************
     * Divide the array in 2 halves, and keep repeating that process
     * until all elements in the array are in its own array. Then put
     * these elements back together in order.
     * 
     * @param arr the array to be sorted
     */
    public void mergeSort(T[] arr) {

        if (arr.length > 1) {

            int mid = (int)Math.floor(arr.length >> 1);

            T[] left = Arrays.copyOfRange(arr, 0, mid);
            T[] right = Arrays.copyOfRange(arr, mid, arr.length);

            mergeSort(left);
            mergeSort(right);

            //////////// MERGE PROCESS ///////////

            int l = 0, r = 0, i = 0;

            while (l < left.length && r < right.length) {

                if (left[l].compareTo(right[r]) <= 0) {
                    arr[i] = left[l];
                    l++;
                }
                else {
                    arr[i] = right[r];
                    r++;
                }
                i++;
            }

            // merge the leftover from the left partition
            while (l < left.length) {
                arr[i] = left[l];
                l++;
                i++;
            }

            // merge the leftover from the right partition
            while (r < right.length) {
                arr[i] = right[r];
                r++;
                i++;
            }
        }
    }
	





	/*************************************************************************************************
	* Counting sort works by iterating through the input, counting the 
    * number of times each item occurs, and using those counts to compute 
    * an item's index in the final, sorted array.
    * Counting sort is the only sorting algorithm that is linear in time.
    * However, counting sort is only useful when the largest number in
    * the input is small. Otherwise, it will take up a large space
    * 
    * @param arr the array to be sorted
    * @return the sorted version of the given array
	*/
	public Integer[] countingSort(Integer[] arr) {

		int maxVal = 0;		

		// get the highest value in the array
		for (int i = 0; i < arr.length; i++) {
			maxVal = Math.max(maxVal, arr[i]);
		} 

		int[] count = new int[maxVal + 1];
		
		// initialize all the counts to be -1
		for (int i = 0; i < count.length; i++) {
			count[i] = 0;
		}

		// get the occurences of each value in array
		for (int i = 0; i < arr.length; i++) {
			count[arr[i]]++;
		}

		// get the running sum at each cell
        count[0]--;
		for (int i = 1; i < count.length; i++) {
			count[i] += count[i - 1];
		}

		Integer[] result = new Integer[arr.length];

		for (int i = arr.length - 1; i >= 0; i--) {
			int val = arr[i];
			int idx = count[val];
			result[idx] = val;
			count[val]--;
		}

		return result;
	}	







    /**************************************************************************************************
     * swap two array indices
     * @param arr the array with indices to be swapped
     * @param index1 first index to be swapped
     * @param index2 second index to be swapped
     */
    private void swap(T[] arr, int index1, int index2) {
        T temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
