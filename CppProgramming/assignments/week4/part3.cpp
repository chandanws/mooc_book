#include <iostream>
#include <cstring>
#include <vector>

using namespace std;


class Array2
{
public:
    Array2(int i=1, int j=1): x(i), y(j), a(i){
        vector<int> b(y,0);
        for (int i=0; i< x; i++)
            a[i] = b;
    };
    
    vector<int> & operator[](int index){return a[index];}
    int & operator()(int index_i, int index_j) {return a[index_i][index_j];}
    Array2 & operator=(Array2 _array){a = _array.a; return *this;}
private:
    int x, y;
    vector<vector<int> > a;
    
};


int main() {
    Array2 a(3,4);
    int i,j;
    for(i = 0;i < 3; ++i )
        for(j = 0; j < 4; j++)
            a[i][j] = i * 4 + j;
    for( i=0;i<3; ++i) {
        for( j = 0; j < 4; j ++ ) {
            cout << a(i,j) << ",";
        }
        cout << endl;
    }
    
    cout << "next" << endl;
    
    Array2 b;
    b = a;
    for(  i = 0;i < 3; ++i ) {
        for(  j = 0; j < 4; j ++ ) {
            cout << b[i][j] << ",";
        }
        cout << endl;
    }
    return 0;
}
