
#include <iostream>


//Recursive factorial function
//
//#include<iostream>

using namespace std;

//Recursive factorial function
//
long factorial (int n)
{
	if (n<=1)
		return 1;
	else
		return n*factorial(n-1);
}

int main()
{
	int i = 3;
	cout << "\n Factorial of 3 is " << factorial(i) << endl;
}
