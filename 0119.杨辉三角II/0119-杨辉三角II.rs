impl Solution {
    pub fn get_row(n: i32) -> Vec<i32> {
        let mut ret: Vec<Vec<i32>> = Vec::new();
        for i in 1..((n+2) as usize) {
            let mut arr = vec![1;i];
            for j in 1..i-1 {
                arr[j] = ret[i-2][j-1] + ret[i-2][j];
            }
            ret.push(arr);
        }
        return ret[n as usize].clone();
        
    }
}