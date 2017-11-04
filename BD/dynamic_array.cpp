#include<iostream>
#include<cassert>


using namespace std;

int main()
{
	int* data;
	int size;
	cout << "\nEnter array size: ";
	cin >> size;
	assert(size>0);

	data = new int[size]; // allocate array of ints
	assert(data!=0); // data !=0 allocatio OK
	for(int j=0; j< size; ++j)
	{
		cout << (data[j] = j) << '\t';
	}
	cout << "\n\n";
	delete [] data; //deallocate an array
}
