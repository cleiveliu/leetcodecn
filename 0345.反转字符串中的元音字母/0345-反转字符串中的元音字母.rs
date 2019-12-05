impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        
        fn is_target(x: &char) -> bool {
            let x = *x;
            match x {
                'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U' => true,
                _ => false,
            }
        }
        
        let mut chars: Vec<char> = s.chars().collect();
        if chars.len() == 0 {
            return "".to_string()
        }
        let mut i = 0usize;
        let mut j = chars.len() - 1;
        
        while i < j {
            if is_target(&chars[i]) && is_target(&chars[j]) {
                let tmp = chars[i];
                chars[i] =chars[j];
                chars[j] =tmp;
                i += 1;
                j -= 1;
            }
            while i < chars.len() && !is_target(&chars[i]) {
                i += 1;
            }
            while j > 0 && !is_target(&chars[j]) {
                j -= 1;
            }
        }
        // println!("{:?}", chars);
        chars.iter().collect::<String>()
    }
}