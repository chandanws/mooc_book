#include<iostream>
#include<cstdlib>

using namespace std;

int gcd(int a, int b)
{

	static int fcn_calls = 1; // count the number of recursive
	// swap a and b
	if (a<b)
	{
		a = a^b; b = a^b; a = a^b;
	}

	if (a%b==0)
	{
		cout << "(Calls: " << fcn_calls << ") "<< endl;
		fcn_calls = 1; // set to 1;
		return b;
	}
	else
	{
		fcn_calls++;
		return gcd(b, (a%b));
	}
}


int main()
{
	srand(6);
	int a, b;
	for (int i=0; i<10; ++i)
	{
		a = rand(), b = rand();
		cout << " The greastest common divisor of " << a 
			<< " and " << b << " is " << gcd(a, b) 
			<< endl;
	}

}
