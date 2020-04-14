
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
	#print(librex,librey)
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

 
def evaluate_board(board):
	winner=0
	for player in [1,2]:
		if col_win(board,player) or row_win(board,player) or diag_win(board,player):
			winner=player
	if np.all(board!=0) and winner == 0:
		winner=-1

	return winner
	


#np.random.seed(1)
X=create_board()
#X[1][1]=1

ganador=0
while ganador==0:
	for player in [1,2]:
		posicion=random_place(X,player)
		ganador= evaluate_board(X) 
		
		if ganador!=0:
			break
	
print("el ganador es ", ganador )
print(X)


