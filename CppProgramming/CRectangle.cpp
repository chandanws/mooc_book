#include <iostream>

using namespace std;

// class CRectangle
class CRectangle
{
private:
    int w, h;
    static int nTotalArea;
    static int nTotalNumber;
    
public:
    CRectangle(int w_,int h_);
    ~CRectangle();
    static void PrintTotal();
    CRectangle(CRectangle & r );
};

//CRectangle::CRectangle
CRectangle::CRectangle(int w_,int h_)
{
    w = w_;
    h = h_;
    nTotalNumber ++;
    nTotalArea += w * h;
}

//CRectangle::~CRectangle
CRectangle::~CRectangle()
{
    nTotalNumber --;
    nTotalArea -= w * h;
}

//在静态成员函数中，不能访问非静态成员变量， 也不能调用非静态成员函数。

void CRectangle::PrintTotal()
{
    cout << nTotalNumber << "," << nTotalArea << endl;
}

CRectangle :: CRectangle(CRectangle & r ) {
    w = r.w;
    h = r.h;
    nTotalNumber ++;
    nTotalArea += w * h;
}

//必须在定义类的文件中对静态成员变量进行一次说明
//或初始化。否则编译能通过，链接不能通过。
int CRectangle::nTotalNumber = 0;
int CRectangle::nTotalArea = 0;

int main()
{
    CRectangle r1(3,3), r2(2,2);
    //cout << CRectangle::nTotalNumber; // Wrong , 私有
    CRectangle::PrintTotal();
    r1.PrintTotal();
}
