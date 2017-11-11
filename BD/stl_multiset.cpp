// Associative Containers - checking up on your diet
//
#include <iostream>
#include <set> //used for both set and multiset
#include <vector>
#include <cstdlib>

using namespace std;

enum vegetables { broccoli, tomato, carrot, lettuce, beet, radish, potato};

int main()
{
	vector<vegetables> my_diet(100);
	vector<vegetables>:: iterator pos;
	vegetables veg;
	multiset<vegetables, greater<vegetables> > v_food;
	multiset<vegetables, greater<vegetables> >:: iterator vpos;

	for (pos = my_diet.begin(); pos != my_diet.end(); ++ pos)
	{
		*pos = static_cast<vegetables>(rand() %7);
		v_food.insert(*pos);
	}

	cout << "How often a vegetable is eaten." << endl;
	cout << " broccoli, tomato, carrot, lettuce,"
		<< "beet, radish, potato " << endl;
	for (veg = broccoli; veg <= potato;
			veg = static_cast<vegetables>(veg+1))
		cout << v_food.count(veg) << endl;
	cout << "\n Offering of vegetables" << endl;
	for (vpos = v_food.begin(); vpos!= v_food.end(); ++ vpos)
		cout << *vpos << '\t';
	cout << endl;
}

