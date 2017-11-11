//Adapt a stack from a vector

#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

int main()
{
	stack<string, vector<string> > str_stack;
	string quote[3] = {
		"The wheel that squeaks the loudest\n",
		" Is the one that gets the grease \n",
		"Josh Billings \n "};
	for (int i=0; i<3; ++i)
		str_stack.push(quote[i]);
	while(!str_stack.empty()){
		cout << str_stack.top();
		str_stack.pop();
	}
}

