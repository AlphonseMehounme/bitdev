pub fn fibonacci(n: u32) -> u32 {
    // TODO: Implement the Fibonacci sequence
    if n == 0 {
        0
    } else if n == 1 {
        1
    } else {
        fibonacci(n - 2) + fibonacci(n - 1)
    }
}
