fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
    const SECONDS_IN_HOUR: u32 = 60 * 60;
    println!("Nuber of seconds is: {SECONDS_IN_HOUR}");
    {
        let x = x + 1;
        println!("X in the scope {x}");
    }
    println!("The value of x is: {x}");
}
