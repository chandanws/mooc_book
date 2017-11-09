#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

class CShape
{
public:
    virtual double Area() = 0; //纯虚函数
    virtual void PrintInfo() = 0;
};


class CRectangle:public CShape
{
public:
    int w,h;
    virtual double Area();
    virtual void PrintInfo();
};

class CCircle:public CShape {
public:
    int r;
    virtual double Area();
    virtual void PrintInfo();
};


class CTriangle:public CShape {
public:
    int a,b,c;
    virtual double Area();
    virtual void PrintInfo();
};


double CRectangle::Area() {
    return w * h;
}


void CRectangle::PrintInfo() {
    cout << "Rectangle:" << Area() << endl;
}


double CCircle::Area() {
    return 3.14 * r * r ;
}

void CCircle::PrintInfo() {
    cout << "Circle:" << Area() << endl;
}

double CTriangle::Area() {
    double p = (a+b+c)/2.0;
    return sqrt(p * ( p - a)*(p- b)*(p - c));
};

void CTriangle::PrintInfo() {
    cout << "Triangle:" << Area() << endl;
}

CShape * pShapes[100];
int MyCompare(const void * s1, const void * s2);

int main()
{
    
    int i; int n;
    CRectangle *pr; CCircle *pc; CTriangle *pt;
    cout << "Input the number of shapes: " << endl;
    cin >> n;
    
    for( i = 0;i < n;i ++ ) {
        char c;
        cout << "Input shape(R-rectangle, C-circle, T-triangle):" << endl;
        cin >> c;
        switch(c) {
                
            case 'R':
                pr = new CRectangle();
                cout << "Width and height:" << endl;
                cin >> pr->w >> pr->h;
                pShapes[i] = pr;
                break;
            
            case 'C':
                pc = new CCircle();
                cout << "radius: " << endl;
                cin >> pc->r;
                pShapes[i] = pc;
                break;
                
            case 'T':
                pt = new CTriangle();
                cout << "a, b, c of triangle: " << endl;
                cin >> pt->a >> pt->b >> pt->c;
                pShapes[i] = pt;
                break;
                
        }
        
    }
    
    qsort(pShapes, n, sizeof(CShape*), MyCompare);
    
    cout << "The area of shapes are" << endl;
    for( i=0; i<n; i++)
        pShapes[i]->PrintInfo(); //多态
    return 0;
    
}

int MyCompare(const void *s1, const void *s2)
{
    
    double a1,a2;
    CShape **p1 ; // s1,s2 是 void * ，不可写 “* s1”来取得s1指向的内容
    CShape **p2;
    
    p1 = (CShape **) s1; //s1,s2指向pShapes数组中的元素，数组元素的类型是CShape *
    p2 = (CShape **) s2; // 故 p1,p2都是指向指针的指针，类型为 CShape **
    a1 = (*p1)->Area(); // * p1 的类型是 Cshape* ,是基类指针，故此句为多态
    a2 = (*p2)->Area();
    
    if(a1<a2)
        return -1;
    else if (a2<a1)
        return 1;
    else
        return 0;
    
}
