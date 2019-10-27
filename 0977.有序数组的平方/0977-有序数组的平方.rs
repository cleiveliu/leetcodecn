impl Solution {
    pub fn sorted_squares(a: Vec<i32>) -> Vec<i32> {
        let mut ret: Vec<i32> = a.iter().map(|x| x*x).collect();
        ret.sort();
        
        ret
    }
}