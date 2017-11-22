// First Assignment
// Convert this program to C++
// change to C++ io
// change to one line comments
// change defines of constants to const
// change array to vector<>
// inline any short function

#include <iostream>
#include <vector>

using namespace std;

// Const N used to define data size
const int N=40;

// Return summation of a vector
void sum(int &p, vector<int> &d)
{
    int i;
    p = 0;
    for(i = 0; i < d.size(); ++i)
        p = p + d[i];
}

// Define a vector and then output its summation
int main()
{
    
    int i;
    int accum = 0;
    vector<int> data(N);
    for(i = 0; i < N; ++i)
        data[i] = i;
    
    sum(accum, data);
    cout << "The sum is " << accum << endl;
    return 0;
}
