// 一个学生成绩录入和查询系统，
// 接受以下两种输入:
// Add name id score
// Query score
// name是个字符串，中间没有空格，代表学生姓名。id是个整数，代表学号 。score是个整数，表示分数。学号不会重复，分数和姓名都可能重复。

// 第一种输入表示要添加一个学生的信息，碰到这种输 入，就记下学生的姓名、id和分数。
// 第二种输入表示要查询，碰到这种输入 ，就输出已有记录中分数比score低的最高分获得者的姓名、学号和分数。
// 如 果有多个学生都满足条件，就输出学号最大的那个学生的信息。如果找不到 满足条件的学生，则输出“Nobody”

#include <iostream>
#include <map> //使用multimap需要包含此头文件
#include <string>

using namespace std;

class CStudent
{
public:
    struct CInfo //类的内部还可以定义类
    {
        int id;
        string name;
    };
    int score;
    CInfo info; //学生的其他信息
};


typedef multimap<int, CStudent::CInfo> MAP_STD;


int main()
{
    MAP_STD mp;
    CStudent st;
    string cmd;
    while( cin >> cmd ) {
        if( cmd == "Add") {
            cin >> st.info.name >> st.info.id >> st.score ;
            mp.insert(MAP_STD::value_type(st.score, st.info));
        }
        else if( cmd == "Query" ){
            int score;
            cin >> score;
            MAP_STD::iterator p = mp.lower_bound(score);
            if( p!= mp.begin()) {
                --p;
                score = p->first; //比要查询分数低的最高分
                MAP_STD::iterator maxp = p;
                int maxId = p->second.id;
                for( ; p!= mp.begin() && p->first == score; --p)
                {
                    //遍历所有成绩和score相等的学生
                    if( p->second.id > maxId ) {
                        maxp = p;
                        maxId = p->second.id ;
                    }
                }
                if( p->first == score) {
                    //如果上面循环是因为 p == mp.begin()
                    // 而终止，则p指向的元素还要处理
                    if( p->second.id > maxId ) {
                        maxp = p;
                        maxId = p->second.id ;
                    }
                }
                cout << maxp->second.name << " " << maxp->second.id << " " <<
                maxp->first << endl;
            }
            else
                //lower_bound的结果就是 begin，说明没人分数比查询分数低
                cout << "Nobody" << endl;
        }
    }
    return 0;
}

//mp.insert(MAP_STD::value_type(st.score,st.info ));
//mp.insert(make_pair(st.score,st.info )); 也可以
