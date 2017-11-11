#include <iostream>
#include <cassert>

using namespace std;

template <class type, int n>
class stack
{
	public:
		explicit stack(int size=n): max_len(size), top(EMPTY), s(new type[size]){assert(s!=0);}
		~stack(){delete []s;}
		void reset(){top = EMPTY;}
		void push(type c) { s[++top] = c;}
		type pop() {return s[top--];}
		type top_of() const {return s[top];}
		bool empty() const { return top == EMPTY;}
		bool full() const {return top == max_len -1;}
	private:
		enum {EMPTY = -1};
		type* s;
		int max_len;
		int top;
};

int main()
{
	stack<int, 100> s1, s2;
}

using namespace std;
