pub fn sum_of_evens(start: i32, end: i32) -> i32 {
    let mut sum = 0;
    for num in start..=end + 1 {
        if num % 2 == 0 {
            sum += num;
        }
    }
    sum
}
