pub fn check_number_sign(number: i32) -> String {
    // Return `"positive"` if the number is positive.
    // Return `"negative"` if the number is negative.
    // Return `"zero"` if the number is zero.
    if number > 0 {
        String::from("positive")
    } else if number < 0 {
        String::from("negative")
    } else {
        String::from("zero")
    }
}
