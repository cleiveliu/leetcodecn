impl Solution {
    pub fn total_hamming_distance(nums: Vec<i32>) -> i32 {
        let mut ret = 0;
        let (mut c0, mut c1) = (0, 0);
        for i in 0..30 {
            for num in nums.iter() {
                if ((num >> i) & 1) == 0 {
                    c0 += 1;
                } else {
                    c1 += 1;
                }
            }
            ret += c0*c1;
            c0 = 0;
            c1 = 0;
        }
        
        ret
    }
}