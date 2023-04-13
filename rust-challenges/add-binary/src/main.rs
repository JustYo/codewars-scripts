fn add_binary(a: u64, b: u64) -> String {
    let result = a + b;
    format!("{:b}", result)
}

fn main() {
    println!("{}", add_binary(1, 1));
}
