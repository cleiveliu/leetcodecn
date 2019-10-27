impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n == 0 {
            return 0;
        } else if n == 1 || n == 2 {
            return 1;
        }
        let (mut a,mut b,mut c) = (0,1,1);
        let mut n = n;
        while n > 2 {
            let tmp = c;
            c = a + b + c;
            a = b;
            b = tmp;
            n -= 1;
        }
        return c;
    }
}