impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut buy = std::i32::MAX;
        let mut sell = 0;
        for price in prices {
            if price < buy {
                buy = price;
            } else {
                sell = price;
                profit = profit.max(sell-buy);
            }
        }
        
        profit
    }
}