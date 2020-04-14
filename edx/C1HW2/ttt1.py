
import numpy as np


def create_board():
	return(np.zeros((3,3)))

def place(board,player,position):
	x,y=position
	if board[x][y]==0:
		board[x][y]=player

def possibilities(board):
	return(np.where(board==0))

def random_place(board,player):
	librex,librey=possibilities(board)
	rx=np.random.choice(librex)
	ry=np.random.choice(librey)
	if board[rx][ry]==0:
		board[rx][ry]=player
	
def row_win(board,player):
	if np.any(np.all(board==player,axis=0)==True):
		return True
	else:
		return False

def col_win(board,player):
	if np.any(np.all(board==player,axis=1)==True):
		return True
	else:
		return False

def diag_win(board,player):
	if np.all(np.diag(board,0)==player) or np.all(np.diag(np.fliplr(board),0)==player):
		return True
	else:
		return False



np.random.seed(1)
X=create_board()
X[1][1]=1

ganador=False

while not ganador:
	for player in [1,2]:
		posicion=random_place(X,player)
		if player==1:
			player=2
		else:
			player=1
		if  row_win(X,player) or col_win(X,player) or diag_win(X,player):
			print ("el ganador es player ", player)	
			ganador=True
			break
	

print(X)
# place(X,1,posicion)


