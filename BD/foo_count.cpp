#include<iostream>
using namespace std;

int foo(int n) 
{
	static int count = 0;

	++count; 

	if ( n <= 1) 
	{
		cout << " count = " << count << endl;
		return n; 
	}
	else
		return foo(n/3);
}


int main() 
{
	foo(21);
	foo(27);
	foo(243);
}

