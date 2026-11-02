class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> nset;
        for (int n : nums) {
            if (nset.count(n)) {
                return true;
            } else {
                nset.insert(n);
            }
        }
        return false;
    }
};