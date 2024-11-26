// Main function
fn main() {
    println!("Hello, Satoshi!");

    println!("-----Wallet-----");

    another_function(99999);

    print_labeled_measurement(21000, 's');

    let x = {
        let y = 6;
        y + 1
    };
    println!("Value of x is: {x}.");
    let x = five();
    println!("Value of x is now: {x}.")
}

// Simple function that print provided Bitcoin Price
fn another_function(x: i32) {
    println!("The Bitcoin price is {x}");
}

// Function that prints value and unit
fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("Bitcoin Balance : {value}{unit_label}");
}

// Function that returns 5
fn five() -> i32 {
    5
}
