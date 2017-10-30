#include<iostream>
using namespace std;

int foo(int n) 
{
	static int ++count; 

	if ( n <= 1) 
	{
		count = 0;
		cout << " count = " << count << endl;
		return n; 
	}
	else
		foo(n/3);
}


int main() 
{
	foo(21);
	foo(27);
	foo(243);
}

