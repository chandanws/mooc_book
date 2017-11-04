#include <cstdlib>
#include <iostream>
using namespace std;

class ch_stack {
public:
   void  reset() { top = EMPTY; }
   void  push(char c);
   char  pop();
   char  top_of() const { return s[top]; }
   bool  empty() const { return (top == EMPTY); }
   bool  full() const { return (top == FULL); }
private:
   enum { max_len = 10, EMPTY = -1, 
          FULL = max_len - 1 };
   char  s[max_len];
   int   top;
};

void ch_stack:: push(char c)
{
	if (full())
	{
		cerr << "Error: The stack is full.";
		exit(1);
	}
	s[++top] = c;
}

char ch_stack:: pop()
{
	if (empty())
	{
		cerr << "Error: The stack is empty.";
		exit(1);
	}
	return s[top--];
}



// Reverse a string with a ch_stack

int main()
{
   ch_stack  s;
   char   str[40] = { "My name is Don Knuth!" };
   int    i = 0;

   cout << str << endl;
   s.reset();            	// s.top = EMPTY; is illegal
   while (str[i])
      s.push(str[i++]);
}
