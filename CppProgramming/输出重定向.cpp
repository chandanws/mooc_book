#include <iostream>

using namespace std;

int main()
{
    int x,y;
    
    cin >> x >> y;
    freopen("test.txt","w",stdout); //将标准输出重定向到 test.txt文件
    
    if( y == 0 ) //除数为0则在屏幕上输出错误信息
        cerr << "error." << endl;
    else
        cout << x /y ; //输出结果到test.txt
    
    return 0;
    
}
