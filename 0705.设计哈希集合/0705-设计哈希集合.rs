struct MyHashSet {
    vals: [bool; 100_0005],
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {

    /** Initialize your data structure here. */
    fn new() -> Self {
        MyHashSet { vals: [false; 100_0005]}
    }
    
    fn add(&mut self, key: i32) {
        self.vals[key as usize] = true;
    }
    
    fn remove(&mut self, key: i32) {
        self.vals[key as usize] = false;
    }
    
    /** Returns true if this set contains the specified element */
    fn contains(&self, key: i32) -> bool {
        self.vals[key as usize]
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */