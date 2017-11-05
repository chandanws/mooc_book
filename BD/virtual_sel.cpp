#include <iostream>
using namespace std;


//Virtual function selection

class Base{
	public:
		virtual void print() const
		{
			cout << " inside Base" << endl;
		}
};


class Derived: public Base {
	public:
		//Virtual as well
		void print() const
		{
			cout << " inside Derived" << endl;
		}
};

int main()
{
	Base b;
	Derived f;
	Base * pb = &b; // points at a Base object

	pb-> print(); //call Base:: print()
	pb = &f;	// points at Derived object
	pb -> print(); //Call Derived:: print()
}

