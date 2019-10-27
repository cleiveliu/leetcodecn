use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i,val) in nums.iter().enumerate() {
            if map.contains_key(val) {
                return vec![map[val] as i32,i as i32];
            } else {
                map.insert(target - val,i);
            }
        }
        return vec![];
    }
}