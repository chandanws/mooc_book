#include <vector>
#include <iostream>

using namespace std;

int main()
{
    //v有3个元素,
    //每个元素都是vector<int> 容器
    vector <vector<int> > v(3);
    
    for (int i=0; i< v.size(); ++i)
        for (int j=0; j<10; ++j)
            v[i].push_back(i*j);
    
    for (int i=0; i< v.size(); ++i){
        for (int j=0; j<v[i].size(); ++j)
            cout << v[i][j] << " ";
        cout << endl;
    }
    
    return 0;
}
