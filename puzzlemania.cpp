#include <bits/stdc++.h>
#define MAPHEIGHT 20
#define MAPLENGTH 20

using namespace std;
 
typedef struct po{
	int x,y,step;
	char act[100];
	char stage[20][20];
}position;
position goal,now,start;
queue<position>que;
int r,c;
int direction[4][2] = {{0,-1},{1,0},{0,1},{-1,0}};
// 0-> w
// 1-> s
// 2-> e
// 3-> n
char ccc[9] = "wsenWSEN";
char zzz[9] = "enws";
char mapp[MAPHEIGHT][MAPLENGTH];
char went[MAPHEIGHT][MAPLENGTH];
void getIn();
void showMap();
void getPosition();
void showWent();
void showStage(position);
bool inBound();
int BFS(position,position);

int main(){
//	cout << "welcome back CXz." << endl;
	getIn();
	showMap();
	getPosition();
//	showStage(start);
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
	for(int i = 0 ; i < r;i++){
		for(int j = 0 ; j < c ; j++){
			if(mapp[i][j]=='T') goal.x = i , goal.y = j;
			else if(mapp[i][j]=='S') start.x = i, start.y = j;
			start.stage[i][j] = mapp[i][j];
		}
	}
	start.step = 0;
	cout << "goal :\n\tx: " << goal.x << endl;
	cout << "\ty: " << goal.y << endl;
	cout << "now start:\n\tx: "<< start.x << endl;
	cout << "\ty: " << start.y << endl;
	cout << "-------------END getPosition\n";
	
}
void showWent(){
	cout << "--------------------------showWent\n";
	for(int x = 0 ; x < r;x++){
		for(int j = 0 ; j < c ; j++){
			cout << char(went[x][j]+'0');
		}
		cout << endl;
	}
	cout << "--------------------------\n";	
}
void showStage(position x){
	
	cout << "--------------------------showStage\n";
	for(int i = 0 ; i < r;i++){
		for(int j = 0 ; j < c ; j++){
			cout << x.stage[i][j];
		}
		cout << endl;
	}
	cout << "--------------------------\n";	
}
bool inBound(){
	return true;
}
bool checkBox(position n){
	
}
int BFS(position nnow,position goal){
//	cout << "welcome to BFS\n";
	que.push(nnow); // add a start state
	if(start.x == goal.x && start.y == goal.y){
		return 0;
	}
	 
//	for(int i = 0 ; i< r;i++)
//		for(int j = 0 ; j <c;j++)
//			went[i][j] = 0;
	while(1){
		if(que.empty()){
			return -1;	
		} 
		else{
			position now = que.front();
			que.pop();
//			went[now.x][now.y] = 1;
			
			for(int i = 0 ; i < 4 ; i++){
//				if(now.step==0 || now.stage[now.x+direction[i][0]][now.y+direction[i][1]]!='S')
				
				if(now.step==0 || (now.act[now.step-1] != zzz[i]))
				if(now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='.'
				||now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='T'
				||now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='B'
				||now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='S'){
//					showWent();
					
//					showStage(now);
					int Br,Bc;
//					cout << "--------------------------showStage\n";
					for(int z = 0 ; z < r;z++){
						for(int j = 0 ; j < c ; j++){
//							cout << now.stage[z][j];
							if(now.stage[z][j]=='B')
								Br=z,Bc=j;
						}
//						cout << endl;
					}
//					cout << "--------------------------\n";
					
					for(int z = 0 ; z < 4 ;z++){
						if(now.stage[Br+direction[z][0]][Bc+direction[z][1]]=='#')
						if(now.stage[Br+direction[(z+1)%4][0]][Bc+direction[(z+1)%4][1]]=='#')
							break;
							break;
					}
					
					position temp=now;
					temp.x = now.x+direction[i][0];
					temp.y = now.y+direction[i][1];
					
					
					if(now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='B'
						&&(now.stage[now.x+2*direction[i][0]][now.y+2*direction[i][1]]=='.'
						||now.stage[now.x+2*direction[i][0]][now.y+2*direction[i][1]]=='T')){
						temp.act[temp.step++] = ccc[i+4];
						temp.stage[now.x+direction[i][0]][now.y+direction[i][1]]='S';
						temp.stage[now.x+2*direction[i][0]][now.y+2*direction[i][1]]='B';
						temp.stage[now.x][now.y]='.';
						que.push(temp);
					}
					else if (now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='.'){
						temp.act[temp.step++] = ccc[i];
						temp.stage[now.x][now.y]='.';
						temp.stage[now.x+direction[i][0]][now.y+direction[i][1]]='S';
						que.push(temp);
					}
				
//					if(now.stage[now.x+direction[i][0]][now.y+direction[i][1]]=='T'){
					if(now.stage[goal.x][goal.y]=='B'){
						for(int i = 0 ; i <= now.step ; i++)
							cout << now.act[i];
						cout << "\nFOUND GOALLLL!!!!\n";
						return 1;
					}
					
					
				}
				
			}
		}
	} // end while(1)
	
	
}

/* MAPP:
3 5
#####
#TBS#
#####

3 7
#######
#T..BS#
#######

5 5
#####
#...#
#TBS#
#...#
#####

5 6
######
#....#
#T.BS#
#....#
######

5 6
######
#T#..#
#..BS#
#....#
######

7 11
###########
#T##......#
#.#.#..####
#....B...S#
#.######..#
#.........#
###########

7 11
###########
#.........#
#..T...####
#....B...S#
#.........#
#.........#
###########
*/
// 0-> w
// 1-> s
// 2-> e
// 3-> n

