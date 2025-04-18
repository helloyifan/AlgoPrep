// g++ concatenation-of-array.cpp && a.out

#include <iostream>
#include <vector>
#include <string>
#include <iterator>

using namespace std;

class Solution {
    public:
        vector<int> getConcatenation(vector<int>& nums) {
            vector<int> numsCopy(nums);
            nums.insert(nums.end(), numsCopy.begin(), numsCopy.end());
                        
            copy(
                nums.begin(), nums.end(),
                ostream_iterator<int>(cout, " ")
            );
            return nums;
        }
};


int main() {
    Solution sol;
    vector<int> input = {1, 2, 1};
    sol.getConcatenation(input);
};