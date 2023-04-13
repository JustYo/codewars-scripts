fn high_and_low(numbers: &str) -> String {
    let num_list: Vec<&str> = numbers.split(" ").collect();
    let mut buffer_max = -40;
    for item in &num_list {
        let num: i32 = item.parse().unwrap();
        if num > buffer_max {
            buffer_max = num;
        }
    }
    let mut buffer_min = buffer_max;
    for item in num_list {
        let num = item.parse().unwrap();
        if num < buffer_min {
            buffer_min = num;
        }
    }
    let result = format!("{} {}", buffer_max, buffer_min);
    result
}

fn main() {
    println!("{:?}", high_and_low("-1 -1"))
}
