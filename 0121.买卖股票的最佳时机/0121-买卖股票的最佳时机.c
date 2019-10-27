

int maxProfit(int* prices, int len){
    int ret = 0;
    for (int i=0;i<len;i++) {
        for (int j=i;j<len;j++) {
            if (prices[j] - prices[i] > ret) {
                ret = prices[j] - prices[i];
            }
        }
    }
    return ret;
}

