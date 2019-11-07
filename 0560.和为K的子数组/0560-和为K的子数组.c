int subarraySum(int* nums, int numsSize, int k){
    int len = numsSize + 1;
    int sums[len];
    for (int i=1; i<len;i++) {
        sums[i] = sums[i-1] + nums[i-1];
    }
    int ret = 0;
    for (int i=0;i<len;i++) {
        for (int j=i+1;j<len;j++) {
            if (sums[j] - sums[i] == k) {
                ret += 1;
            }
        }
    }
    return ret;
}