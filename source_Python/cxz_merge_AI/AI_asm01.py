class Problem:
  def __init__(self,prb):
    
    self.sol = []       #solution
    self.state = prb    #current map
    self.x,self.y,self.bx,self.by,self.gx,self.gy = -1,-1,-1,-1,-1,-1  #initial position of S,B,T
    self.directionS = [[-1,0,'n'],[0,-1,'w'],[1,0,'s'],[0,1,'e']]      #S actions                     
    self.directionB = [[-1,0,'N',-2,0],[1,0,'S',2,0],[0,-1,'W',0,-2],[0,1,'E',0,2]] #S and B actions
    
    #------get S,B,T positions from map------#
    for i in range(len(self.state)):
      for j in range(len(self.state[0])):
        if self.state[i][j] == 'S':
          self.setposition(i,j)
        elif self.state[i][j] == 'T':
          self.setGoalposition(i,j)
        elif self.state[i][j] == 'B':
          self.setBoxposition(i,j)


  def setposition(self,x,y):
    self.x,self.y = x,y
    
  def getposition(self):
    return self.x,self.y
  
  def setBoxposition(self,bx,by):
    self.bx,self.by = bx,by
    
  def getBoxposition(self):
    return self.bx,self.by
  
  def setGoalposition(self,gx,gy):
    self.gx,self.gy = gx,gy
    
  def getGoalposition(self):
    return self.gx,self.gy
    
  def goalTest(self,stateNode):
    if stateNode.getBoxposition() == stateNode.getGoalposition():
      return True
    return False
  
  def Action(self,node):
    action = []
    for i in range(4):
      if node.state[node.x+node.directionB[i][0]][node.y+node.directionB[i][1]] == 'B' and node.state[node.x+node.directionB[i][3]][node.y+node.directionB[i][4]] != '#':
         action.append(node.directionB[i])  
          
      if node.state[node.x+node.directionS[i][0]][node.y+node.directionS[i][1]]  != '#' and node.state[node.x+node.directionS[i][0]][node.y+node.directionS[i][1]] != 'B':
         action.append(node.directionS[i]) 
          
    return action 
    
def Child(node,act):
  
  child = copy.deepcopy(node)
  if len(act)==3:

    #------S actions------#
    if child.state[node.x][node.y] != 'T':
          child.state[child.x][child.y] = ' '
    child.x,child.y = child.x+act[0],child.y+act[1]
    if child.state[child.x][child.y] != 'T':
          child.state[child.x][child.y] = 'S'    
    
  else:
    #------S and B actions------#
        if child.state[child.x][child.y] != 'T':
          child.state[child.x][child.y] = ' '
        if child.state[child.x+act[0]][child.y+act[1]] != 'T':
          child.state[child.x+act[0]][child.y+act[1]] = 'S'
        child.state[child.x+act[3]][child.y+act[4]] = 'B'
        child.bx,child.by = child.bx+act[0],child.by+act[1]
        child.x,child.y = child.x+act[0],child.y+act[1]   
         
  sol = act[2]
  return child,sol
  
  

def BFS(prb):
  fron = []
  node = copy.deepcopy(prb)

  if prb.goalTest(node):
    return node.sol
  
  fron.append(node) #frontier
  explored = []  
  
  while True:
    if fron==[]:
      print('Goal not Found!!')
      return [-1]

    node = fron.pop(0)
    
    if node.state in explored: #avoid loop
      continue
    
    explored.append(node.state)

    #-----Check if Box can not move-----#
    for i in range(4):
      if node.state[node.bx+node.directionS[i][0]][node.by+node.directionS[i][1]]=='#' and node.state[node.bx+node.directionS[(i+1)%4][0]][node.by+node.directionS[(i+1)%4][1]]=='#':       
        continue 
    
    for action in prb.Action(node):
      child,tempsol = Child(node,action)
      child.sol.append(tempsol)

      
      if child.state not in explored and child.state not in fron:
        if prb.goalTest(child):
          print('Found Goal!!')
          return child.sol
      fron.append(child)
      
    
  
def DFS_limit(prb,limit):
  sol = []
  fron = []
  node = copy.deepcopy(prb)
  if prb.goalTest(node):
    return node.sol
  
  fron.append(node)
  explored = []

  while True:
    if fron==[]:
      break
    node = fron.pop(0)
    explored.append(node.state)
    if len(node.sol) > limit :
        continue
    
    for i in range(4):
      if node.state[node.bx+node.directionS[i][0]][node.by+node.directionS[i][1]]=='#'and node.state[node.bx+node.directionS[(i+1)%4][0]][node.by+node.directionS[(i+1)%4][1]]=='#':
        # print('fail can not move Box')
        break
        continue

    for action in prb.Action(node):
      child,tempsol = Child(node,action)
      child.sol.append(tempsol)
      
      if child.state not in explored and child.state not in fron:
        if prb.goalTest(child):
          sol.append(child.sol)
        fron.append(child)
  
  return sol
  
  
def IDS(prb,limit):
  for i in range(limit):
    # print(i)
    sol = DFS_limit(prb,i)
    if sol != []:
        return sol

      
#---------------------------------------
#main     
#---------------------------------------
import copy
import time
#import psutil

R,C = input("Enter Map's size (RxC) : ").split('x')
R,C = int(R),int(C)

mapp = [[' '] * C for i in range(R)]
for i in range(R):
    mapp[i][:C]=input()
    if len(mapp[i]) > C:
      print("out range !!!")
      break
      

print('Map Problem: ')
prb = Problem(mapp)
print('start : ',prb.getposition())
print('box : ',prb.getBoxposition())
print('goal : ',prb.getGoalposition())




start_time = time.time()

print(BFS(prb))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

print(IDS(prb,25))

print("--- %s seconds ---" % (time.time() - start_time))

"""
# gives a single float value
psutil.cpu_percent()
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary 
memused = dict(psutil.virtual_memory()._asdict())
print('Space usage = ',memused)

-------------------------------------------------------
maptest

5x5
#####
#T  #
# B #
#  S#
#####

6x6
######
#T   #
# B  #
#    #
#   S#
######
[['n', 'n', 'w', 'W', 's', 'w', 'N'],

8x8
########
#T# #  #
#      #
#  B # #
#      #
# #### #
#     S#
########

############
#   T#  #S #
#  #   #   #
## #   #   #
##     #   #
## ##  #   #
##  ###    #
##  ###### #
#          #
##  #####B #
#       #  #
############


###############
# T        B  #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#            S#
###############


7x11
###########
#T##      #
# # #  ####
#    B   S#
# ######  #
#         #
###########



########
#  S # #
#     T#
# B ## #
#      #
# #### #
#      #
########


20x20
####################
#                  #
#  T               #
#                  #
#                  #
#                  #
#       B    S     #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
#                  #
####################

"""    

