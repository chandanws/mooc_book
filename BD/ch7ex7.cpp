#include <iostream> 
#include <list> 
#include <vector> 
#include <set> 

using namespace std;



template <class Iterator>
Iterator secondLargest(Iterator b, Iterator e)
{

	Iterator max1 = b, max2 = ++b, t; 
	if (*max1 < *max2){ 
		t = max1;
		max1 = max2;
		max2 = t;
	} 

	for (++b; b != e; ++b)
		if (*b >= *max1)
			{
				max2 = max1; 
				max1 = b;
			}
		else 
			if(*b > *max2)
				max2 = b; 

	return max2;
}

int d[] = { 3, 7 , -99, 0, 14, 19, 22, -34 };

int main() {
	list<int> intData(d, d+8) ;
	cout << "2nd largest is " 
	<< (*secondLargest(intData.begin(), intData.end())) 
	<< endl; 
}


