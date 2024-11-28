pub fn sum_array(arr: &[i32]) -> i32 {
    // TODO: Implement the function here
    let mut sum: i32 = 0;
    for el in arr {
        sum += el;
    }
    sum
}
