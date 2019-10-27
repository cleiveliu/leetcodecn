impl Solution {
    pub fn asteroid_collision(nums: Vec<i32>) -> Vec<i32> {
        let mut stack = vec![];
        for num in nums {
            if stack.is_empty() || stack[stack.len()-1] < 0 || num > 0 {
                stack.push(num);
            } else if num < 0 {
                let mut push_num = true;
                while !stack.is_empty() && push_num {
                    let last = stack.len() - 1;
                    if stack[last] > 0 {
                        if stack[last] > num.abs() {
                            push_num = false;
                        } else if stack[last] == num.abs() {
                            stack.pop();
                            push_num = false;
                        } else if stack[last] < num.abs() {
                            stack.pop();
                        }
                    } else if stack[last] < 0 {
                        break;
                    }
                }
                if push_num {
                    stack.push(num);
                }
            }
        }

        stack
    }
}