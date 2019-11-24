impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        let mut ret = 0;
        let mut until_index = 0usize;
        for (index, num) in arr.iter().enumerate() {
            until_index = until_index.max(*num as usize);
            if index == until_index {
                ret += 1;
            }
        }
        
        
        ret
    }
}