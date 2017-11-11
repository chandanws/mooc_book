#include <iostream>
#include <typeinfo>
#include <vector>
using namespace std;

int main() {
   char c;
   vector<char>::value_type v;
   if (typeid(c) == typeid(v))
      cout << "vector<char>::value_type is just char"
           << endl;
   else
      cout << "vector<char>::value_type differs "
           << "from char" << endl;
}
