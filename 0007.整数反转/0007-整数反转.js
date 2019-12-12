/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if (x > Math.pow(2,31)-1 || x < Math.pow(-2,31)) {
        return 0;
    }
    let isNeg = x < 0? true: false;
    let ret = 0;
    x = Math.abs(x);
    while (x > 0) {
        ret = ret*10 + x%10;
        x  = x/10 >> 0;
    }
    if (ret > Math.pow(2,31)-1 || -ret < Math.pow(-2,31)) {
        return 0;
    }
    return isNeg? -ret: ret;
};