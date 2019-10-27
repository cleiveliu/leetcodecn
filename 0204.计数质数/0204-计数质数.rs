impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        if n < 3{
            return 0;
        } else {
            let mut ret:Vec<i32> = vec![1;n as usize];
            for i in 2..((n/2 +1) as usize) {
                if ret[i] == 1 {
                    let mut index = 2*(i as i32);
                    while index < n {
                        ret[index as usize] = 0;
                        index += i as i32;
                    }
                }
            }
            return ret.iter().sum::<i32>() - 2;
        }
        unreachable!();
        
    }
}