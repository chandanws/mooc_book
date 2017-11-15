#include <iostream>

using namespace std;

class A {
public:
    virtual void f() = 0; //纯虚函数
    void g() {
        this->f( ); } //ok
    A( ){ } //f( ); // 错误
    //输出结果:
};

class B : public A{
public:
    void f(){
        cout<<"B: f()"<<endl; }
};

int main(){
    B b;
    b.g();
    return 0;
}
