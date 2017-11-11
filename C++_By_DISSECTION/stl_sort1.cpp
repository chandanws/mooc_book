//Using sort() from STL

#include <iostream>
#include <algorithm>
using namespace std;

const int N=5;

int main()
{
	int d[N], i, *e = d+N;
	for(i=0;i<N;++i)
		d[i] = rand();
	sort(d,e);
	for(i=0;i<N;++i)
		cout << d[i] <<'\t';
	cout << endl;
}

