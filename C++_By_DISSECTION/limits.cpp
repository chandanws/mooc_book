
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 6    Templates and Generic Programming
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


#include <iostream>
#include <limits>
using namespace std;

int main()
{
   cout << numeric_limits<char>::digits 
        << " char\n ";
   cout << numeric_limits<unsigned char>::digits
        << " u  char\n";
   cout << numeric_limits<wchar_t>::digits 
        << " wchar_t\n";
   cout << numeric_limits<int>::max() 
        << " max int\n";
   cout << numeric_limits<double>::max() 
        << " max double " << endl;
}