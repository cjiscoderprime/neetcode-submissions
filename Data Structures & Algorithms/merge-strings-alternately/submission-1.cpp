class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res;
        int n = word1.size();
        int n2 = word2.size();
        bool result = true;
        int i = 0;
        int j = 0;

        while(i < n or j < n2){
            if(i < word1.size() && result == true){
                res += word1[i];
                i++;
                result = false;
            }
            if(j < word2.size() && result == false){
                res += word2[j];
                j++;
                result = true;
            }
        
        if(i == word1.size()){
            result = false;
        }
        if(j == word2.size()){
            result = true;
        }

        }
        return res;
    }
};