
class ch_stack {
public:
//the public interface for the ch_stack
   ch_stack() : max_len(100),top(EMPTY)
       { s = new char[100]; assert(s != 0); }
      explicit ch_stack(int size) : 
      max_len(size), top(EMPTY)
      { assert(size > 0); s = new char[size];
        assert(s != 0); }
   ch_stack(int size, const char str[]);
   ch_stack(const ch_stack& str) : 
                   max_len(str.max_len), top(str.top)
      { s = new char[str.max_len]; assert(s != 0);
        memcpy(s, str.s, max_len); }
   ~ch_stack() { delete []s; }  	//destructor
   void  reset() { top = EMPTY; }
   void  push(char c) { s[++top]= c; }
   char  pop() { return s[top--]; }
   char  top_of() const { return s[top]; }
   bool  empty() const { return (top == EMPTY); }
   bool  full() const { return (top == max_len-1); }
   void  print() const;
private:
   enum  { EMPTY = -1 };
   char* s;                 	//changed from s[max_len]
   int   max_len;
   int   top;
};


void ch_stack::print() const 
{  
   if (top == EMPTY)
     cout << "Stack is empty" << endl;
   else {
      cout << "Stack is size " << (top + 1) << endl;
      for (int i = 0; i < top + 1; ++i)
         cout << s[i];
      cout << endl; 
   }
}

//copy a char* string into the ch_stack
ch_stack::ch_stack(int size, const char str[]) : max_len(size)
{
   int i;
   assert(size > 0);
   s = new char[size];
   assert(s != 0);
   for (i = 0; i < max_len && str[i] != 0; ++i)
      s[i] = str[i];
   top = --i;
}



