impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n < 2 {
            return n;
        }
        let mut n = n;
        let mut a = 0;
        let mut b = 1;
        while n > 1 {
            let tmp = b;
            b = a +b;
            a = tmp;
            n -= 1;
        }
        return b;
        /*
        match n {
            0 => 0,
            1 => 1,
            _ => Self::fib(n-1) + Self::fib(n-2),
        }
        */
    }
}