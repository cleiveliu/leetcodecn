int lengthOfLongestSubstring(char * s){
    int ret = 0;
    int dict[256] = {0};
    int left = 0;
    int right = 0;
    while (*s != '\0') {
        int key = *s - 0;
        if (dict[key] > left) {
            left = dict[key];
        }
        ret = ret > right - left + 1 ? ret : right - left + 1;
        s++;
        right += 1;
        dict[key] = right;
    }
    return ret;
}