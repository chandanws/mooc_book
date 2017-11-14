#include <iostream>

using namespace std;

class CDemo {
private:
    int n;
public:
    CDemo(int i=0):n(i) { }
    CDemo & operator++();    //用于前置++形式
    CDemo operator++(int);     //用于后置++形式
    operator int ( ) { return n; } //int 作为一个类型强制转换运算符被重载
    friend CDemo & operator--(CDemo &); //用于前置--形式
    friend CDemo operator--(CDemo &, int); //用于后置--形式
};

//前置 ++
CDemo & CDemo::operator++() {
    n++;
    return * this;
}

//后置 ++
CDemo CDemo::operator++(int k) {
    CDemo tmp(*this); //记录修改前的对象
    n++;
    return tmp;
    //返回修改前的对象
}

CDemo & operator--(CDemo & d) {
    //前置--
    d.n--;
    return d;
}

CDemo operator--(CDemo & d, int) {
    //后置--
    CDemo tmp(d);
    d.n--;
    return tmp;
}

int main(){
    CDemo d(5);
    cout << (d++) << ","; //等价于 d.operator++(0);
    cout << d << ",";
    cout << (++d) << ",";
    cout << d << endl;
    cout << (d--) << ",";
    cout << d << ",";
    cout << (--d) << ",";
    cout << d << endl;
    return 0;
}
