
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 7    Standard Template Library
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


// Use of ostream_iterator iterator

#include <iostream>
#include <iterator>
using namespace std;

int main()
{
   int  d[5] = { 2, 3, 5, 7, 11 };          	// primes
   ostream_iterator<int> out(cout, "\t");

   for (int i = 0; i < 5; ++i)
      *out = d[i];
   cout << endl;
}