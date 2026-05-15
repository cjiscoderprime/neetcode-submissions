class Solution {
public:
    bool isValid(int l, int r, string s){
        while(l < r){
            if(s[l] != s[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }


    bool validPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        while(l < r){
        if(s[l] != s[r]){
            return(isValid(l+1, r, s) || isValid(l, r-1, s));
        }
        l++;
        r--;
    }
    return true;
    }
};