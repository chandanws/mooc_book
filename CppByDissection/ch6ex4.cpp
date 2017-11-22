#include<iostream>

using namespace std;

template<typename type>
void exchange(type&a, type&b, type&c)
{
	//replace a's value by b's and b's by c's
	//and c's by a's
	type temp;
	temp = b;
	b = c;
	c = a;
	a = temp;
}

int main()
{
	int a=5,b=4,c=3;
	cout <<"a,b,c = "<< a << "," << b << ","  << c << endl;
	exchange(a,b,c);
	cout <<"a,b,c = "<< a << "," << b << ","  << c << endl;
}
