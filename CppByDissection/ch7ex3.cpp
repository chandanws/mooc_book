#include<iostream>
#include<vector>

using namespace std;

template<typename T>
T add_even(vector<T> &v)
{
	int i=0;
	T sum = 0;
	typename vector<T>::iterator p;
	for(p= v.begin(); p!= v.end();++p,++i)
	{
		if (i%2==0)
		   sum += *p;
	}
	return sum;
}

int main()
{
	vector<int> a(10);
	vector<double> b(10);
	for(int i=0;i<10;++i)
		a[i] =5, b[i] =5.1;
	cout<< add_even(a);
	cout << '\n';
	cout<< add_even(b);

}
