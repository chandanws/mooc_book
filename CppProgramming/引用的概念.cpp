#include <iostream>

using namespace std;

int main()
{
    int n=4;
    int & r= n;
    
    r=4;
    cout << r;
    cout << n;
    
    n=5;
    cout << r;
    cout << n;
    
    
    double a = 4, b = 5;
    double & r1 = a; // r2也引用 a
    double & r2 = r1;
    
    r2 = 10;
    cout << a << endl; // 输出 10
    r1 = b; // r1并没有引用b
    cout << a << endl; //输出 5
}
