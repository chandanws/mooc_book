
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

const int SIZE = 100;

// A typical container algorithm

template <typename T>
T sum(deque<T> &dq)
{ 
   T s = 0;

   for(typename deque<T>::iterator p = dq.begin(); p != dq.end(); ++p)
      s += *p;
   return s;
}

int main()
{
	vector<double> vec(SIZE, 0);   //changed form int to double
	deque<double> deq;             //ditto and later iterator
	int i;
	double sumTotal;
                                 // init and output vec
	for(i = 0; i < SIZE; i++){
	   vec[i] = i * 0.6; cout << vec[i] <<"\t";
	}

   deq.push_front(vec.front()); // add an element to the front
   deq.push_back(vec.back());   // add an element to the back

   // Insert the remaining elements from the vector between
   // the first and last deque elements
   //
   deq.insert(deq.begin()+1, vec.begin()+1, vec.end()-1);

   sumTotal = sum(deq);
   cout << "The sum of the deque is : " << sumTotal << endl;
}
