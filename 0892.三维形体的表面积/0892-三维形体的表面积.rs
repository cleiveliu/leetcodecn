impl Solution {
    pub fn surface_area(grid: Vec<Vec<i32>>) -> i32 {
        let mut all_cubic: i32 = 0;
        let r = grid.len();
        let c = grid[0].len();
        for i in 0..r {
            for j in 0..c {
                all_cubic += grid[i][j];
            }
        }
        let mut e: i32 = 0;
        for i in 0..r {
            for j in 0..c {
                e += (grid[i][j] -1).max(0);
            }
        }
        for i in 0..r {
            for j in 0..c-1 {
                e += grid[i][j].min(grid[i][j+1]);
            }
        }
        for i in 0..c {
            for j in 0..r-1 {
                e += grid[j][i].min(grid[j+1][i]);
            }
        }
        
        return all_cubic*6 - e*2;
    }
}