impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut nums1 = nums1;
        nums1.extend(nums2.iter().cloned());
        nums1.sort();
        let n = nums1.len();
        if n%2 == 1 {
            nums1[n/2] as f64
        } else {
            ((nums1[n/2-1] + nums1[n/2]) as f64) / 2.0 
        }
    }
}