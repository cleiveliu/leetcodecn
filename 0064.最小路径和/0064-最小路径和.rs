impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let r = grid.len();
        let c = grid[0].len();
        for i in 1..c {
            grid[0][i] += grid[0][i-1];
        }
        for i in 1..r {
            grid[i][0] += grid[i-1][0];
        }
        for i in 1..r {
            for j in 1..c {
                grid[i][j] += grid[i-1][j].min(grid[i][j-1]);
            }
        }
        return grid[r-1][c-1];
    }
}