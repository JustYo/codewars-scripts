fn num_to_vec(num: u64) -> Vec<u64> {
    let mut x = num;
    let mut result: Vec<u64> = Vec::new();

    if num == 0 {
        return vec![0];
    } else {
        loop {
            result.push(x % 10);
            x /= 10;
            if x == 0 {
                break;
            }
        }
        result.reverse();
        return result;
    }
}

fn persistence(num: u64) -> u64 {
    if (num == 0) | (num < 10) {
        0
    } else {
        let mut mut_num = num;
        let mut i: u64 = 0;
        loop {
            let mut mult_res: u64 = 1;
            let num_vec = num_to_vec(mut_num);
            for item in num_vec.iter() {
                mult_res = mult_res * item;
            }
            let res_vec = num_to_vec(mult_res);
            mut_num = mult_res;
            i += 1;
            if res_vec.len() == 1 {
                break;
            }
        }
        i
    }
}

fn main() {
    println!("Hello, world!");
    let num = 4;
    println!("{:?}", persistence(num))
}
