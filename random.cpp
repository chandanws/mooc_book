#include<iostream>
#include<cstdlib>

using namespace std;

void prn_random_numbers(int k)
{
	int r, biggest, smallest;

	r = biggest = smallest = rand();
	cout << endl << r;

	for (int i=1; i< k; ++i)
	{
		if (i%5==0)
			cout << endl;
		else
			cout << '\t';
		r = rand();
		biggest = r > biggest ? r : biggest;
		smallest = r < smallest ? r : smallest;
		cout << r;
	}
	cout << endl << "\n\nCount: " << k
		<< "\n Maximum: " << biggest
		<< "\n Minimum: " << smallest << endl;
}


int main(void)
{
	int n, seed;

	cout << "\n some random numbers will be printed.";
	cout << "\n Enter how many you want? " << endl;

	cin >> n;
	cout << "Enter seed number: ";
	cin >> seed;
	srand(seed);
	prn_random_numbers(n);
}


