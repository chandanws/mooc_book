#include <iostream>
using namespace std;

class CSample{
    int x;
public:
    CSample(){
        cout << "Constructor 1 Called" << endl;
    }
    CSample(int n){
        x = n;
        cout << "COnstructor 2 Called" << endl;
    }
    ~CSample(){
        cout << "Destructor Called" << endl;
    }
};

int main()
{
    CSample array1[2];
    cout << "step1" << endl;
    
    CSample array2[2] = {4,5};
    cout << "step2" << endl;
    
    CSample array3[2] = {3};
    cout << "setp3" << endl;
    
    CSample *array4 = new CSample[2];
    delete[] array4;
    return 0;
}
