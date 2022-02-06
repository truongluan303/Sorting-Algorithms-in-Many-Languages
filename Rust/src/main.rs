use rand::Rng;



pub fn bubble_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        for j in 1..(arr.len() - i) {
            if arr[j] < arr[j - 1] {
                arr.swap(j, j - 1);
            }
        }
    }
}



// TODO: selection sort under development
pub fn selection_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        let mut min_idx: usize = i;
        for j in i..arr.len() {
            if arr[j] < arr[min_idx] {
                min_idx = j;
            }
        }
        arr.swap(min_idx, i);
    }
}



pub fn insertion_sort(arr: &mut Vec<i32>) {
    for i in 1..arr.len() {
        let key: i32 = arr[i];
        let mut j: usize = i - 1;
        while key < arr[j] && j >= 0 {
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = key;
    }
}



fn main() {
    const REPEAT: i32 = 100;    // number of repititions
    const SIZE: usize = 1000;   // size of each array
    const RANGE: i32 = 100;     // range of the values in the arrays
    
    let mut passed: bool = true;

    // create 2 vectors
    let mut arr1: Vec<i32> = vec![0; SIZE];
    let mut arr2: Vec<i32> = vec![0; SIZE];

    println!("\nRunning test...\n");

    // run the test for 100 times

    for i in 0..REPEAT {
        
        // generate random values for each element in the arrays
        for j in 0..SIZE {
            let randval: i32 = rand::thread_rng().gen_range(0..RANGE);
            arr1[j] = randval;
            arr2[j] = randval;
        }

        arr1.sort();
        
        //bubble_sort(&mut arr2);

        //selection_sort(&mut arr2);

        //insertion_sort(&mut arr2);

        if arr1 != arr2 {
            println!("\n> Case {}: Failed", i + 1);
            println!("Expected:");
            print_vector(&mut arr1);
            println!("\nActual:");
            print_vector(&mut arr2);
            passed = false;
        }
    }

    if passed {
        println!("\n>>>>>> All Cases Passed <<<<<<\n");
    }
    else {
        println!("\n>>>>>> Failed <<<<<<\n");
    }
}


fn print_vector(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        print!("{} ", i);
    }
    println!();
}