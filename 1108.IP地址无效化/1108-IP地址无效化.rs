impl Solution {
    pub fn defang_i_paddr(addr: String) -> String {
        addr.chars().map(|x| if x == '.' {"[.]".to_string()} else {x.to_string()})
                    .collect::<String>()
    }
}