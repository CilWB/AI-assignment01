#include <bits/stdc++.h>
#define MAPHEIGHT 7
#define MAPLENGTH 11
/* MAPP:
7 11
###########
#.##......#
#T#.#..####
#....B...S#
#.######..#
#.........#
###########
*/
using namespace std;
 
typedef struct po{
	int x,y;
}position;
position goal,now,temp;

char mapp[MAPHEIGHT][MAPLENGTH];
void getIn();
void showMap();
void getPosition();
void DFS();
int main(){
//	cout << "welcome back CXz." << endl;
	getIn();
	showMap();
	getPosition();
	return 0;
}
/////////////////////////////////////
//	functionZone
/////////////////////////////////////

void getIn(){
	for(int i = 0; i < MAPHEIGHT ; i++){
		scanf(" %[^\n]s",mapp[i]);
	}
//	mapp = "############T##......##.#.#..#####....B...S##.######..##.........############";	
}
void showMap(){
	cout << "--------------------------\n";
	for(int i = 0 ; i < MAPHEIGHT;i++){
		for(int j = 0 ; j < MAPLENGTH ; j++){
			cout << mapp[i][j];
		}
		cout << endl;
	}
	cout << "--------------------------\n";
}
void getPosition(){
	cout << "-------------USE getPosition\n";
	for(int i = 0 ; i < MAPHEIGHT;i++){
		for(int j = 0 ; j < MAPLENGTH ; j++){
			if(mapp[i][j]=='T') goal.x = i , goal.y = j;
			else if(mapp[i][j]=='S') now.x = i, now.y = j;
		}
	}
	cout << "goal :\n\tx: " << goal.x << endl;
	cout << "\ty: " << goal.y << endl;
	cout << "now start:\n\tx: "<< now.x << endl;
	cout << "\ty: " << now.y << endl;
	cout << "-------------END getPosition\n";
	
}
void DFS(){
	
}


