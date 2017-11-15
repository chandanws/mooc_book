#include <iostream>
#include <string>
#include <cstdlib>


using namespace std;


//pair类模版
template <class T1, class T2>
class Pair{
public:
    Pair(T1 k, T2 v): key(k), value(v){};
    string operator <(const Pair<T1, T2> &p) const;
    template<class A1, class A2> friend ostream & operator<<(ostream &out, const Pair<A1, A2> &p);
private:
    T1 key;
    T2 value;
};

template<class T1, class T2>
string Pair<T1, T2>::operator<(const Pair<T1, T2> &p) const
{
    if (key < p.key)
        return string("Yes!");
    else
        return string("No!");
}

template<class T1, class T2>
ostream& operator<<(ostream &out, const Pair<T1, T2> &p)
{
    return (out << p.key << ":" << p.value);
}



int main()
{
    Pair<string, int> student1("Tom", 19);
    Pair<string, int> student2("tai", 18);
    //实例化一个类Pair<string, int>
    cout << student1 << " is younger than " << student2 << "?  " << (student1 < student2)<< endl;
}
