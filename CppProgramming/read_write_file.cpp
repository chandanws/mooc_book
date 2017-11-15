#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ofstream fout("test.out", ios::app);
	long location = fout.tellp(); //取得写指针的位置
	location = 10L;

	fout.seekp(location); //将写指针移动到第10个字节处
	fout.seekp(location, ios::beg); //从头数location;
	fout.seekp(location, ios::cur);//从当前位置数location
	fout.seekp(location, ios::end); //从尾部数location

}
