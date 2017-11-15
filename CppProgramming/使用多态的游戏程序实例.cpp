
#include <iostream>
using namespace std;


//非多态的实现方法
class class CCreature0 {
protected:
    
    int nPower ; //代表攻击力
    int nLifeValue ; //代表生命值
    
};


// 为每个怪物类编写
// Attack、FightBack和 Hurted成员函数。
// Attact函数表现攻击动作，攻击某个怪物，并调用被攻击怪物的 Hurted函数，
// 以减少被攻击怪物的生命值，同时也调用被攻击怪物 的 FightBack成员函数，遭受被攻击怪物反击。
// Hurted函数减少自身生命值，并表现受伤动作。
// FightBack成员函数表现反击动作，并调用被反击对象的Hurted成 员函数，使被反击对象受伤。

class CDragon0:public CCreature0 {
public:
    void Attack(CWolf * pWolf) {
        // ．．．表现攻击动作的代码
        pWolf->Hurted(nPower);
        pWolf->FightBack(this);
    }
    
    void Attack(CGhost * pGhost) {
        //．．．表现攻击动作的代码
        pGhost->Hurted(nPower);
        pGohst->FightBack(this);
    }
    
    void Hurted (int nPower) {
        //．．．．表现受伤动作的代码
        nLifeValue -= nPower;
    }
    
    void FightBack(CWolf * pWolf) {
        //．．．表现反击动作的代码
        pWolf ->Hurted(nPower/2);
    }
    
    void FightBack(CGhost * pGhost) {
        //．．．．表现反击动作的代码
        pGhost->Hurted(nPower/2 );
    }
    
};

//基类CCrecture:
class CCreature{
protected:
    int m_nLifeValue, m_nPower;
public:
    virtual void Attack(CCrecture *pCreature) {}
    virtual void Hurted(int nPower){}
    virtual void FightBack(CCreture* pCreature){}
}

//派生类CDragon:
class CDragon: public CCrecture{
public:
    virtual void Attack(CCrecture *pCreature);
    virtual void Hurted(int nPower);
    virtual void FightBack(CCreature* pCreature);
}

void CDragon::Attack(CCreature *p)
{
    //…表现攻击动作的代码
    p->Hurted(m_nPower); //多态
    p->FightBack(this); //多态
}

void CDragon::Hurted(int nPower)
{
    //…表现受伤动作的代码
    m_nLifeValue -= nPower;
}

void CDragon::FightBack(CCreature * p)
{
    //…表现反击动作的代码
    p->Hurted(m_nPower/2); //多态
}


int main()
{
    CDragon Dragon;
    CWolf Wolf;
    CGhost Ghost;
    CThunderBird Bird;
    
    Dragon.Attack(&Wolf);
    Dragon.Attack(&Ghost);
    Dragon.Attack(&Bird);
}

















