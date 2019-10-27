impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        let mut guess: i32 = 1;
        while guess < n && guess < std::i32::MAX/2 {
            if guess == n {
                return true;
            }
            guess = guess << 1;
        }
        return guess == n;
    }
}