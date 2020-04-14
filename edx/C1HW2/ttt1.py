
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
	return(rx,ry)



X=create_board()
player=1
for x in range(9):
	posicion=random_place(X,player)
	if player==1:
		player=2
	else:
		player=1

	print(posicion)
	place(X,player,posicion)

print(X)
# place(X,1,posicion)


