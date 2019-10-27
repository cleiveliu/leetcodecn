bool judgeSquareSum(int c){
    if (c < 0) {
        return false;
    }
    long long int left = 0;
    long long int right =  (sqrt(c) + 1);
    
    while (left <= right) {
        int val = left*left + right*right;
        if (val == c) {
            return true;
        } else if (val > c) {
            right -= 1;
        } else {
            left += 1;
        }
    }
    
    return false;
}