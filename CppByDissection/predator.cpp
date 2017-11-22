#include <iostream>
using namespace std;

// Predator-Prey simulation using class living

enum state { EMPTY, GRASS, RABBIT, FOX, STATES };

const int DRAB = 3, DFOX = 6, TMFOX = 5, CYCLES = 5, N = 40;

// DRAB rabbits die at 3, DFOX foxes at 6, 
// TMFOX too many foxes, CYCLES of simulation, 
// N size of square world

class living;                 	// forward declaration

typedef living* world[N][N]; 
 
class living {                	// what lives in world
public:
   virtual state  who() = 0;  	// state identification
   virtual living*  next(world w) = 0;  
protected:
   int  row, column;          	// location
   void sums(world w, int sm[]); 
};

void living::sums(world w, int sm[])
{
   int  i, j;

   sm[EMPTY] = sm[GRASS] = 0; 
   sm[RABBIT] = sm[FOX] = 0;
   for (i = -1; i <= 1; ++i)
      for (j = -1; j <= 1; ++j)
         sm[w[row + i][column + j] -> who()]++;
}

// Currently only predator class

class fox : public living {
public:
   fox(int r, int c, int a = 0) : age(a)
      { row = r; column = c; }
   state  who() { return FOX; }	// deferred fox method
   living*  next(world w);
protected:
   int  age;               	// used to decide on dying
};

// Currently only prey class

class rabbit : public living {
public:
   rabbit(int r, int c, int a = 0) : age(a)
      { row = r; column = c; }
   state  who() { return RABBIT; }
   living*  next(world w);
protected:
   int  age;
};

// Currently only plant life

class grass : public living {
public:
   grass(int r, int c) { row = r; column = c; }
   state who() { return GRASS; }
   living* next(world w);
};

// Nothing lives here

class empty : public living {
public:
   empty(int r, int c) { row = r; column = c; }
   state  who() { return EMPTY; }
   living*  next(world w);
};

living* grass::next(world w)
{
   int  sum[STATES];

   sums(w, sum);
   if (sum[GRASS] > sum[RABBIT])         	// eat grass
      return (new grass(row, column));
   else
      return (new empty(row, column));
}

living* rabbit::next(world w)
{
   int  sum[STATES];

   sums(w, sum);
   if (sum[FOX] >= sum[RABBIT])  	// eat rabbits
      return (new empty(row, column));
   else if (age > DRAB)          	// rabbit is too old
      return (new empty(row, column));
   else
      return (new rabbit(row, column, age + 1));
}

living* fox::next(world w)
{
   int  sum[STATES];

   sums(w, sum);
   if (sum[FOX] > TMFOX)         	// too many foxes
      return (new empty(row, column));
   else if (age > DFOX)          	// fox is too old
      return (new empty(row, column));
   else
      return (new fox(row, column, age + 1));
}

living* empty::next(world w)     	// fill empty square
{
   int  sum[STATES];

   sums(w, sum);
   if (sum[FOX] > 1)
      return (new fox(row, column));
   else if (sum[RABBIT] > 1)
      return (new rabbit(row, column));
   else if (sum[GRASS] > 0)
      return (new grass(row, column));
   else
      return (new empty(row, column));
}

// World is all empty

void init(world w)
{
   int  i, j;

   for (i = 0; i < N; ++i)
      for (j = 0; j < N; ++j)
         w[i][j] = new empty(i,j);
}

// New world w_new is computed from old world w_old

void update(world w_new, world w_old)
{
   int  i, j;

   for (i = 1; i < N - 1; ++i)   	// borders are taboo
      for (j = 1; j < N - 1; ++j)
         w_new[i][j] = w_old[i][j] -> next(w_old);
}

// Clean world up

void dele(world w)
{
   int  i, j;

   for (i = 1; i < N - 1; ++i)    	//borders are taboo
      for (j = 1; j < N - 1; ++j)
         delete(w[i][j]);
}

void eden(world w)
{
   int  i, j;

   for (i = 2; i < N - 2; ++i)
      for (j = 2; j < N - 2; ++j) {
         delete(w[i][j]);
         if ( (i + j) % 3 == 0)
            w[i][j] = new rabbit(i, j);
         else
            if ( (i + j) % 3 == 1)
               w[i][j] = new fox(i, j);
            else
               w[i][j] = new grass(i, j);
      }
}


void pr_state(world w)
{
   int  i, j;

   for (i = 0; i < N; ++i) {
      cout << endl;
      for (j = 0; j < N; ++j)
         cout << static_cast<int>(w[i][j] -> who());
   }
   cout << endl << endl;
}

int main()
{
   world  odd, even;
   int    i;

   init(odd);  init(even);
   eden(even);          	// generate initial world
   pr_state(even);      	// print Garden of Eden state
   for (i = 0; i < CYCLES; ++i) {       	// simulation
      if (i % 2) {
         update(even, odd);
         pr_state(even);
         dele(odd);
      }
      else {
         update(odd, even);
         pr_state(odd);
         dele(even);
      }
   }
}