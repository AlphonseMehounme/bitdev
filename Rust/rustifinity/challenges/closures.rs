pub fn create_closures() -> (
    impl Fn(i32, i32) -> i32,
    impl Fn(i32, i32) -> i32,
    impl Fn(i32, i32) -> i32,
) {
    let add_closure = |a, b| {
        // Step 1: Implement here
        a + b
    };

    // Step 2:
    // Create the `subtract_closure` closure that subtracts two `i32` values.
    let subtract_closure = |a, b| a - b;
    // Step 3:
    // Create the `multiply_closure` closure that multiplies two `i32` values.
    let multiply_closure = |a, b| a * b;

    (add_closure, subtract_closure, multiply_closure)
}
