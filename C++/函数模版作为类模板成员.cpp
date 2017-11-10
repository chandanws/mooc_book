#include <iostream>

using namespace std;

template <class T>
class A{
public:
    template<class T2> void Func(T2 t){cout << t;}//成员函数模版
};

int main()
{
    A<int> a;
    a.Func('K'); //成员函数模版Func被实例化
    return 0;
}




