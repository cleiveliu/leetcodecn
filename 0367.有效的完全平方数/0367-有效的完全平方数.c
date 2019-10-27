bool isPerfectSquare(int num){
    if (num < 0) {
        return false;
    }
    long long int num2 = (long long int) num;
    for (long long int i = 0; i< num2+1; i++) {
        if (i*i == num2) {
            return true;
        } else if (i*i > num2) {
            return false;
        }
    }
    return false;
}