#include <vector>
#include <iostream>
#include "HomebrewHelpers/PrintStuff.cpp"

using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int f = 0;
        int b = s.size() - 1;
        while (f < b)
        {
            char temp = s[f];
            s[f] = s[b];
            s[b] = temp;
            f += 1;
            b -= 1;
        }
    }
};

int main()
{
    Solution sol;
    vector<char> input = {'a', 'b', 'c'};
    sol.reverseString(input);
    printVector(input);
};