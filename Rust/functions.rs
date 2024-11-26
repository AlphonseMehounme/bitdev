fn main() {
    println!("Hello, Satoshi!");

    println!("-----Wallet-----");

    another_function(99999);

    print_labeled_measurement(21000, 's')
}

fn another_function(x: i32) {
    println!("The Bitcoin price is {x}");
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("Bitcoin Balance : {value}{unit_label}");
}
