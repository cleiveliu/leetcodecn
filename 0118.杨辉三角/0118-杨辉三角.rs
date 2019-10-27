impl Solution {
    pub fn generate(n:i32) -> Vec<Vec<i32>> {
        
        let mut ret: Vec<Vec<i32>> = Vec::new();
        for i in 1..((n+1) as usize) {
            let mut arr = vec![1;i];
            for j in 1..i-1 {
                arr[j] = ret[i-2][j-1] + ret[i-2][j];
            }
            ret.push(arr);
        }
        return ret;
    }
}