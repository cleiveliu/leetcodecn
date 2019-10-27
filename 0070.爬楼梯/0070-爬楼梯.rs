impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        fn fib(n: i32) -> i32 {
            if n == 1 || n == 2 {
                return n;
            }
            let mut a = 1;
            let mut b = 2;
            let mut n = n;
            while n > 2 {
                let tmp = a;
                a = b;
                b = tmp + b;
                n -= 1;
            }
            return b;
        }
        return fib(n);
    }
}