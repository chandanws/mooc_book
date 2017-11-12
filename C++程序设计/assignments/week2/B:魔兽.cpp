#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;


//武士
class knight
{
public:
    knight(int b, int i, int d=0):blood(b), id(i), damage(d){}
private:
    int blood; //生命值
    int id; //编号
    int damage;//攻击力
};

//司令部
class Command
{
public:
    //constructor
    Command(int _n, int _dragon, int _ninja, int _iceman, int _lion, int _wolf, string _flag):
    n(_n), dragon(_dragon), ninja(_ninja), iceman(_iceman), lion(_lion), wolf(_wolf), flag(_flag), name(5), blood(5), num(5,0), id(1), producing_id(0){choose();}
    bool produce();
    void choose();
    void stop_produce(); //停止生产
    ~Command();
private:
    int lion, dragon, ninja, iceman, wolf;     //iceman、lion、wolf、ninja、dragon 的初始生命值
    knight * kni[100];     // 拥有的武士
    int n;     //生命元
    int time;    //时间
    string flag;    //红方或者蓝方
    // 制造顺序
    vector<string> name; //每一种武士名字
    vector<int> blood; //每一种武士初始生命元
    vector<int> num; //每一种武士数量
    int id; //制造的武士数量:从1开始编号
    int producing_id; //正在制造的武士编号:0-4;
};

Command::~Command()
{
    for (int i=0;i<id;i++)
        delete kni[i];
}



void Command::choose()
{
    if (flag == string("red"))
    {
        vector<string> red_order_name{"iceman", "lion", "wolf", "ninja", "dragon"};
        name = red_order_name;
        vector<int> red_order_blood{iceman, lion, wolf, ninja, dragon};
        blood = red_order_blood;
    }
    else if (flag == string("blue"))
    {
        vector<string> blue_order_name{"lion", "dragon", "ninja", "iceman", "wolf"};
        name = blue_order_name;
        vector<int> blue_order_blood{lion, dragon, ninja, iceman, wolf};
        blood = blue_order_blood;
    }
}


void Command::stop_produce()
{
    cout << setw(3) << setfill('0') << time << " "; //输出时间： e.g. 004
    cout << flag << " headquarter stops making warriors" << endl;
}

bool Command::produce()
{
    //找到适合生产的武士
    int j = 0;
    while (blood[producing_id] > n)
    {
        j++;
        producing_id = (producing_id+1)%5; //循环制造武士
        if (j==5) //所有的都不能生产
        {
            stop_produce();
            return false;
        }
    }

    //生产武士
    int i = producing_id;
    kni[id] = new knight(blood[i], id);
    
    //输出生产信息
    string space = " ";
    cout << setw(3) << setfill('0') << time << space; //输出时间： e.g. 004
    cout << flag << space << name[i] << space << id; //输出武士: blue lion 5
    cout << " born with strength " << blood[i] << "," ; //输出生命值：e.g. born with strength 5,
    cout << num[i]+1 << space << name[i] << " in " << flag << " headquarter" << endl;
    
    //更新信息
    n -= blood[i]; //生命元减小
    time += 1; //时间增加
    num[i] = num[i]+1; //该种武士数量增加
    id += 1; //编号增加
    producing_id = (producing_id+1)%5; //循环制造武士
    
    return true;
}



int main()
{
    int num; //代表测试数据组数
    int n; // //生命元
    int b_dragon, b_ninja, b_iceman,b_lion, b_wolf; //依次是 dragon 、ninja、iceman、lion、wolf 的初始生命值
    
    cin >> num;
    cin >> n >> b_dragon >> b_ninja >> b_iceman >> b_lion >> b_wolf; //输入
    Command blue(n, b_dragon, b_ninja, b_iceman,b_lion, b_wolf, string("blue"));
    Command red(n, b_dragon, b_ninja, b_iceman,b_lion, b_wolf, string("red"));
    bool p1=true, p2=true;
    while( p1 || p2)
    {
        if (p2)
            p2 = red.produce();
        if (p1)
            p1 = blue.produce();
    }

    return 0;
}
