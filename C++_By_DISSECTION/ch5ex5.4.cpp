//Overloading functions

#include <iostream>
using namespace std;


// Overloading functions

class rational {
public:
   rational(int n = 0) : a(n), q(1) { }
   rational(int i, int j);
   rational(double r) : a(static_cast<long>
                         (r * BIG)), q(BIG) { }
   void  print() const { cout << a << " / " << q; }
   operator double() 
              { return static_cast<double>(a) / q; }
private:
   long  a, q;
   enum { BIG = 100 };
};

int gcd(int i, int j)
{
	if (i%j==0)
		return j;
	else
		return gcd(j, i%j);
}


inline rational::rational(int i, int j)
{
	int m = gcd(i,j);
	a = i/m;
	q = j/m;
}


inline int     greater(int i, int j) 
      { return (i > j ? i : j); }

inline double  greater(double x, double y)
      { return (x > y ? x : y); }

inline rational greater(rational w, rational z)
      { return (w > z ? w : z); }

int main()
{
   int     i = 10, j = 5;
   float   x = 7.0;
   double  y = 14.5;
   rational w(10), z(3.5), zmax;

   cout << "\ngreater(" << i << ", " << j << ") = "
        << greater(i, j);
   cout << "\ngreater(" << x << ", " << y << ") = "
        << greater(x, y);
   cout << "\ngreater(" << i << ", ";
   z.print();
   cout << ") = "
        << greater(static_cast<rational>(i), z);
   zmax = greater(w, z);
   cout << "\ngreater("; 
   w.print();
   cout << ", ";
   z.print();
   cout << ") = ";
   zmax.print();
   cout << endl;
}
