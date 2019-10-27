use std::collections::HashSet;
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut xs = HashSet::new();
        let mut ys = HashSet::new();
        let r = matrix.len();
        let c = matrix[0].len();
        for i in 0..r {
            for j in 0..c {
                if matrix[i][j] == 0 {
                    xs.insert(i);
                    ys.insert(j);
                }
            }
        }
        for x in xs {
            for i in 0..c {
                matrix[x][i] = 0;
            }
        }
        for y in ys {
            for i in 0..r {
                matrix[i][y] = 0;
            }
        }
    }
}