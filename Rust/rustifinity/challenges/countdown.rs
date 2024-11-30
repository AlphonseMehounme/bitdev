pub fn countdown(n: u32) -> Vec<u32> {
    // TODO: Implement the countdown using a while loop
if n == 0 {
        vec![0]
    } else {
        let mut vect : Vec<u32> = Vec::new();
        let mut m = n;
        while m > 0 {
            vect.push(m);
            m -= 1;
        }
        vect.push(0);
        vect
    }
}
