/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int len, int target, int* returnSize){
    int* ret = (int *) malloc(sizeof(int)*2);
    *returnSize = 0;
    for (int i=0; i<len; i++) {
        for (int j=i+1; j<len;j++) {
            if (nums[i] + nums[j] == target) {
                ret[0] = i;
                ret[1] = j;
                *returnSize = 2;
                return ret;
            }
        }
    }
    return ret;
}