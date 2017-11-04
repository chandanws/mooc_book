/* Compute a table of cubes. */ 
#include <iostream> 
using namespace std;

const int  N = 15;
const double MAX = 3.5;

double cube(double x)
{
	return (x * x * x); 
}

int main() 
{
	int i;

	printf("\n\nINTEGERS\n"); 
	for (i = 1; i <= N; ++i) 
		cout << "cube (" << i << ")= "  << cube(i) << endl; 
	
	printf("\n\nREALS\n");
	for (double x = 1; x <= MAX; x += 0.3)
		cout << "cube (" << x << ")= "  << cube(x) << endl; 
}

