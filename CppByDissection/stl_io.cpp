//Use of istream_iterator and ostream_iterator
//
#include <iterator>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> d(5);
	int i, sum;
	cout << "enter 5 numbers" << endl;

	istream_iterator<int> in(cin);
	ostream_iterator<int> out(cout, "\t");

	sum = d[0] = *in;
	for(i=1; i< 5; ++ i){
		d[i] = *++in; // input consecutive values
		sum += d[i];
	}

	for (i=0;i<5;++i)
		*out = d[i];

	cout << "sum= " << sum << endl;
}

