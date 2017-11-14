#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

class Complex {
private:
    double r,i;
public:
    void Print() {cout << r << "+" << i << "i" << endl;}
    Complex & operator = (string c);
};

Complex & Complex:: operator =(string c)
{
    int pos = c.find("+"); //the position of "+"
    r = atof(c.substr(0, pos).c_str());
    i = atof(c.substr(pos+1, c.length()-pos-2).c_str());
    return *this;
}


int main() {
    Complex a;
    a = "3+4i"; a.Print();
    a = "5+6i"; a.Print();
    return 0;
}
