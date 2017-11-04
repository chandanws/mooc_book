
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 6    Templates and Generic Programming
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


#include <iostream>

// Generic swap

template <class T>
void swap(T& x, T& y)
{
   T  temp;

   temp = x;
   x = y;
   y = temp;
}


void swap(char* s1, char* s2)
{
   int  max_len;

   max_len = (strlen(s1) >= strlen(s2)) ?
              strlen(s1) : strlen(s2);
    char* temp = new char[max_len + 1];


   strcpy(temp, s1);
   strcpy(s1, s2);
   strcpy(s2, temp);
}

int main()
{

   int      i, j;
   char     str1[100], str2[100], ch1, ch2;

   char *s1 = str1, *s2 = str2;

   i = 0;
   j = 1;
   ch1 = 'A';
   ch2 = 'B';
   strcpy(str1, "ABCD");
   strcpy(str2, "EFGHIJKL");

   std::cout << "\nints:     " << i     << '\t' << j;
   std::cout << "\nchars:    " << ch1   << '\t' << ch2;
   std::cout << "\nstrings:  " << str1  << '\t' << str2;

   swap(i, j);                	//i j int - okay
   swap(str1[50], str2[33]);  	//both char variables-okay
 //  swap(i, ch1);              //i int ch char - illegal
 //  swap(str1, str2);          //illegal
   swap(s1, s2);       	        //legal- but may not be intention

   std::cout << "\nints:     " << i     << '\t' << j;
   std::cout << "\nchars:    " << ch1   << '\t' << ch2;
   std::cout << "\nstrings:  " << str1  << '\t' << str2;
}

