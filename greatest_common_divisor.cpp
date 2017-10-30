#include<iostream>
#include<cstdlib>

using namespace std;

int gcd(int a, int b)
{

	// swap a and b
	if (a<b)
	{
		a = a^b; b = a^b; a = a^b;
	}

	if (a%b==0)
		return b;
	else
		return gcd(b, (a%b));
}


int main()
{
	srand(6);
	int a, b;
	for (int i=0; i<10; ++i)
	{
		a = rand(), b= rand();
		cout << " The greastest common divisor of " << a 
			<< " and " << b << " is " << gcd(a, b) 
			<< endl;
	}

}
