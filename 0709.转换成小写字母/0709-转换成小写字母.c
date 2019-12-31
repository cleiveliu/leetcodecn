char * toLowerCase(char * str){
    char* dummy = str;
    while (*dummy != '\0') {
        int num = (int) *dummy;
        if (num >= 65 && num <= 90) {
            num += (97-65);
        }
        *dummy = (char) num;
        
        dummy++;
    }
    
    return str;
}