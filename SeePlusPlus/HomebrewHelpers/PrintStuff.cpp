#include <vector>
#include <iostream>

using namespace std;

template<typename T> //Template it to accept any type.

void printVector(vector<T>& input) { //& to avoid copying
    for (int i = 0; i < input.size(); i+= 1) {
            cout << input[i] << "\n";
    }
}
