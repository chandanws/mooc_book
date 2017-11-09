//赋值兼容原则引起函数模板中类型参数的二义性
# include <iostream>

using namespace std;


template<class T>
T myFunction(T arg1, T arg2)
{
    cout << arg1 << " " << arg2 << "\n";
    return arg1;
}

int main(){
    myFunction(5,7); //ok: replace T with int
    myFunction(5.8, 8.4); // ok: replace T with double
    myFunction(5, 8.4); //error: replace T with int or double? 二义性
}
