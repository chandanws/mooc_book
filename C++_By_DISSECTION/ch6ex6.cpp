#include<iostream>
#include <cassert>


template <class T>
class vector {
public:
   typedef T* iterator;
   explicit vector(int n = 100);	// make size n array
   vector(const vector<T>& v);  	// copy vector
   vector(const T a[], int n);  	// copy an array
   ~vector() { delete []p; }
   iterator begin() { return p; }
   iterator end() { return p + size; }
   T& operator[](int i);     	// range-checked element
   vector<T>& operator=(const vector<T>& v);
   void print(); // print the entire vector range
private:
   T*  p;                    	// base pointer
   int  size;                	// number of elements
};


template <class T>
void vector<T>::print()
{
	iterator p;
	for(p=begin();p<end();++p)
	{
		std::cout << *p;
	}
}



template <class T> 
vector<T>::vector(int n) : size (n)
{ 
   assert(n > 0);
   p = new T[size];
   assert(p != 0);
}

template <class T>
vector<T>::vector(const T a[], int n)
{
   assert(n > 0);
   size = n;
   p = new T[size];
   assert(p != 0);
   for (int i = 0; i < size; ++i)
      p[i] = a[i];
}


template <class T>
vector<T>::vector(const vector<T>& v)
{
   size = v.size;
   p = new T[size];
   assert(p != 0);
   for (int i = 0; i < size; ++i)
      p[i] = v.p[i];
}

template <class T> T& vector<T>::operator[](int i) 
{ 
   assert (i >= 0 && i < size); 
   return p[i]; 
}


template <class T> 
vector<T>& vector<T>::operator=(const vector<T>& v) 
{ 
   assert(v.size == size); 
   for (int i = 0; i < size; ++i) 
      p[i] = v.p[i]; 
   return *this; 
}

int main()
{
	vector<int> a(10);
	vector<int>::iterator p;
	for(p=a.begin();p<a.end();++p)
		*p = 5;
	a.print();
}

