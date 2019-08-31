#include <bits/stdc++.h>
#define MAPHEIGHT 20
#define MAPLENGTH 20

using namespace std;
 
typedef struct po{
	int x,y,step;
	char act[100];
}position;
position goal,now,start;
queue<position>que;
int r,c;
int direction[4][2] = {{0,-1},{1,0},{0,1},{-1,0}};
// 0-> w
// 1-> s
// 2-> e
// 3-> n
char ccc[5] = "wsen";

char mapp[MAPHEIGHT][MAPLENGTH];
void getIn();
void showMap();
void getPosition();
int BFS(position,position);
int main(){
//	cout << "welcome back CXz." << endl;
	getIn();
	showMap();
	getPosition();
	cout << "BFS " << BFS(start,goal);
	return 0;
}
/////////////////////////////////////
//	functionZone
/////////////////////////////////////

void getIn(){
	
	cin >> r >> c ;
	for(int i = 0 ; i < r ; i++){
		for(int j = 0 ; j < c ;j++){
			scanf(" %c",&mapp[i][j]);
		}
	}
	
//	for(int i = 0; i < MAPHEIGHT ; i++){
//		for(int j = 0 ; j < )
//		scanf(" %[^\n]s",mapp[i]);
//	}
//	mapp = "############T##......##.#.#..#####....B...S##.######..##.........############";	
}
void showMap(){
	cout << "------------show map--------------\n";
	for(int i = 0 ; i < r;i++){
		for(int j = 0 ; j < c ; j++){
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
			else if(mapp[i][j]=='S') start.x = i, start.y = j;
		}
	}
	start.step = 0;
	cout << "goal :\n\tx: " << goal.x << endl;
	cout << "\ty: " << goal.y << endl;
	cout << "now start:\n\tx: "<< start.x << endl;
	cout << "\ty: " << start.y << endl;
	cout << "-------------END getPosition\n";
	
}
int BFS(position nnow,position goal){
//	cout << "welcome to BFS\n";
	que.push(nnow); // add a start state
	if(start.x == goal.x && start.y == goal.y){
		return 0;
	}
	char went[MAPHEIGHT][MAPLENGTH]; 
	for(int i = 0 ; i< MAPHEIGHT;i++)
		for(int j = 0 ; j <MAPLENGTH;j++)
			went[i][j] = 0;
	while(1){
		if(que.empty()){
			return -1;	
		} 
		else{
			position now = que.front();
			que.pop();
			went[now.x][now.y] = 1;
			
			for(int i = 0 ; i < 4 ; i++){
				if(went[now.x+direction[i][0]][now.y+direction[i][1]]==0)
				if(mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='.'
				||mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='T'){
//					cout << "Add " << now.x+direction[i][0] << " " << now.y+direction[i][1] << endl;
				
//					cout << "--------------------------\n";
//					for(int x = 0 ; x < MAPHEIGHT;x++){
//						for(int j = 0 ; j < MAPLENGTH ; j++){
//							cout << char(went[x][j]+'0');
//						}
//						cout << endl;
//					}
//					cout << "--------------------------\n";	
				
					if(mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='T'){
						for(int i = 0 ; i <= now.step ; i++)
							cout << now.act[i];
						cout << "\nFOUND GOALLLL!!!!\n";
						return 1;
					}
					else{
//						cout << i << endl;
						position temp=now;
						temp.x = now.x+direction[i][0];
						temp.y = now.y+direction[i][1];
						temp.act[temp.step++] = ccc[i];
						
						que.push(temp);
					}
					
				}
				
			}
		}
	
	} // end while(1)
	
	
}

/* MAPP:
5 5
#####
#...#
#T.S#
#...#
#####

7 11
###########
#.##.....T#
#.#.#..####
#....B...S#
#.######..#
#.........#
###########
*/
// 0-> w
// 1-> s
// 2-> e
// 3-> n

