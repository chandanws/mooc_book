#include <iostream>
using namespace std;


template<typename T>
void bubble(T d[], T how_many) 
{
	T temp; 
	for (int i = 0; i < how_many - 1; ++i)
		for (int j= 0; j < how_many - 1 - i; ++j)
			if (d[j] < d[j + 1]) 
				{
					temp = d[j]; 
					d[j]= d[j + 1]; 
					d[j + 1] = temp;
				}

}


int main()
{
	int t[10]={10,9,8,7,6,5,4,3,2,1};
	bubble(t,10);
	for(int i=0;i<10;++i)
		cout << t[i] << ",";
	cout << endl;
}








