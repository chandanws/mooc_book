
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 6    Templates and Generic Programming
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


#include "vect_it.h"
#include <iostream>

int main() 
{ 
   vector<double> v(5); 
   vector<double>::iterator p; 
   int  i = 0;

   for (p = v.begin(); p != v.end(); ++p) 
      *p = 1.5 + i++; 

   do { 
      --p; 
      std::cout << *p << " , "; 
   } while (p != v.begin()); 
   std::cout << std::endl; 
}