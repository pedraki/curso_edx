import numpy as np 
import pygame
import time  



pygame.init()

width, height = 700,700 
screen=pygame.display.set_mode((height,width))
bg=25,25,25
screen.fill(bg)
nxC,nyC=50,50
dimcW=width/nxC
dimcH=height/nyC

#1 vivas 0 muertas
gameState=np.zeros((nxC,nyC))
 
gameState[5,3]=1
gameState[5,4]=1
gameState[5,5]=1

gameState[21,21]=1
gameState[22,22]=1
gameState[22,23]=1
gameState[21,23]=1
gameState[20,23]=1

pauseExect=False
juego=True
while juego:

	newgameState=np.copy(gameState)
	screen.fill(bg)
	time.sleep(0.1)
	ev=pygame.event.get()
	for evento in ev:
		if evento.type == pygame.QUIT:
			juego=False
		#pygame.KEYDOWM ES AL bajar CUALQUIER TECLA keyup es al subir
		if evento.type == pygame.KEYDOWN:
			pauseExect = not pauseExect
	#mouseClick tupla (izdo,central, derecho) 0 no pulsado 1 pulsado
		mouseClick=pygame.mouse.get_pressed()
		if sum(mouseClick) > 0:
			posX,posY=pygame.mouse.get_pos()
			celX,celY = int(np.floor(posX/dimcW)),int(np.floor(posY/dimcH))
			print(celX,celY)
			#mouseclick 
			gameState[celX,celY]=not mouseClick[2]
		

	if not pauseExect:
		
		for y in range(nxC):
			for x in range(nyC):
				
			#numero de vecinos
				n_neigh = gameState[(x-1) % nxC, (y+1) % nyC]+ \
						  gameState[(x)   % nxC, (y+1) % nyC]+ \
						  gameState[(x+1) % nxC, (y+1) % nyC]+ \
						  gameState[(x-1) % nxC, (y)   % nyC]+ \
						  gameState[(x+1) % nxC, (y)   % nyC]+ \
						  gameState[(x-1) % nxC, (y-1) % nyC]+ \
						  gameState[(x)   % nxC, (y-1) % nyC]+ \
						  gameState[(x+1) % nxC, (y-1) % nyC] 

		#muerta con 3 vecinas vivas revive
				if gameState[x,y]==0 and n_neigh==3:
					newgameState[x,y]=1
	#viva con menos de 2 o mas de 3 vecinas vivas muere
				elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
					newgameState[x,y] =0

				poly=[
				((x) * dimcW, y * dimcH), 
				((x+1) * dimcW , y * dimcH),
				((x+1) * dimcW ,(y+1) * dimcH),
				((x) * dimcW ,(y+1) * dimcH)
				]
				
				#pantalla, color, punto,ancho
				if newgameState[x,y]==0:
					pygame.draw.polygon(screen,(128,128,128),poly,1)
				else:
					pygame.draw.polygon(screen,(255,255,255),poly,0)

		gameState=np.copy(newgameState)
		pygame.display.flip()
	
