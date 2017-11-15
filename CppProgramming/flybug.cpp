#include<iostream>

using namespace std;


class Skill {
public:
    Skill(int n) { cout << "Skill constructed" << endl;}
    ~Skill(){cout << "Skill destructed" << endl; }
};


class Bug {
private :
    int nLegs;
    int nColor;
    
public:
    int nType;
    Bug (int legs, int color){cout << "Bug constructed" << endl;};
    void PrintBug () { };
    ~Bug () {cout << "Bug destructed" << endl;}
};


class FlyBug: public Bug {
    int nWings;
    Skill sk1, sk2;
public:
    FlyBug(int legs, int color, int wings);
    ~FlyBug() { cout << "FlyBug destructed " << endl;}
};

FlyBug::FlyBug( int legs, int color, int wings):
Bug(legs, color), sk1(5), sk2(color)
{
    cout << "FlyBug constructed" << endl;
};

int main()
{
    FlyBug a(5, 4, 3);
}
