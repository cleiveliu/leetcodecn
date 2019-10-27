

void reverseString(char* s, int len){
    int l = 0, r = len-1;
    while (l < r) {
        char temp = s[l];
        s[l] = s[r];
        s[r] = temp;
        l += 1;
        r -= 1;
    }
}

