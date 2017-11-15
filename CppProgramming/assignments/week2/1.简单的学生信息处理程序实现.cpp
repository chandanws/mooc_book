#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

class student{
public:
    student(string _name, int _age, string _id, int a1, int a2, int a3, int a4):
        name(_name), age(_age), id(_id), gpa1(a1), gpa2(a2), gpa3(a3), gpa4(a4)
        {average = (gpa1+gpa2+gpa3+gpa4)/4;}
    void print();
private:
    string name; //姓名
    int age;   //年龄
    string id;   //学号
    int gpa1; //第1学年平均成绩
    int gpa2; //第2学年平均成绩
    int gpa3; //第3学年平均成绩
    int gpa4; //第4学年平均成绩
    int average; // average gpa
};

void student::print()
{
    cout << name << "," << age << "," << id << "," << average << endl;
}

int main()
{
    vector<student> s;
    
    string line;
    while (getline(cin, line))//ctrl-D结束
    {
        string name; //姓名
        int age;   //年龄
        string id;   //学号
        int gpa1; //第1学年平均成绩
        int gpa2; //第2学年平均成绩
        int gpa3; //第3学年平均成绩
        int gpa4; //第4学年平均成绩
        int average; // average gpa
        
        
        //preprocessin input
        string item, token;
        
        string delim=",";
        size_t pos = 0;
        while( (pos = line.find(delim))!=string::npos)
        {
            token = line.substr(0,pos);
            item += " ";
            item += token;
            line.erase(0, pos+delim.length());
        }
        
        istringstream record(item);
        record >> name >> age >> id >> gpa1 >> gpa2 >> gpa3 >> gpa4;
        student a(name, age, id, gpa1, gpa2, gpa3, gpa4);
        s.push_back(a);
        a.print();
    
    };
}
