#include <iostream>
#include <string>

using namespace std;

//Overloaded get_age() and operator <<


class person
{
	public:
		person(const string& nm, int a, char g):
			name(nm), age(a), gender(g) {}
		virtual void print() const {cout << *this << endl;}
		friend ostream& operator << ( ostream& out, const person& p);
		int get_age() const {return age;}
	protected:
		string name;
		int age;
		char gender; //male='M', female='F'
};


ostream& operator << (ostream& out, const person & p)
{
	return (out << p.name << ", age is " << p.age
			<< ", gender is " << p.gender);
}

//older can work with student as well
const person& older(const person& a, const person&b)
{
	if (a.get_age() >= b.get_age())
		return a;
	else
		return b;
}



