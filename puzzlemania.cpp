#include <bits/stdc++.h>
#define MAPHEIGHT 7
#define MAPLENGTH 11
/* MAPP:
7 11
###########
#T##......#
#.#.#..####
#....B...S#
#.######..#
#.........#
###########
*/
using namespace std;


char mapp[MAPHEIGHT][MAPLENGTH];
//void getIn();
//void showMap();

int main(){
	cout << "welcome back CXz." << endl;
	getIn();
	showMap();
	return 0;
}
/////////////////////////////////////
//	functionZone
/////////////////////////////////////
void getIn(){
	for(int i = 0; i < MAPHEIGHT ; i++){
		scanf(" %[^\n]s",mapp[i]);
	}
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



