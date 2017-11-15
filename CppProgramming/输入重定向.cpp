#include <iostream>

using namespace std;

int main()
{
    double f;
    int n;
    freopen("test.txt", "r", stdin); //cin被改为从 t.txt中读取数据
    cin >> f >> n;
    cout << f << ", " << n << endl;
    return 0;
}
