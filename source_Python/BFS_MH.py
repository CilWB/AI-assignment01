mapp = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
 ['#', 'T', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
 ['#', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'S', '#'],
 ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
 ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

mapp = [
 ['#', '#', '#', '#', '#'],
 ['#', 'T', '#', '#', '#'],
 ['#', ' ', '#', ' ', '#'],
 ['#', 'B', ' ', ' ', '#'],
 ['#', ' ', ' ', ' ', '#'],
 ['#', 'S', ' ', ' ', '#'],
 ['#', ' ', ' ', ' ', '#'],
 ['#', '#', '#', '#', '#']
 ]

for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        print(mapp[i][j],end = '')
    print()

class MapState:
    def __init__(self,mapp):
        self.Sx,self.Sy,self.Tx,self.Ty = -1,-1,-1,-1
        self.Bx,self.By = -1,-1
        self.getPosition(mapp)
        self.sol = []
    def getPosition(self,mapp):
        for i in range(len(mapp)):
            for j in range(len(mapp[i])):
                if mapp[i][j] == 'S':
                    self.Sx = i
                    self.Sy = j
                if mapp[i][j] == 'T':
                    self.Tx = i
                    self.Ty = j
                if mapp[i][j] == 'B':
                    self.Bx = i
                    self.By = j

    def printPo(self):
        # return 'S:' + str(self.Sx) + ' ' + str(self.Sy) + '\n' + 'B:' + str(self.Bx) +' ' + str(self.By) + '\n' + 'T:' + str(self.Tx) +' ' + str(self.Ty) + 
        return    str(self.sol)

def BFS(State):
    node = State
    fron = []
    fron.append(node)
    explored = []
    while(True):
        if fron == []:
            return -1 
        # if node.Sx == 3 and node.Sy == 6:
        #     print('36')
        #     x = input()
        # x = input()
        # print(node.printPo())
        node = fron.pop(0)
        explored.append(node)
        ###for each##
        if mapp[node.Sx][node.Sy+1] != '#' and mapp[node.Sx][node.Sy+1] != 'B':
            temp = copy.deepcopy(node)
            temp.Sy += 1
            temp.sol.append('e')
            if temp not in explored:
                fron.append(temp)
            if temp.Bx == temp.Tx and temp.By == temp.Ty:
                return temp.sol
            # print('A')
        if mapp[node.Sx][node.Sy-1] != '#' and mapp[node.Sx][node.Sy-1] != 'B':
            temp = copy.deepcopy(node)
            temp.Sy -= 1
            temp.sol.append('w')
            
            if temp not in explored:
                fron.append(temp)
            if temp.Bx == temp.Tx and temp.By == temp.Ty:
                return temp.sol
            # print('B')
        if mapp[node.Sx+1][node.Sy] != '#' and mapp[node.Sx+1][node.Sy] != 'B':
            temp = copy.deepcopy(node)
            temp.Sx += 1
            temp.sol.append('s')
            
            if temp not in explored:
                fron.append(temp)
            if temp.Bx == temp.Tx and temp.By == temp.Ty:
                return temp.sol
            # print('C')
        if mapp[node.Sx-1][node.Sy] != '#' and mapp[node.Sx-1][node.Sy] != 'B':
            temp = copy.deepcopy(node)
            temp.Sx -= 1
            temp.sol.append('n')
            
            if temp not in explored:
                fron.append(temp)
            if temp.Bx == temp.Tx and temp.By == temp.Ty:
                return temp.sol
            # print('D')
        if node.Sx-2 >= 0:
            if mapp[node.Sx-2][node.Sy] != '#' and mapp[node.Sx-1][node.Sy] == 'B' :
                temp = copy.deepcopy(node)
                temp.Sx -= 1
                temp.Bx -= 1
                temp.sol.append('N')
                
                if temp not in explored:
                    fron.append(temp)
                if temp.Bx == temp.Tx and temp.By == temp.Ty:
                    return temp.sol
                # print('E')
        if node.Sx+2 < len(mapp) :
            if mapp[node.Sx+2][node.Sy] != '#' and mapp[node.Sx+1][node.Sy] == 'B' :
                temp = copy.deepcopy(node)
                temp.Sx += 1
                temp.Bx += 1
                temp.sol.append('S')
                
                if temp not in explored:
                    fron.append(temp)
                if temp.Bx == temp.Tx and temp.By == temp.Ty:
                    return temp.sol
                # print('F')
        if node.Sy+2 < len(mapp[node.Sx]):
            if  mapp[node.Sx][node.Sy+2] != '#' and mapp[node.Sx][node.Sy+1] == 'B' :
                temp = copy.deepcopy(node)
                temp.Sy += 1
                temp.By += 1
                temp.sol.append('E')
                
                if temp not in explored:
                    fron.append(temp)
                if temp.Bx == temp.Tx and temp.By == temp.Ty:
                    return temp.sol
                # print('G')
        if node.Sy-2 >= 0 :
            if mapp[node.Sx][node.Sy-2] != '#' and mapp[node.Sx][node.Sy-1] == 'B' :
                temp = copy.deepcopy(node)
                temp.Sy -= 1
                temp.By -= 1
                temp.sol.append('W')
                
                if temp not in explored:
                    fron.append(temp)
                if temp.Bx == temp.Tx and temp.By == temp.Ty:
                    return temp.sol
                # print('H')
        
        




####main#####
import copy
start = MapState(mapp)
print(start.printPo())
print (BFS(start))

"""

maptest

7x11
###########
#T##      #
# # #  ####
#  B    S #
#  ###### #
#         #
###########
"""    