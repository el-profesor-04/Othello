import copy
board=[]
for i in range(10):
  a=list(map(int,input().split()))
  board.append(a)
rn=copy.deepcopy(board)
player=int(input())
opponent=2 if player==1 else 1

#rnn=copy.deepcopy(rn)
node=(board,'max',1,1,player,opponent)
root=copy.deepcopy(node)
#print(node)

def findtrail(board,x,y,player,opponent):
  if board[x-1][y]==opponent and x!=0:
    for k in range(9):
      if board[x-k][y]==player and x-k>=0:
        for z in range(k+1):
          board[x-z][y]=player
        break
  try:
    if board[x+1][y]==opponent:
      for k in range(9):
        if board[x+k][y]==player:
          for z in range(k+1):
            board[x+z][y]=player
          break
  except:
    pass
  if board[x][y-1]==opponent and y!=0:
    for k in range(9):
      if board[x][y-k]==player and y-k>=0:
        for z in range(k+1):
          board[x][y-z]=player
        break
  try:
    if board[x][y+1]==opponent:
      for k in range(9):
        if board[x][y+k]==player:
          for z in range(k+1):
            board[x][y+z]=player
          break
  except:
    pass
  if board[x-1][y-1]==opponent and x!=0 and y!=0:
    for k in range(9):
      if board[x-k][y-k]==player and x-k>=0 and y-k>=0:
        for z in range(k+1):
          board[x-z][y-z]=player
        break
  try:
    if board[x-1][y+1]==opponent and x!=0:
      for k in range(9):
        if board[x-k][y+k]==player and x-k>=0:
          for z in range(k+1):
            board[x-z][y+z]=player
          break
  except:
    pass
  try:
    if board[x+1][y+1]==opponent:
      for k in range(9):
        if board[x+k][y+k]==player:
          for z in range(k+1):
            board[x+z][y+z]=player
          break
  except:
    pass
  try:
    if board[x+1][y-1]==opponent and y!=0:
      for k in range(9):
        if board[x+k][y-k]==player and y-k>=0:
          for z in range(k+1):
            board[x+z][y-z]=player
          break
  except:
    pass
  for i in range(10):
    for j in range(10):
      if board[i][j]==3:
        board[i][j]=0
  #print(board)
  return availchoice(board,opponent,player)

def availchoice(board,player,opponent):
  #print('availchoice',player,opponent)
  for m in range(10):
    for n in range(10):
      if board[m][n]==opponent:
        try:
            for q in range(9):
              if board[m-q][n]==player and m!=0 and board[m+1][n]==0:
                board[m+1][n]=3
                break
              elif board[m-q][n]==opponent:
                continue
              break
        except:
          pass
        try:
            for q in range(9):
              if board[m+q][n]==player and m!=0 and board[m-1][n]==0:
                board[m-1][n]=3
                break
              elif board[m+q][n]==opponent:
                continue
              break
        except:
          pass
        try:
            for q in range(9):
              if board[m][n-q]==player and n!=0 and board[m][n+1]==0:
                board[m][n+1]=3
                break
              elif board[m][n-q]==opponent:
                continue
              break
        except:
          pass
        try:
            for q in range(9):
              if board[m][n+q]==player and n!=0 and board[m][n-1]==0:
                board[m][n-1]=3
                break
              elif board[m][n+q]==opponent:
                continue
              break
        except:
          pass
        try:
          for q in range(9):
              if board[m-q][n-q]==player and n!=0 and m!=0 and board[m+1][n+1]==0:
                board[m+1][n+1]=3
                break
              elif board[m-q][n-q]==opponent:
                continue
              break
        except:
          pass
        try:
          for q in range(9):
              if board[m-q][n+q]==player and n!=0 and m!=0 and board[m+1][n-1]==0:
                board[m+1][n-1]=3
                break
              elif board[m-q][n+q]==opponent:
                continue
              break
        except:
          pass
        try:
          for q in range(9):
              if board[m+q][n-q]==player and n!=0 and m!=0 and board[m-1][n+1]==0:
                board[m-1][n+1]=3
                break
              elif board[m+q][n-q]==opponent:
                continue
              break
        except:
          pass
        try:
          for q in range(9):
              if board[m+q][n+q]==player and n!=0 and m!=0 and board[m-1][n-1]==0:
                board[m-1][n-1]=3
                break
              elif board[m+q][n+q]==opponent:
                continue
              break
        except:
          pass
  return board

def movegen(node):
  board=node[0]
  rnn=copy.deepcopy(board)
  player=node[4]
  opponent=node[5]
  childtype='max' if node[1]=='min' else 'min'
  depth=node[2]
  ele=node[3]
  no=0
  for w in range(10):
    no+=board[w].count(3)
  stlist=[]
  for i in range(10):
    for j in range(10):
      if board[i][j]==3:
        y=j
        x=i
        new=(findtrail(board,x,y,player,opponent),childtype,depth+1,ele*no,opponent,player)
        #print(stlist)
        if new not in stlist:
          stlist.append(new)
        board=copy.deepcopy(rnn)
  return stlist


#---------------------------------


def evaluation(node):
  player=node[4]
  opponent=node[5]
  board=node[0]
  val=0
  wincount=0
  loscount=0
  for x in range(10):
    if node[1]=='max':
      val+=(10*board[x].count(player))
      val-=(10*board[x].count(opponent))
      if board[x][0]==player:
        val+=1000
      elif board[x][0]==opponent:
        val-=1000
      if board[x][9]==player:
        val+=1000
      elif board[x][9]==opponent:
        val-=1000
      wincount+=board[x].count(player)
      loscount+=board[x].count(opponent)
    else:
      val+=(10*board[x].count(opponent))
      val-=(10*board[x].count(player))
      if board[x][0]==opponent:
        val+=1000
      elif board[x][0]==player:
        val-=1000
      if board[x][9]==opponent:
        val+=1000
      elif board[x][9]==player:
        val-=1000
      wincount+=board[x].count(opponent)
      loscount+=board[x].count(player)
  #if wincount>loscount and wincount+loscount==100:
  #  val+=10000
  if node[1]=='max':
    if board[0][2]==player:
      val+=100000
    elif board[0][2]==opponent:
      val-=100000
    if board[2][0]==player:
      val+=100000
    elif board[2][0]==opponent:
      val-=100000
    if board[0][7]==player:
      val+=100000
      #print('val')
    elif board[0][7]==opponent:
      val-=100000
    if board[2][7]==player:
      val+=100000
    elif board[2][7]==opponent:
      val-=100000
    if board[7][0]==player:
      val+=100000
    elif board[7][0]==opponent:
      val-=100000
    if board[9][2]==player:
      val+=100000
    elif board[9][2]==opponent:
      val-=100000
    if board[7][9]==player:
      val+=100000
    elif board[7][9]==opponent:
      val-=100000
    if board[9][7]==player:
      val+=100000
    elif board[9][7]==opponent:
      val-=100000
    if (board[0][0]==0 or board[0][0]==3 or board[0][0]==opponent) and (board[0][1]==player or board[1][0]==player or board[1][1]==player):
      val-=1000000
    if (board[0][9]==0 or board[0][9]==3 or board[0][9]==opponent) and (board[0][8]==player or board[1][9]==player or board[1][8]==player):
      val-=1000000
    if (board[9][0]==0 or board[9][0]==3 or board[9][0]==opponent) and (board[9][1]==player or board[8][0]==player or board[8][1]==player):
      val-=1000000
    if (board[9][9]==0 or board[9][9]==3 or board[9][9]==opponent) and (board[9][8]==player or board[8][9]==player or board[8][8]==player):
      val-=1000000
    val+=(1000*board[0].count(player))
    val+=(1000*board[9].count(player))
    val-=(1000*board[0].count(opponent))
    val-=(1000*board[9].count(opponent))
    if board[0][0]==player:
      val+=500000
    elif board[0][0]==opponent:
      val-=500000
    if board[0][9]==player:
      val+=500000
    elif board[0][9]==opponent:
      val-=500000
    if board[9][0]==player:
      val+=500000
    elif board[9][0]==opponent:
      val-=500000
    if board[9][9]==player:
      val+=500000
    elif board[9][9]==opponent:
      val-=500000
    '''
    if board[4][4]==player:
      val+=20
    else:
      val-=20
    if board[4][5]==player:
      val+=20
    else:
      val-=20
    if board[5][4]==player:
      val+=20
    else:
      val-=20
    if board[5][5]==player:
      val+=20
    else:
      val-=20'''
  else:
    if board[0][2]==opponent:
      val+=100000
    elif board[0][2]==player:
      val-=100000
    if board[2][0]==opponent:
      val+=100000
    elif board[2][0]==player:
      val-=100000
    if board[0][7]==opponent:
      val+=100000
    elif board[0][7]==player:
      val-=100000
    if board[2][7]==opponent:
      val+=100000
    elif board[2][7]==player:
      val-=100000
    if board[7][0]==opponent:
      val+=100000
    elif board[7][0]==player:
      val-=100000
    if board[9][2]==opponent:
      val+=100000
    elif board[9][2]==player:
      val-=100000
    if board[7][9]==opponent:
      val+=100000
    elif board[7][9]==player:
      val-=100000
    if board[9][7]==opponent:
      val+=100000
    elif board[9][7]==player:
      val-=100000
    if (board[0][0]==0 or board[0][0]==3 or board[0][0]==player) and (board[1][1]==opponent or board[1][0]==opponent or board[0][1]==opponent):
      val-=1000000
    if (board[0][9]==0 or board[0][9]==3 or board[0][9]==player) and (board[0][8]==opponent or board[1][9]==opponent or board[1][8]==opponent):
      val-=1000000
    if (board[9][0]==0 or board[9][0]==3 or board[9][0]==player) and (board[9][1]==opponent or board[8][0]==opponent or board[8][1]==opponent):
      val-=1000000
    if (board[9][9]==0 or board[9][9]==3 or board[9][9]==player) and (board[9][8]==opponent or board[8][9]==opponent or board[8][8]==opponent):
      val-=1000000
    val+=(1000*board[0].count(opponent))
    val+=(1000*board[9].count(opponent))
    val-=(1000*board[0].count(player))
    val-=(1000*board[9].count(player))
    if board[0][0]==opponent:
      val+=500000
    elif board[0][0]==player:
      val-=500000
    if board[0][9]==opponent:
      val+=500000
    elif board[0][9]==player:
      val-=500000
    if board[9][0]==opponent:
      val+=500000
    elif board[9][0]==player:
      val-=500000
    if board[9][9]==opponent:
      val+=500000
    elif board[9][9]==player:
      val-=500000
    '''
    if board[4][4]==opponent:
      val+=20
    else:
      val-=20
    if board[4][5]==opponent:
      val+=20
    else:
      val-=20
    if board[5][4]==opponent:
      val+=20
    else:
      val-=20
    if board[5][5]==opponent:
      val+=20
    else:
      val-=20'''
  return val

def terminal(node):
  if node[2]==3 :# or len(movegen(node))==0:
    return True
  else:
    return False

#-------------------------------------

def bestmove(node):
  b=[]
  value=-10000000
  for s in movegen(node):
    temp=copy.deepcopy(s)
    vj=alphabeta(s)
    print(vj)
    if vj > value:
      value=vj
      b=temp
  return b

def alphabeta(j,alpha=-10000000,beta=10000000):
  #print(j,'j',j[4],j[5])
  if terminal(j):
    return evaluation(j)
  else:
    #print(j,'j bb stl')
    if j[1]=='max':
      stl=movegen(j)
      for c in range(len(stl)):
        alpha=max(alpha,alphabeta(stl[c],alpha,beta))
        if alpha>=beta:
          return beta
        if c==len(stl)-1:
          return alpha
    else:
     # print(j,'j b stl')
      stl=movegen(j)
      #print(stl,'stl')
      for c in range(len(stl)):
       # print(stl[c],' c ',c,len(stl))
        beta=min(beta,alphabeta(stl[c],alpha,beta))
        #print(beta,'beta')
        if alpha>=beta:
          return alpha
        if c==len(stl)-1:
          return beta
  return 0

#------------------------------

choice=bestmove(node)
#print(choice)


def output(choice,root):
  fboard=choice[0]
  #print(fboard)
  r=copy.deepcopy(root[0])
  player=root[4]
  opponent=root[5]
  for u in range(10):
    for v in range(10):
      if r[u][v]==3:
        #print(findtrail(r,u,v,player,opponent),u,v)
        if findtrail(r,u,v,player,opponent)==fboard:
          print(u,v)
          return
        else:
          r=copy.deepcopy(root[0])

#print('movegen')
#print(movegen(([[0, 0, 0, 0, 0, 0, 3, 1, 0, 0], [0, 0, 0, 0, 0, 3, 3, 1, 3, 0], [0, 0, 3, 0, 3, 1, 3, 1, 2, 2], [0, 0, 3, 1, 1, 1, 1, 1, 2, 2], [0, 0, 3, 1, 1, 1, 2, 1, 2, 2], [0, 3, 1, 1, 2, 2, 1, 1, 3, 2], [0, 3, 1, 1, 2, 1, 1, 3, 3, 2], [0, 0, 1, 1, 1, 1, 1, 3, 0, 0], [0, 3, 3, 3, 1, 3, 3, 3, 0, 0], [0, 0, 0, 3, 3, 0, 0, 0, 0, 0]], 'min', 2, 3, 2, 1)))
output(choice,root)


'''
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 0 0 0 0
0 0 0 0 1 2 3 0 0 0
0 0 0 3 2 1 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1


0 3 1 1 1 0 0 0 0 0
0 3 2 1 3 3 3 3 0 0
1 1 2 2 1 2 2 1 0 0
0 1 2 2 2 1 2 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0
0 0 0 0 0 1 1 1 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
1

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 3 2 1 0 0 0 0 0
0 0 0 3 2 1 0 0 0 0
0 0 0 0 1 2 3 0 0 0
0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1

0 0 0 0 0 0 0 3 0 0
0 0 0 0 0 0 0 2 3 3
0 0 0 0 0 1 0 2 2 2
0 0 0 1 1 1 1 2 2 2
0 0 0 1 1 1 2 1 2 2
0 0 1 1 2 2 1 1 0 2
0 0 1 1 2 1 1 0 0 2
0 0 1 1 1 1 1 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1

([[0, 0, 0, 0, 0, 0, 3, 1, 0, 0], [0, 0, 0, 0, 0, 3, 3, 1, 3, 0], [0, 0, 3, 0, 3, 1, 3, 1, 2, 2], [0, 0, 3, 1, 1, 1, 1, 1, 2, 2], [0, 0, 3, 1, 1, 1, 2, 1, 2, 2], [0, 3, 1, 1, 2, 2, 1, 1, 3, 2], [0, 3, 1, 1, 2, 1, 1, 3, 3, 2], [0, 0, 1, 1, 1, 1, 1, 3, 0, 0], [0, 3, 3, 3, 1, 3, 3, 3, 0, 0], [0, 0, 0, 3, 3, 0, 0, 0, 0, 0]], 'min', 2, 3, 2, 1)
'''