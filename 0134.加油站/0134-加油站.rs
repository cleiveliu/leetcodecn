impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let mut cur_rest = 0;
        let mut total_rest = 0;
        let mut start = 0;
        for i in 0..gas.len() {
            total_rest += (gas[i] - cost[i]);
            cur_rest += (gas[i] - cost[i]);
            if cur_rest < 0 {
                start = (i +1) as i32;
                cur_rest = 0;
            }
        }
        
        if total_rest < 0 { -1 } else { start%(gas.len() as i32)}
    }
}