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
    
    //写入数据
    CStudent s;
    ofstream OutFile("students.dat", ios::out|ios::binary);
    
    cout << "Input Name and Score: ";
    while( cin >> s.szName >> s.nScore ) {
        if( strcmp(s.szName, "exit") == 0) //名字为exit则结束
            break;
        OutFile.write((char *) &s, sizeof(s));
    }
    
    OutFile.close();
    
    
    //读取数据
    ifstream inFile("students.dat", ios::in| ios::binary);
    if(!inFile){
        cout << "error" << endl;
        return 0;
    };
    
    while(inFile.read((char*) &s, sizeof(s))){
        int nReadedBytes = inFile.gcount(); //看刚才读了多少字节
        cout << s.szName << " " << s.nScore << endl;
    }
    
    inFile.close();
    
    return 0;
}
