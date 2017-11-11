
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 7    Standard Template Library
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


// Compare iterator and pointer traversal

#include <iostream>
#include <set>
using namespace std;

int main()
{
   int  primes[4] ={ 2, 3, 5, 7 }, *ptr = primes;
   set<int, greater<int> > s;
   set<int, greater<int> > :: const_iterator c_it;
   while (ptr != primes + 4)
      s.insert(*ptr++);

   cout << "The primes below 10 : " << endl;
   for (c_it = s.begin(); c_it != s.end(); ++c_it)
      cout << *c_it << '\t';
   cout << endl;
}