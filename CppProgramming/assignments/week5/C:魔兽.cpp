#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;



//武士
class knight
{
public:
    knight(int _blood, int _id):blood(_blood), id(_id){}
    virtual void print()=0;
    virtual ~knight(){}
private:
    int blood; //生命值
    int id; //编号
};

//武器
class weapon
{
public:
    weapon(int i): id(i), name(weapon_name[i]), weapon_name({"sword", "bomb", "arrow"}){};
    const string get_name(){return name;}
private:
    int id; //编号
    vector<string> weapon_name;
    string name;
};


// dragon可以拥有一件武器。编号为n的dragon降生时即获得编号为 n%3 的武器。
// dragon还有“士气”这个属性，是个浮点数，
// 其值为它降生后其司令部剩余生命元的数量除以造dragon所需的生命元数量。
class dragon: public knight
{
public:
    dragon(int _blood, int _id, int _left_blood): knight(_blood, _id), w(_id%3)
    {morale=static_cast<double>(_left_blood)/_blood;}
    void print(){cout << "It has a " << w.get_name() << ",and it's morale is ";
        cout << setiosflags(ios::fixed) << setprecision(2) << morale << endl;};
private:
    weapon w;
    double morale;
};

// ninja可以拥有两件武器。编号为n的ninja降生时即获得编号为 n%3 和 (n+1)%3的武器。
class ninja: public knight
{
public:
    ninja(int _blood, int _id):
        knight(_blood, _id), w1(_id%3), w2((_id+1)%3)
            {};
    void print(){cout << "It has a "<< w1.get_name() << " and a " << w2.get_name() << endl;}
private:
    weapon w1, w2;
};

//iceman有一件武器。编号为n的iceman降生时即获得编号为 n%3 的武器。
class iceman: public knight
{
public:
    iceman(int _blood, int _id):
    knight(_blood, _id), w(_id%3){};
    void print(){ cout << "It as a " << w.get_name() << endl;}
private:
    weapon w;
};


//lion 有“忠诚度”这个属性，其值等于它降生后其司令部剩余生命元的数目。
class lion: public knight
{
public:
    lion(int _blood, int _id, int _left_blood):knight(_blood, _id), loyalty(_left_blood){};
    void print(){cout << "It's loyalty is " << loyalty << endl;}
private:
    int loyalty;
};

//wolf没特点
class wolf:public knight
{
public:
    wolf(int _blood, int _id):knight(_blood, _id){};
    void print(){};
};


//司令部
class Command
{
public:
    //constructor
    Command(int _n, int _dragon, int _ninja, int _iceman, int _lion, int _wolf, string _flag):
    n(_n), bdragon(_dragon), bninja(_ninja), biceman(_iceman), blion(_lion), bwolf(_wolf), flag(_flag), name(5), blood(5), num(5,0), id(1), producing_id(0){choose();}
    bool produce();
    void choose();
    void stop_produce(); //停止生产
    ~Command();
private:
    int blion, bdragon, bninja, biceman, bwolf;     //iceman、lion、wolf、ninja、dragon 的初始生命值
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
        vector<int> red_order_blood{biceman, blion, bwolf, bninja, bdragon};
        blood = red_order_blood;
    }
    else if (flag == string("blue"))
    {
        vector<string> blue_order_name{"lion", "dragon", "ninja", "iceman", "wolf"};
        name = blue_order_name;
        vector<int> blue_order_blood{blion, bdragon, bninja, biceman, bwolf};
        blood = blue_order_blood;
    }
    else
        cerr << "Only blue and red used here: " << flag << " can't be used." << endl;
}


void Command::stop_produce()
{
    cout << setw(3) << setfill('0') << time << " "; //输出时间： e.g. 004
    cout << flag << " headquarter stops making warriors" << endl;
}

bool Command::produce()
{
    //找到适合生产的武士producing_id
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
    int i = producing_id;//为了简化而已
    if (name[i] == string("lion"))
        kni[i] = new  lion(blood[i], id, n-blood[i]);
    else if (name[i] == string("dragon"))
        kni[i] = new  dragon(blood[i], id, n-blood[i]);
    else if (name[i] == string("ninja"))
        kni[i] = new  ninja(blood[i], id);
    else if (name[i] == string("iceman"))
        kni[i] = new  iceman(blood[i], id);
    else  if (name[i] == string("wolf"))
        kni[i] = new  wolf(blood[i], id);
    else
        cerr << "Systematic error" << endl;
    
    //输出生产信息
    string space = " ";
    cout << setw(3) << setfill('0') << time << space; //输出时间： e.g. 004
    cout << flag << space << name[i] << space << id; //输出武士: blue lion 5
    cout << " born with strength " << blood[i] << "," ; //输出生命值：e.g. born with strength 5,
    cout << num[i]+1 << space << name[i] << " in " << flag << " headquarter" << endl;
    kni[i] -> print();

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
