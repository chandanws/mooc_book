#include <iostream> 
#include <numeric> 
#include <vector>
#include <algorithm>

using namespace std;

int d[] = { 3, 7 , -99, 0, 14, 19, 22, -34 };

int main() 
{
	int n = 0; 
	vector<int> intData(d, d+8);
	n = count_if(intData.begin(), intData.end(), bind2nd(less<int>(), 20)); 
	cout << n << " are less than 20 " << endl; 
	n = 0; 
	n = count_if(intData.begin(), intData.end(),bind2nd(equal_to<int>(), 14)); 
	cout << n << " are equal to 14 " << endl;
}
