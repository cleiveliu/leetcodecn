struct NumArray {
    nums: Vec<i32>,
    cache: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        let nums = nums.clone();
        let mut cache: Vec<i32> = Vec::with_capacity(nums.len()+1);
        cache.push(0);
        for i in 0..nums.len() {
            cache.push(cache[i]+nums[i]);
        }
        
        NumArray {
            nums, cache
        }
    }
    
    fn sum_range(&self, i: i32, j: i32) -> i32 {
        self.cache[(j+1) as usize] - self.cache[i as usize]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(i, j);
 */