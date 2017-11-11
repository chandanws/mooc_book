#include <iostream>
#include <list>

using namespace std;

// using the list container

template<typename T>
void print(list<T> &lst)
{
	typename list<T>:: iterator p;

	for (p=lst.begin(); p!=lst.end();++p)
		cout << *p << '\t';
	cout << endl;
}

int main()
{
	double w[4] = {0.9, 0.8, 88, -99.99};
	list<double> z;

	for (int i=0; i< 4; ++i)
		z.push_front(w[i]);
	print(z);
}

