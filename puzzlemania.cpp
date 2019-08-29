#include <bits/stdc++.h>
#define MAPHEIGHT 7
#define MAPLENGTH 11

using namespace std;
 
typedef struct po{
	int x,y,step;
	char act[100];
}position;
position goal,now,start;
queue<position>que;
int direction[4][2] = {{0,-1},{1,0},{0,1},{-1,0}};

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
	BFS(start,goal);
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
			
			cout << "--------------------------\n";
			for(int x = 0 ; x < MAPHEIGHT;x++){
				for(int j = 0 ; j < MAPLENGTH ; j++){
					cout << char(went[x][j]+'0');
				}
				cout << endl;
			}
			cout << "--------------------------\n";	
			
			for(int i = 0 ; i < 4 ; i++){
				if(went[now.x+direction[i][0]][now.y+direction[i][1]]==0)
				if(mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='.'
				||mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='T'){
//					cout << "Add " << now.x+direction[i][0] << " " << now.y+direction[i][1] << endl;
					
					if(mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='T'){
						for(int i = 0 ; i <= now.step ; i++)
							cout << now.act[i];
						cout << "\nFOUND GOALLLL!!!!\n";
						return 1;
					}
					else{
						position temp;
						temp.x = now.x+direction[i][0];
						temp.y = now.y+direction[i][1];
						temp.act[temp.step++] = '0'+i;
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
#.##......#
#T#.#..####
#....B...S#
#.######..#
#.........#
###########
*/
