//下面的程序从键盘输入几个学生的姓名的成绩,
//并以二进制, 文件形式存起来

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

class CStudent {
public:
    char szName[20];
    int nScore;
};

int main()
{
    
    CStudent s;
    ofstream OutFile("students.dat", ios::out|ios::binary);
    
    while( cin >> s.szName >> s.nScore ) {
        if( strcmp(s.szName, "exit") == 0) //名字为exit则结束
            break;
        OutFile.write((char *) &s, sizeof(s));
    }
    
    OutFile.close();
    return 0;
}
