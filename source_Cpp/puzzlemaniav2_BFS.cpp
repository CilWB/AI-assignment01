#include <bits/stdc++.h>
#define MAPHEIGHT 20
#define MAPLENGTH 20

using namespace std;
 
typedef struct po{
	int x,y,step;
	int Br,Bc;
	char act[50];
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
bool checkLoop4(position);
int BFS(position,position);

int main(){
//	cout << "welcome back CXz." << endl;
	getIn();
	getPosition();
//	showMap();
//	showStage(start);
	cout << "BFS " << BFS(start,goal);
	while(1);
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
//	cout << "-------------USE getPosition\n";
	for(int i = 0 ; i < r;i++){
		for(int j = 0 ; j < c ; j++){
			if(mapp[i][j]=='T') goal.x = i , goal.y = j,mapp[i][j]='.';
			else if(mapp[i][j]=='S') start.x = i, start.y = j,mapp[i][j]='.';
			else if(mapp[i][j]=='B') start.Br = i,start.Bc = j,mapp[i][j]='.';
		}
	}
	start.step = 0;
//	cout << "goal :\n\tx: " << goal.x << endl;
//	cout << "\ty: " << goal.y << endl;
//	cout << "now start:\n\tx: "<< start.x << endl;
//	cout << "\ty: " << start.y << endl;
//	cout << "now box:\n\tBr: "<< start.Br << endl;
//	cout << "\tBc: " << start.Bc << endl;
//	
//	cout << "-------------END getPosition\n";
	
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
	for(int i = 0 ;i < r ; i++){
		for(int j = 0 ; j < c ; j++){
			if(x.Br==i&&x.Bc==j) cout << 'B';
			else if(x.x==i&&x.y==j) cout << 'S';
			else if(goal.x==i&&goal.y==j) cout <<'T';
			else cout<<mapp[i][j];
		}
		cout << endl;
	}
	for(int i = 0 ; i < x.step ; i++)
		cout<< x.act[i];
	cout << endl;
	cout << "--------------------------\n";	
}
bool inBound(){
	return true;
}
bool checkBox(position n){
	
}
bool checkLoop4(position n){
	return (n.act[n.step-1]+n.act[n.step-2]+n.act[n.step-3]+n.act[n.step-4])==('n'+'s'+'w'+'e');
}
int BFS(position nnow,position goal){
//	cout << "welcome to BFS\n";
	que.push(nnow); // add a start state
	bool ok;
	if(start.x == goal.x && start.y == goal.y){
		return 0;
	}
	while(1){
		if(que.empty()){
			return -1;	
		} 
		else{
			position now = que.front();
			que.pop();
			
			if(now.Br==goal.x&&now.Bc==goal.y){
				for(int i = 0 ; i <= now.step ; i++)
					cout << now.act[i];
				cout << "\nFOUND GOALLLL!!!!\n";
				return 1;
			}
			
			ok = true;
			for(int z = 0 ; z < 4 ;z++){
//				cout <<"yeah!\n";
//				cout << mapp[now.Br+direction[z][0]][now.Bc+direction[z][1]] ;
//				cout << mapp[now.Br+direction[(z+1)%4][0]][now.Bc+direction[(z+1)%4][1]] << endl;;
				if(mapp[now.Br+direction[z][0]][now.Bc+direction[z][1]]=='#')
				if(mapp[now.Br+direction[(z+1)%4][0]][now.Bc+direction[(z+1)%4][1]]=='#'){
					ok = false;
				}
			}
			if(now.step>3 && checkLoop4(now)){
				ok = false;
			}
			if(ok == false) continue;	
			
			
			
			for(int i = 0 ; i < 4 ; i++){
			
				if(now.step==0 || (now.act[now.step-1] != zzz[i]))
				if(now.step<50)
				if(mapp[now.x+direction[i][0]][now.y+direction[i][1]]!='#'){
//					showStage(now);
					
					for(int z = 0 ; z < 4 ;z++){
						if(mapp[now.Br+direction[z][0]][now.Bc+direction[z][1]]=='#')
						if(mapp[now.Br+direction[(z+1)%4][0]][now.Bc+direction[(z+1)%4][1]]=='#'){
							break;
							break;
						}
					}
					if(now.step>3 &&checkLoop4(now)){
						break;
						break;
					}
					
					position temp=now;
					temp.x = now.x+direction[i][0];
					temp.y = now.y+direction[i][1];
					
					
					if( (now.x+direction[i][0])==now.Br && (now.y+direction[i][1])==now.Bc
						&&(mapp[now.x+2*direction[i][0]][now.y+2*direction[i][1]]!='#')){
						temp.act[temp.step++] = ccc[i+4];
						
						temp.Br = now.x+2*direction[i][0];
						temp.Bc = now.y+2*direction[i][1];
						
						que.push(temp);
					}
					else if (mapp[now.x+direction[i][0]][now.y+direction[i][1]]=='.'){
						temp.act[temp.step++] = ccc[i];
						que.push(temp);
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
wwwWWWWWeeeeeesswwwwwwwnNN

7 11
###########
#.........#
#..T...####
#....B...S#
#.........#
#.........#
###########

8 8
########
#T#.#..#
#......#
#..B.#.#
#......#
#.####.#
#.....S#
########

7 11
###########
#.........#
#..T......#
#....B....#
#.........#
#........S#
###########

7 11
###########
#T.....B..#
#########.#
#.........#
#.#########
#........S#
###########

7 11
###########
#T.#S.....#
#.#.#B.####
#.........# 
#.######..#
#.........#
###########


15 11
###########
#..T......#
#.........#
#.........#
#.........#
#.........#
#.........#
#.........#
#.B.......#
#.........#
#.........#
#.........#
#.........#
#........S#
###########

12 12
############
#...T#..#S.#
#..#...#.#.#
##.....#.#.#
##.#...#.#.#
##.##..#.#.#
##..###..#.#
##..######.#
#.B........#
##..#####..#
##..#...#..#
############


12 12
############
#...T#..#S.#
#..#...#.#.#
##.#...#.#.#
##.....#.#.#
##.##..#.#.#
##..###..#.#
##..######.#
#..........#
##..#####B.#
#.......#..#
############

12 12
############
#...T#..#S.#
#..#...#...#
##.#...#...#
##.....#...#
##.##..#...#
##..###....#
##..######.#
#..........#
##..#####B.#
#.......#..#
############

12 12
############
#...T#..#S.#
#..#...#.#.#
#..#...#.#.#
#......#...#
#..##..#.#.#
#...###..#.#
##..#..###.#
#..........#
##.######B.#
#..........#
############
essssssssswNenWWWWWWWeeeeeesswwwwwwwnNNNNNNNwnEE

12 15
###############
#.T........B..#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#............S#
###############

15 15
###############
#.T........B..#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#.............#
#............S#
###############

20 20
####################
#..................#
#..T...............#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#..................#
#......B...........#
#..................#
#..................#
#..................#
#.................S#
####################
 




*/
// 0-> w
// 1-> s
// 2-> e
// 3-> n

