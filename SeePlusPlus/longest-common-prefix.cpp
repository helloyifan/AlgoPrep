
#include <iostream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;

class Solution {
    public:
    string longestCommonPrefix(vector<string>& strs) {
        
        //Custom sort function for shorted to longest
        sort(strs.begin(), strs.end(), [](const string& a, const string& b) {
            return a.size() < b.size();
        });
        string ret;
        string& firstWord = strs[0]; 

        for (int i = 0; i < firstWord.size(); i++) { 
            for (string& curStr: strs) { // note string curStr also works, but then we are copying a string everytime 
                if (firstWord[i] != curStr[i]) {
                    return ret; // Fail fast
                }
            }
            //If we get to the end, append
            ret += firstWord[i];
        }
        return ret;
    }
};

int main() {
    Solution sol;
    vector<string> input = {"flower","flow","flight"};
    string ret = sol.longestCommonPrefix(input);
    cout << ret << endl;

};