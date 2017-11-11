
#include <iostream>
#include <cassert>
using namespace std;

struct slistelem {
   char        data;
   slistelem*  next;
};

class slist {               	// singly linked list
public:
   slist() : h(0) { }       	// 0 denotes empty slist
   slist(const char*c);       // slist constructor with initializer char* string
   int length() const; // length returns the length of the slist
   int count_c(char c) const; // return number of elements whose data value is c
   ~slist() ; 
   void  prepend(char c);   	// adds to front of slist
   void  del();
   slistelem*  first() const { return h; }
   void  print() const;
   void  release();
private:
   slistelem*  h;           	// head of slist
};



inline slist::slist(const char *c) // slist constructor with initializer char* string
{
	int i = 0;
	while(c[i]!='\0')
	{
		i++;
	}
	while(--i>=0)
	{
		prepend(c[i]);
	}
}

int slist::length() const
{
	int len = 0;
	slistelem * temp = h; 
	while(temp!=0)
	{
		len += 1;
		temp = temp-> next;
	}
	return len;
}


int slist::count_c(char c) const
{
	int count = 0;
	slistelem *temp = h;
	while(temp!=0)
	{
		if (temp->data == c)
			count += 1;
		temp = temp-> next;
	}
	return count;
}



void slist::prepend(char c)
{
   slistelem*  temp = new slistelem;	// create element
   assert(temp != 0);
   temp -> next = h;                	// link to slist
   temp -> data = c;
   h = temp;                  	// update head of slist
}

void slist::del()
{
   slistelem*  temp = h;
   h = h -> next;         	// presumes nonempty slist
   delete temp;
}



void slist::print() const      	// object is unchanged
{
   slistelem*  temp = h;

   while (temp != 0) {         	// detect end of slist
      cout << temp -> data << " -> ";
      temp = temp -> next;
   }
   cout << "\n###" << endl;
}
// Elements returned to the heap

void slist::release()  
{
   while (h != 0)
      del();
}

slist::~slist()
{
   cout << "destructor invoked" << endl;
   release();
}

int main()
{
   slist*  p;
   {
      slist  w;
      const char *c = "sdsadfasfa";
      char c1 = 's';
      slist x(c);
      x.print();
      cout << "The lengh of singly list x is " << x.length(); 
      cout << "   the signly list x has character s " << x.count_c(c1) << " times " << '\n';
      cout << "   the signly list x has character d " << x.count_c('d') << " times " << endl;

   }
}
