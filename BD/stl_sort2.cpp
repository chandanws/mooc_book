#include <iostream>
#include <algorithm>

using namespace std;

//Using sort() from STL

//Class MyLess works for any class T that has operator<() defined

template <class T>
class MyLess{
	public:
		bool operator()(const T& x, const T &y)
		{ return x < y;}
};

template <class T>
bool MyGreater(const T& x, const T &y)
{ return x > y;}

const int N=5;


int main()
{
	int i, d[N], *e = d+N;
	MyLess<int> myLessObj;

	for (i=0;i<N;++i)
		d[i] = rand()%100;
	sort(d,e, MyLess<int>()); //Use comparison class
	for(i=0; i< N;++i)
		cout << d[i] << '\t';
	cout << endl;
	sort(d,e,MyGreater<int>); //Use comparison func
	for (i=0;i<N;++i)
		cout << d[i] << '\t';
	cout << endl;
	sort(d,e, myLessObj); //use comparison method
	for(i=0;i<N;++i)
		cout <<d[i] <<'\t';
	cout << endl;
}
