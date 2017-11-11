#include <iostream>

using namespace std;

int n = 4;

int & SetValue() { return n; }

int main()

{
    SetValue() = 40;
    cout << n;
    return 0;
}
