#include <iostream>

using namespace std;

class MyInt  {
private:
    int nVal;
public:
    MyInt(int n) { nVal = n; }
    int ReturnVal() { return nVal; }
    // 在此处补充你的代码
    MyInt& operator-(int a)
    {
        nVal -= a;
        return *this;
    }
    
};


int main ()  {
    MyInt objInt(10);
    objInt-2-1-3;
    cout << objInt.ReturnVal();
    cout <<",";
    objInt-2-1;
    cout << objInt.ReturnVal();
    return 0;
}
