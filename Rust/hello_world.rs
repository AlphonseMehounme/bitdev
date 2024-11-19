use ferris_says::say;
use std::io::{stdout, BufWriter};

fn main() {
    let stdout = stdout();
    let message = String::from("Hello fellow Bitcoiners!");
    let width = message.chars().count();
    let mut writer = BufWriter::new(stdout.lock());
    say(&message, width, &mut writer).unwrap();
    let mut my_name = "Alphonse";
    let my_age: i32 = 26;
    println!("My name is {my_name} \
        and I am {my_age}!"
    );
    my_name = "Ferris";
    println!("My name is {my_name} and I \
        am {my_age}!"
    );
}
