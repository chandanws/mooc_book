#include <iostream>
#include <cassert>
using namespace std;


// Reference counted my_strings

class str_obj {
public:
   friend class my_string;	// my_string access members
   str_obj() : len(0), ref_cnt(1)
      { s = new char[1]; assert(s != 0); s[0] = 0; }
   str_obj(const char* p) : ref_cnt(1)
      { len = strlen(p); s = new char[len + 1];
        assert(s != 0); strcpy(s, p); }
   ~str_obj() { delete []s; }
private:
   int    len, ref_cnt;
   char*  s;
};

class my_string {
public:
   my_string() { st = new str_obj; assert(st != 0); }
   my_string(const char* p)
      { st = new str_obj(p); assert(st != 0); }
   my_string(const my_string& str)
       { st = str.st; st -> ref_cnt++; }
   ~my_string();
   void  assign(const my_string& str);
   void  print() const { cout << st -> s; }
   my_string& operator=(const my_string& str);
   char& operator[](int position);
   int strcmp(const my_string& s1);
   void strrev();
   void print(int n) const;
private:
   str_obj*  st;
};


// print overloaded to print the first n characters 
void my_string::print(int n) const
{
	char *s = st->s;
	for (int i=0; i< n; i++)
	{
		cout << s[i];
	}
	cout << endl;
}


// strrev reverses the my_string void
void my_string::strrev()
{
	char *s = st->s;
	char p[st->len];
	p[st->len] = '\0';
	for (int i=0; i<(st->len); i++)
	{
		p[(st->len)-i-1] = s[i];
	}
    st = new str_obj(p);
    assert(st!=0);	
}

my_string::~my_string()
{
   if (--st -> ref_cnt == 0)
      delete st;
}

void my_string::assign(const my_string& str)
{
   if (str.st != st) {
      if (--st -> ref_cnt == 0)
         delete st;
      st = str.st;
      st -> ref_cnt++;
   }
}

my_string& my_string::operator=(const my_string& str)
{
   if (str.st != st) {
      if (--st -> ref_cnt == 0)
         delete st;
      st = str.st;
      st -> ref_cnt++;
   }
   return *this;
}

// strcmp is negative if s < s1,
// is 0 if s == s1, 
// and is positive if s > s1 
// where s is the implicit argument
int my_string::strcmp(const my_string& s1)
{
	char *s = st->s;
	char *sc = s1.st->s;
	
	int i;
	for (i=0; s[i] && sc[i] && s[i]==sc[i];i++)
		continue;
	return s[i] - sc[i];
}


char& my_string::operator[](int position)
{
   char* s = st -> s;
   for (int i = 0; i != position; ++i) {
      if (*s == 0)
         break;
      s++;
   }
   return *s;
}


int main()
{
   //code fragment using overloaded assignment
   my_string  a("1234567890");
   my_string s1("hello");
   my_string b("zds");
   cout  << a.strcmp(s1) << endl;
   cout  << b.strcmp(s1)  << endl;
   a.strrev();
   a.print();
   s1.strrev();
   s1.print();
   cout << '\n'; 
   s1.print(3);
}
