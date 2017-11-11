
/***************************************************************
*  C++ by Dissection    By Ira Pohl           Addison Wesley    
*  Chapter 6    Templates and Generic Programming
*  Compiled with Borland C++ Builder Version 5.0   Summer 2001  
***************************************************************/


#include <iostream>
using namespace std;

// Quicksort 
inline void swap(int& x, int& y)
{ 
   int  t; 
   t = x; 
   x = y; 
   y = t; 
}
inline void order(int& x, int& y)
{
   if (x > y) swap(x, y);
}
bool find_pivot(int *left, int *right, 
                int *pivot_ptr);

int* partition(int *left, int *right, int pivot);

void quicksort(int *left, int *right)
{
   int   *p, pivot;
   if (find_pivot(left, right, &pivot)) {
      p = partition(left, right, pivot);
      quicksort(left, p - 1);
      quicksort(p, right);
   }
}

bool find_pivot(int *left, int *right, 
                int *pivot_ptr)
{
   int   a, b, c, *p;
   a = *left;                         	// left value 
   b = *(left + (right - left) / 2);  	// middle value
   c = *right;                        	// right value 
   order(a, b); 
   order(a, c);
   order(b, c);   	// order these 3 values 
   if (a < b) {   	// pivot is higher of 2 values 
      *pivot_ptr = b;
      return true;
   }
   if (b < c) {
      *pivot_ptr = c;
      return true;
   }

   for (p = left + 1; p <= right; ++p)
      if (*p != *left) {
         *pivot_ptr = (*p < *left) ? *left : *p;
         return true;
      }
   return false;      	// all elements have same value 
}

int *partition(int *left, int *right, int pivot)
{
   while (left <= right) {
      while (*left < pivot)
       ++left;
      while (*right >= pivot)
       --right;
      if (left < right) {
       swap(*left, *right);
       ++left;
       --right;
      }
   }
   return left;
}
int main()
{
   cout << "quicksort\n";
   int a[12]={7, 4, 3, 5, 2, 5, 8, 2, 1, 9, -6, -3 };

   for (int i = 0; i < 12; i++)
      cout << a[i] << " , ";
   quicksort(a, a + 11);
   cout << "\n\nquicksorted\n";
   for (int i = 0; i < 12; i++)
      cout << a[i] << " , ";
   cout << endl;
}