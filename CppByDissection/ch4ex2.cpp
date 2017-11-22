# include <iostream>

using namespace std;

struct point {
	public:
		point(double x1, double x2, double x3):x(x1), y(x2), z(x3){}
		void print();
	private:
		double x,y,z;
};

void point::print()
{
	cout << "(" << x << "," << y << "," << z << ")" << endl;
}


int main()
{
	point z(1.1,1.2,4.5);
	z.print();
}






	


