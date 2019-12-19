impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let len = flowerbed.len() + 2;
        let mut arr: Vec<i32> = Vec::with_capacity(len);
        arr.push(0);
        for val in flowerbed {
            arr.push(val);
        }
        arr.push(0);
        
        let mut count = 0;
        let mut i: usize = 1;
        
        while i < arr.len()-1 {
            if arr[i-1] == 0 && arr[i] == 0 && arr[i+1] == 0 {
                arr[i] = 1;
                count += 1;
                if count >= n {
                    return true;
                }
            }
            i += 1;
        }
        
        return count >= n;
    }
}