#include <list>
#include <iostream>
#include <algorithm>

using namespace std;


//定义类A, 并以友元重载<, ==和<<
class A {
private:
    int n;
public:
    A(int n_) {
        n=n_;
    }
    friend bool operator<( const A & a1, const A & a2);
    friend bool operator==( const A & a1, const A & a2);
    friend ostream & operator <<( ostream & o, const A & a);
};

bool operator<( const A & a1, const A & a2) {
    return a1.n < a2.n;}

bool operator==( const A & a1, const A & a2) {
    return a1.n == a2.n;}

ostream & operator <<( ostream & o, const A & a) {
    o << a.n;
    return o;
}


//定义函数模板PrintList, 打印列表中的对象
template <class T>void PrintList(const list<T> & lst) {
    int tmp = lst.size();
    
    if( tmp > 0 ) {
        typename list<T>::const_iterator i;
        i = lst.begin();
        for(i = lst.begin(); i != lst.end(); i ++)
            cout << * i << ",";
    }
}


int main() {
    list<A> lst1,lst2;
    lst1.push_back(1); lst1.push_back(3);
    lst1.push_back(2); lst1.push_back(4); lst1.push_back(2);
    lst2.push_back(10); lst2.push_front(20);
    lst2.push_back(30); lst2.push_back(30);
    lst2.push_back(30); lst2.push_front(40); lst2.push_back(40);
    
    // print list
    cout << "1) "; PrintList( lst1); cout << endl;
    cout << "2) "; PrintList( lst2); cout << endl;
    
    //list容器的sort函数
    lst2.sort();
    cout << "3) "; PrintList( lst2); cout << endl;
    lst2.pop_front();
    cout << "4) "; PrintList( lst2); cout << endl;
    
    //删除所有和A(2)相等的元素
    lst1.remove(2);
    cout << "5) "; PrintList( lst1); cout << endl;
    
    //删除所有和前一个元素相等的元素
    lst2.unique();
    cout << "6) "; PrintList( lst2); cout << endl;
    
    //合并 lst2到lst1并清空lst2
    lst1.merge (lst2);
    cout << "7) "; PrintList( lst1); cout << endl;
    cout << "8) "; PrintList( lst2); cout << endl;
    
    // reverse()
    lst1.reverse();
    cout << "9) "; PrintList( lst1); cout << endl;
    
    lst2.push_back (100); lst2.push_back (200);
    lst2.push_back (300); lst2.push_back (400);
    
    //将[p2,p3)插入p1之前，并从lst2中删除[p2, p3)
    list<A>::iterator p1, p2, p3;
    p1 = find(lst1.begin(), lst1.end(), 3);
    p2 = find(lst2.begin(), lst2.end(), 200);
    p3 = find(lst2.begin(), lst2.end(), 400);
    cout << "lst1"; PrintList(lst1); cout << endl;
    cout << "lst2"; PrintList(lst2); cout << endl;

    lst1.splice(p1, lst2, p2, p3);
    cout << "11) lst1 "; PrintList( lst1); cout << endl;
    cout << "12) lst2"; PrintList( lst2); cout << endl;
}



