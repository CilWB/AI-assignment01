class Problem:
  def __init__(self,prb):
    
    self.sol = []
    self.state = prb
    self.pathC = 0
    self.x,self.y,self.bx,self.by,self.gx,self.gy = -1,-1,-1,-1,-1,-1
    self.directionS = [[-1,0,'n'],[0,-1,'w'],[1,0,'s'],[0,1,'e']]
                       
    self.directionB = [[-1,0,'N',-2,0], #N
              [1,0,'S',2,0], #S
              [0,-1,'W',0,-2], #W
              [0,1,'E',0,2] #E
                     ]
    
    
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
    if child.state[node.x][node.y] != 'T':
          child.state[child.x][child.y] = ' '
    child.x,child.y = child.x+act[0],child.y+act[1]
    if child.state[child.x][child.y] != 'T':
          child.state[child.x][child.y] = 'S'
    
    
  else:
        if child.state[child.x][child.y] != 'T':
          child.state[child.x][child.y] = ' '
        if child.state[child.x+act[0]][child.y+act[1]] != 'T':
          child.state[child.x+act[0]][child.y+act[1]] = 'S'
        child.state[child.x+act[3]][child.y+act[4]] = 'B'
        child.bx,child.by = child.bx+act[0],child.by+act[1]
        child.x,child.y = child.x+act[0],child.y+act[1]   
        
        
  sol = act[2]
  return child,sol
  
  
def DFS_limit(prb,limit):
  visit=[]
  return DFS_limitrecur(copy.deepcopy(prb),prb,limit,visit)

def DFS_limitrecur(node,prb,limit,visit=[]):
 
  for i in range(4):
     if node.state[node.bx+node.directionS[i][0]][node.by+node.directionS[i][1]]=='#' and node.state[node.bx+node.directionS[(i+1)%4][0]][node.by+node.directionS[(i+1)%4][1]]=='#':
        return 0

  visit.append(node.state)

  if prb.goalTest(node):
    return node.sol
  elif limit == 0:
    if visit != []:
       visit.pop()
    return 0
  else:
    cutoff = False
    for action in prb.Action(node):
       child,tempsol = Child(node,action)
       child.sol.append(tempsol)

       if prb.goalTest(child):
          return child.sol
       elif child.state in visit:
          result = 0
       else:
          result =  DFS_limitrecur(child,prb,limit-1,visit)

       if result== 0: #cutoff
          cutoff = True
       elif result != -1:
          return result
      

    if cutoff:
      if visit != []:
        visit.pop()
      return 0
    else:
      return -1
      
  
def IDS(prb):
  d = 0
  overround = len(prb.state)*len(prb.state[0])
  ans = []
  while True:
    if d > overround:
      print('Goal not Found!!')
      return ans 
    result = DFS_limit(prb,d)
    if result != 0:
      if result == []:
        print('Goal not Found!!')
      else:
        #print('Found Goal!!')
        return result
        if result not in ans:
          ans.append(result)
    elif result == -1:
      print('Goal not Found!!')
      return []
    d+=1


import copy


R,C = input("Enter Map's size (RxC) : ").split('x')
R,C = int(R),int(C)

mapp = [[' '] * C for i in range(R)]

for i in range(R):
    mapp[i][:C]=input()
    if len(mapp[i]) > C:
      print("out range !!!")  
      break
      

# import pandas as pd
print('Map Problem: ')

prb = Problem(mapp)
print('start => ',prb.getposition())
print('goal => ',prb.getGoalposition())
print('box => ',prb.getBoxposition())


import time
start_time = time.time()
# print(pd.DataFrame(prb.state)) 


print(*IDS(prb))

print("--- %s seconds ---" % (time.time() - start_time))



"""
mapp = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
 ['#', 'T', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#'],
 ['#', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'S', '#'],
 ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#'],
 ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
"""
"""
#  #  #  #  #
#  T  #     #
#  S  B     #
#        #  #
#           #
#  #  #  #  #

8x8
########
#T# #  #
#      #
#  B # #
#      #
# #### #
#     S#
########

12x12
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



"""