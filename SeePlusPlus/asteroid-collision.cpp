#include <cstdlib>
#include <iostream>
#include <vector>

#include "HomebrewHelpers/PrintStuff.cpp"

using namespace std;

class Solution {
public:
  vector<int> asteroidCollision(vector<int> &asteroids) {
    bool flag = true;
    vector<int> *stack = new vector<int>;

    for (int i = 0; i < asteroids.size(); i++) {
      int cur = asteroids[i];
      int curVelocity = abs(cur);
      bool curSmashed = false;
      if (cur > 0) {
        stack->push_back(cur);
      } else if (cur < 0) {
        // Smash rocks
        while (stack->size() > 0 && stack->back() > 0 && !curSmashed) {
          // cur backwards moving smashed
          if (stack->back() > curVelocity) {
            curSmashed = true;
            // both smashed
          } else if (stack->back() == curVelocity) {
            stack->pop_back();
            curSmashed = true;
            // top stack smashed, cur backwards moving smashes
          } else if (stack->back() < curVelocity) {
            stack->pop_back();
          }
        }

        // if its going the negative way
        if (!curSmashed) {
          if (stack->size() == 0 || stack->back() < 0) {
            stack->push_back(cur);
          }
        }
      } else {
        throw("shouldn't be possible");
      }
    }
    return *stack;
  }
};

int main() {
  cout << "yep its a main function \n";
  Solution *sol = new Solution();

  // vector<int>* test1 = new vector<int>{2, 4, -4, -1};

  // vector<int> ret1 = (*sol).asteroidCollision(*test1);
  // printVector(ret1);

  vector<int> *test2 = new vector<int>{-5, -5};
  vector<int> ret2 = (*sol).asteroidCollision(*test2);
  printVector(ret2);
}