#include<iostream>
#define PI 3.141592654

using namespace std;

class shape{
	public:
		virtual double area() const {return 0;}
		//virtual double area is default behavior
	protected:
		double x, y;
};

class rectangle: public shape
{
	public:
		rectangle(double h=0.0, double w=0.0): height(h), width(w){}
		double area() const {return (height * width);}
	private:
		double height, width;
};

class circle: public shape
{
	public:
		circle(double r =0.0): radius(r) {}
		double area() const {return (PI*radius*radius);}
	private:
		double radius;
};

const int N=3;

int main()
{
	shape* p[N];
	p[0] = new rectangle(2,3);
	p[1] = new rectangle(2.5, 2.001);
	p[2] = new circle(1.5);
	double tot_area = 0.0;
	for (int i=0;i<N;++i)
		tot_area += p[i]->area();
	cout << tot_area << " is total area" << endl;
}
		




