#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

//声明
class weapon;
int R;


//武士
class knight
{
public:
    knight(int _blood, int _id):blood(_blood), id(_id), w1(nullptr), w2(nullptr), damage(0), status(1){}
    virtual void print()=0;
    virtual ~knight(){delete w1; delete w2; }//删除武器
    friend void choose_weapon(knight *k, int weapon_id, weapon* &w);
    const int get_blood () const { return blood;}
    const int set_blood(int b){ if (b>0) blood=b; else {blood=0; status=0} return b;}
    const int get_damage() const {return damage;}
    const int set_damage(int d){damage=d; return d;}
protected:
    int blood; //生命值
    int id; //编号
    int damage; //攻击力
    weapon *w1, *w2; //武器，至多有2个。
    int status; //status=0 (dead), status=1(live)
};


//城市
class city
{
    city(int i): id(i){};
    int id; //city id
    string flag; //旗帜
};

//武器
class weapon
{
public:
    weapon(knight* _k, int i, int d, string n): belong(_k), id(i), damage(d), name(n){};
    string name; //武器名
    virtual void attack(knight *k)=0; //进行攻击
    void set_damage(int d){damage = d;}
    const int get_damage() const{return damage;};
    virtual ~weapon(){};
protected:
    int id; //编号
    int damage; //攻击力
    knight *belong; //属于哪一个武士
};


// sword武器的初始攻击力为拥有它的武士的攻击力的20%（去尾取整）。
// 但是sword每经过一次战斗(不论是主动攻击还是反击)，就会变钝，攻击力变为本次战斗前的80% (去尾取整)。
// sword攻击力变为0时，视为武士失去了sword。如果武士降生时得到了一个初始攻击力为0的sword，则视为武士没有sword.
// 被攻击者生命值会减去进攻者的攻击力值和进攻者手中sword的攻击力值。
class sword:public weapon
{
public:
    sword(knight* k): weapon(k, id, (int)(k->get_damage()*0.2), "sword"){}
    void attack(knight *k){k->set_blood(k->get_blood()-damage);}
    ~sword(){};
private:
    static constexpr int id = 0;
};

// 拥有bomb的武士，在战斗开始前如果判断自己将被杀死
//（不论主动攻击敌人????，或者被敌人主动攻击都可能导致自己被杀死，而且假设武士可以知道敌人的攻击力和生命值），那么就会使用bomb和敌人同归于尽。
// 武士不预测对方是否会使用bomb。
// 武士使用bomb和敌人同归于尽的情况下，不算是一场战斗，双方都不能拿走城市的生命元，也不影响城市的旗帜。
class bomb:public weapon
{
public:
    bomb(knight *k): weapon(k, id, 0, "bomb"){}
    void attack(knight *k){if (predict(k)) k->set_blood(0);}
    bool predict(knight* k){return false;}
    ~bomb(){};
private:
    static constexpr int id = 1;
};

// arrow有一个攻击力值R。
// 如果下一步要走到的城市有敌人，那么拥有arrow的武士就会放箭攻击下一个城市的敌人（不能攻击对方司令部里的敌人）而不被还击。
// arrow使敌人的生命值减少R，若减至小于等于0，则敌人被杀死。arrow使用3次后即被耗尽，武士失去arrow。两个相邻的武士可能同时放箭把对方射死。
class arrow:public weapon
{
public:
    arrow(knight *k, int R): weapon(k, id, R, "arrow"){}
    void attack(knight *k){while (((usage--)>3)&&(k->set_blood(k->get_blood()-damage)));}
private:
    static constexpr int id = 2;
    int usage = 3;//使用次数
};


//choose weapon corresponding to weapon_id.
void choose_weapon(knight *k, int weapon_id, weapon* &w)
{
    switch (weapon_id) {
        case 0:
            w = new sword(k);
            break;
        case 1:
            w = new bomb(k);
            break;
        case 2:
            w = new arrow(k, R);
            break;
        default:
            cerr << "Weapon error" << endl;
            break;
    }
    
};


// dragon可以拥有一件武器。编号为n的dragon降生时即获得编号为 id%3 的武器。
// dragon有“士气”这个属性，是个浮点数，其值为它降生后其司令部剩余生命元的数量除以造dragon所需的生命元数量。
// dragon 在一次在它主动进攻的战斗结束后，如果还没有战死，而且士气值大于0.8，就会欢呼。
// dragon每取得一次战斗的胜利(敌人被杀死)，士气就会增加0.2，每经历一次未能获胜的战斗，士气值就会减少0.2。
// 士气增减发生在欢呼之前。
class dragon: public knight
{
public:
    dragon(int _blood, int _id, int _left_blood): knight(_blood, _id)
    {choose_weapon(this, _id%3, w1); morale= ((double) _left_blood)/_blood;}
    void print(){cout << "It has a " << w1->name << ",and it's morale is ";
        cout << setiosflags(ios::fixed) << setprecision(2) << morale << endl;};
    void war()
    {
        //dragon 在一次在它主动进攻的战斗结束后，如果还没有战死，而且士气值大于0.8，就会欢呼
        if ((blood > 0)&&( morale>0.8))
            cout << "Dragon claim" << endl;
        
    }
private:
    double morale;
};

// ninjia可以拥有两件武器。
// 编号为n的ninjia降生时即获得编号为 n%3 和 (n+1)%3的武器。
// ninja 挨打了也从不反击敌人。
class ninja: public knight
{
public:
    ninja(int _blood, int _id): knight(_blood, _id)
        {choose_weapon(this, _id%3, w1); choose_weapon(this,(_id+1)%3, w2);};
    void print(){cout << "It has a " << w1->name << " and a " << w2->name << endl;}
};

// iceman有一件武器。编号为n的iceman降生时即获得编号为 n%3 的武器。
// iceman 每前进两步，在第2步完成的时候，生命值会减少9，攻击力会增加20。
// 但是若生命值减9后会小于等于0，则生命值不减9,而是变为1。即iceman不会因走多了而死。
class iceman: public knight
{
public:
    iceman(int _blood, int _id): knight(_blood, _id){ choose_weapon(this, _id%3, w1);};
    void print(){ cout << "It has a " << w1->name << endl;}
};


// lion 有“忠诚度”这个属性，其初始值等于它降生之后其司令部剩余生命元的数目。
// 每经过一场未能杀死敌人的战斗，忠诚度就降低K。
// 忠诚度降至0或0以下，则该lion逃离战场,永远消失。
// 但是已经到达敌人司令部的lion不会逃跑。
// lion在己方司令部可能逃跑。lion 若是战死，则其战斗前的生命值就会转移到对手身上。
// 所谓“战斗前”，就是每个小时的40分前的一瞬间。
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
    int n_blood; //生命元数量
    int n_city; //两个司令部之间一共有N个城市( 1 <= N <= 20 )
    int arrow_damage; // arrow的攻击力
    int loyal_minus_lion; //lion每经过一场未能杀死敌人的战斗，忠诚度就降低K。
    int time_max; //要求输出从0时0分开始，到时间T为止(包括T) 的所有事件。T以分钟为单位，0 <= T <= 5000
    int b_dragon, b_ninja, b_iceman,b_lion, b_wolf; //依次是 dragon 、ninja、iceman、lion、wolf 的初始生命值
    
    //input
    cin >> n_blood >> n_city >> arrow_damage >> loyal_minus_lion >> time_max; //输入
    cin >> b_dragon >> b_ninja >> b_iceman >> b_lion >> b_wolf; //输入
    R = arrow_damage;
    
    //input check
    if ((n_city<1)||(n_city>20))
        cerr << "Input num of City(1~20) Error: " << n_city << endl;
    if ((time_max<0)||(time_max>5000))
        cerr << "Time(0~5000) error: "<< time_max << endl;
    
    //set-up
    Command blue(n_blood, b_dragon, b_ninja, b_iceman,b_lion, b_wolf, string("blue"));
    Command red(n_blood, b_dragon, b_ninja, b_iceman,b_lion, b_wolf, string("red"));
    
    
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
