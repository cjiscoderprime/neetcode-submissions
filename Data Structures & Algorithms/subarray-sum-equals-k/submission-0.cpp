class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int prefixsum = 0;

        unordered_map<int, int> freq;
        freq[0] = 1;

        for(int num: nums){
            prefixsum += num;

            int needed = prefixsum - k;

            if(freq.find(needed) != freq.end()){
                count += freq[needed];
            }
            freq[prefixsum]++;
        }
        return count;
    }
};