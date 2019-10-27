impl Solution {
    pub fn bulb_switch(n: i32) -> i32 {
        let mut ret = 0;
        for i in 1..((n+1) as usize) {
            if i*i <= (n as usize) {
                ret += 1;
            } else {
                break;
            }
        }
        
        ret
    }
}