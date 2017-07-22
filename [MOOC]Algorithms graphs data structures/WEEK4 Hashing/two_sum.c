### ERROR still exists



#include <iostream>
#include <fstream> 
#define MAX 10000 

using namespace std;  

int hash2[MAX + 1] = { 0 }; 
int sum = 0;

void readData()  
{	
	ifstream fin("two_sum.txt");	
	int temp = 0;	
	while(fin>>temp)	
	{		
		if(temp < MAX)				
			hash2[temp]++;	
	} 
}  
		
bool hashMap(int n)  
{		
	if(n > MAX)			
		return false;	
	if(hash2[n])		
		return true;	
	else		
		return false; 
}  

int main()  {	
	readData();		
	for(int i = -10000; i <= 10000; i++)	
	{		
		for(int j = -10000; j <= 10000; j++)		
		{			
			if(hashMap(j) && hashMap(i - j) && i != j)
			{
				sum = sum +1;				
				break;			
			}		
		}	
	}	
	return 0; 
}

