#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int main(){
    int i;
    vector<int> v(10);
    
    
    for (i=0;i<v.size();i++)
        v[i]= i*2-1; // 根据下标随机访问
    
    vector<int>::const_iterator ii;
    for(ii=v.begin(); ii!=v.end();ii++)
        cout << *ii << ", ";
    cout << endl << endl;
    
    
    for(ii=v.begin();ii<v.end();ii++)
        cout << *ii << ", ";
    cout << endl << endl;
    
    //间隔一个输出；
    ii=v.begin();
    while(ii<v.end()){
        cout << *ii << ", ";
        ii += 2;
    }
    cout << endl;
    
    
}
