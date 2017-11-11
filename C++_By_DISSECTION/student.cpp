#include "student.h"

int main()
{
	//decare and initialize
	person abe(string("Abe Pohl"), 92, 'M');
	person sam(string("Sam Pohl"),66,'M');
	student phil(string("philip Pohl"), 68, 'M', 3.8, junior);
	student laura(string("Laura Pohl"), 12, 'F', 3.9, fresh);
	cout << abe << endl; // info on abe is printed
	cout << phil << endl; 

	person* ptr_person;
	ptr_person = &abe;
	ptr_person ->print();
	ptr_person = &phil;
	ptr_person-> print();

	cout << "older is " << older(abe, sam) << endl;
	cout << "older is " << older(abe, phil) << endl;
	cout << "older is " << older(laura, phil) << endl;
}
