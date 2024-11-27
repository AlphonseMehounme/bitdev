fn main() {
    println!("----Start----");
    let mut counter = 0;
    let result = loop {
        counter += 1;
        println!("counter is {counter}");
        if counter == 10 {
            break counter * 2;
        }
    };
    println!("The result is {result}");

    let mut count = 0;
    'counting_up: loop {
        println!("Count: {count}");
        let mut remaining = 10;

        loop {
            println!("Remaining: {remaining}");
            if remaining == 9 {
                break;
            }
	    if count == 2 {
		break 'counting_up;
	    }
	    remaining -= 1;
        }
	count += 1;
    }

    while count != 0 {
	println!("Not zero yet");
	count -= 1;
    }
    let coins = ["BTC", "BTC", "BTC"];
    for coin in coins {
        println!("Thes best is {coin} and there is no second best");
    }
    println!("Count is now 0
----End----");
}
