import copy
mapp = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
 ['#', 'T', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
 ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '#'],
 ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
 ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        print(mapp[i][j],end='')
    print()
print(len(mapp),len(mapp[0]))

# def getPosition(mapp):
#     Sx=Sy=Tx=Ty = 0
#     for i in range(len(mapp)):
#         for j in range(len(mapp[i])):
#             if mapp[i][j] =='S':
#                 Sx,Sy = i,j
#             elif mapp[i][j] == 'T':
#                 Tx,Ty =i,j
#     print('S:',Sx,Sy)
#     print('T:',Tx,Ty)

# getPosition(mapp)

class State:
    def __init__(self,mapp):
        self.Sx = -1
        self.Sy = -1
        self.Tx = -1
        self.Ty = -1
        self.act = []
        for i in range(len(mapp)):
            for j in range(len(mapp[i])):
                if mapp[i][j] =='S':
                    self.Sx,self.Sy = i,j
                elif mapp[i][j] == 'T':
                    self.Tx,self.Ty =i,j
    def _print(self):
        print('---------------------------')
        print('S:',self.Sx,self.Sy)
        print('T:',self.Tx,self.Ty) 
        print('---------------------------')
    
    # def __str__(self):
    #     return 'S:'+str(self.Sx)+str(self.Sy)+'\nT:'+str(self.Tx)+str(self.Ty)
start = State(mapp)

def BFS(startState):
    node = startState
    que = []
    que.append(node)
    explored = []
    while(True):
        if que == [] :
            return -1
        node = que.pop(0)
        # node._print()
        explored.append(node)
        # for each action
        if mapp[node.Sx+1][node.Sy] != '#' :
            temp = copy.deepcopy(node)
            temp.Sx += 1
            temp.act.append('s')
            que.append(temp)
        if mapp[node.Sx-1][node.Sy] != '#' :
            temp = copy.deepcopy(node)
            temp.Sx -= 1
            temp.act.append('n')
            que.append(temp)
        if mapp[node.Sx][node.Sy+1] != '#' :
            temp = copy.deepcopy(node)
            temp.Sy += 1
            temp.act.append('e')
            que.append(temp)
        if mapp[node.Sx][node.Sy-1] != '#' :
            temp = copy.deepcopy(node)
            temp.Sy -= 1
            temp.act.append('w')
            que.append(temp)

        if temp.Sx == temp.Tx and temp.Sy == temp.Ty :
            return temp.act
        # if temp not in explored :

        # if now.Sx==now.Tx and now.Sy == now.Ty:


R,C = input("Enter Map's size (RxC) : ").split('x')
R,C = int(R),int(C)

mapp = [[' '] * C for i in range(R)]
for i in range(R):
    mapp[i][:C]=input()
    if len(mapp[i]) > C:
      print("out range !!!")
      break  
start = State(mapp) 
print(BFS(start))


"""
8x10
##########
#T.......#
#........#
#........#
#........#
#........#
#.......S#
##########

"""