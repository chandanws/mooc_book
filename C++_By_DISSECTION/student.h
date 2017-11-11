#include "person.h"

enum year{fresh, soph, junior, senior};
const string year_label[] = {"freshman", "sophomore", "junior", "senior"};

class student: public person{
	public:
		student(const string& nm, int a, char g, double gp, year yr):
			person(nm, a, g), gpa(gp), y(yr) {}
		void print() const { cout <<*this << endl;}
		friend ostream& operator << (ostream& out, const student& s);
	protected:
		double gpa;
		year y;
};

ostream& operator << (ostream&out, const student & s)
{
	return (out << static_cast<person>(s) << ", " << year_label[s.y] << ",  gap= " << s.gpa);
}
