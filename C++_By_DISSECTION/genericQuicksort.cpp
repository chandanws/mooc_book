#include<iostream>

using namespace std;


template <class T>
inline void swap(T& x, T& y)
{ 
   T t; 
   t = x;  
   x = y; 
   y = t; 
}

template <class T>
inline void order(T& x, T& y)
{
   if (x > y) swap(x, y);
}

//Forward declarations of auxiliary functions
template <class T>
bool find_pivot(T *left, T *right, T *pivot_ptr);

template <class T>
T* partition(T *left, T *right, T pivot);

template <class T>
void quicksort(T *left, T *right)
{
   T   *p, pivot;
   if (find_pivot(left, right, &pivot) == true) {
      p = partition(left, right, pivot);
      quicksort(left, p - 1);
      quicksort(p, right);
   }
}

template <class T>
T *partition(T *left, T *right, T pivot)
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

template <class T>
bool find_pivot(T *left, T *right, T *pivot_ptr)
{
   T   a, b, c, *p;
   a = *left;                           // left value
   b = *(left + (right - left) / 2);    // middle value
   c = *right;                          // right value
   order(a, b); 
   order(a, c);
   order(b, c);         // order these 3 values 
   if (a < b) {         // pivot will be higher of 2 values
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
   return false;           // all elements have the same value 
}

int main()
{
   cout << "quicksort\n";
   int a[12] = {7, 4, 3, 5, 2, 5, 8, 2, 1, 9, -6, -3};

   for (int i = 0; i < 12; i++)
      cout << a[i] << " , ";
   quicksort(a, a + 11);
   cout << "\n\nquicksorted\n";
   for (int i = 0; i < 12; i++)
      cout << a[i] << " , ";
   //Now use doubles
   double b[6] = {7.8, 4.9, 3.8, 5.0, 2.8, 5.3};
   for (int i = 0; i < 6; i++)
      cout << b[i] << " , ";
   quicksort(b, b + 5);
   cout << "\n\nquicksorted\n";
   for (int i = 0; i < 6; i++)
      cout << b[i] << " , ";
}