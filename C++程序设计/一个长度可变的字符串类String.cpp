#include <string>
#include <iostream>
#include <cstring>
using namespace std;



class String {
private:
    char * str;
public:
    String () : str(NULL) { }
    //构造函数, 初始化str为NULL
    const char * c_str() { return str; }
    char * operator = (const char * s);
    ~String( );
};

//重载 ‘=’ obj = “hello”能够成立

char * String::operator = (const char * s){
    if(str) delete [] str;
    if(s) {
            //s不为NULL才会执行拷贝
            str = new char[strlen(s)+1];
            strcpy(str, s);
        }
    else
            str = NULL;
    return str;
}

String::~String( ) {
    if(str) delete [] str;
};

int main(){
    String s;
    s = "Good Luck," ;
    cout << s.c_str() << endl;
    // String s2 = “hello!”; //这条语句要是不注释掉就会出错
    s = "Shenzhou 8!";
    cout << s.c_str() << endl;
    return 0;
}
