impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let r = grid.len();
        let c = grid[0].len();
        let mut cnt = 0; 
        let mut num = 0; // the numbers of 1
        for i in 0..r {
            for j in 0..c {
                if grid[i][j] == 1 {
                    num += 1;
                }
            }
        }
        for i in 0..r {
            for j in 0..c-1 {
                if grid[i][j] == 1 && grid[i][j+1] == 1 {
                    cnt += 1;
                }
            }
        }
        for i in 0..c {
            for j in 0..r-1 {
                if grid[j][i] == 1 && grid[j+1][i] == 1 {
                    cnt += 1;
                }
            }
        }
        
        num*4 - cnt*2
    }
}