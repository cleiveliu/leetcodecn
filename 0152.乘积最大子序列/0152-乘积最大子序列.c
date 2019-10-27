
int maxProduct(int* nums, int numsSize){
    int mmin(int, int, int);
    int mmax(int, int, int);
    if (numsSize == 0) {
        return 0;
    }
    int ret = nums[0];
    int pre_min  = nums[0], pre_max = nums[0];
    for (int i=1;i<numsSize;i++) {
        ret = mmax(ret, pre_min*nums[i], pre_max*nums[i]);
        ret = (ret > nums[i])? ret: nums[i];
        int temp = pre_max;
        pre_max = mmax(pre_max*nums[i], pre_min*nums[i], nums[i]);
        pre_min = mmin(pre_min*nums[i], temp*nums[i], nums[i]);
    }
    return ret;
}

int mmin(int a, int b, int c) {
    int ret;
    ret = (a>b)? b: a;
    ret = (ret>c)? c:ret;
    return ret;
}

int mmax(int a,int b, int c) {
    int ret;
    ret = (a>b)? a: b;
    ret = (ret > c)? ret: c;
    return ret;
}