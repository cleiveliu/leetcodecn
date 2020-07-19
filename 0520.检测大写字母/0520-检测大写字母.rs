#[derive(PartialEq)]
pub enum CharKind {
    Lower,
    Upper,
    Other,
}
impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let mut low = 0usize;
        let mut up = 0usize;
        for c in word.chars() {
            match Solution::judge(c) {
                CharKind::Lower => low += 1,
                CharKind::Upper => up += 1,
                _ => (),
            }
        }
        let n = word.chars().count();

        if low == n || up == n {
            return true;
        } else if up == 1 && Solution::judge(word.chars().next().unwrap()) == CharKind::Upper {
            return true;
        } else {
            return false;
        }
    }

    fn judge(c: char) -> CharKind {
        match c {
            'a'..='z' => CharKind::Lower,
            'A'..='Z' => CharKind::Upper,
            _ => CharKind::Other,
        }
    }
}