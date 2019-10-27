impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        s.trim().chars().rev().take_while(|&x| x!= ' ').collect::<String>().len() as i32
    }
}