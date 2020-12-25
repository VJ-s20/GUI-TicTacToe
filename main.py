import math
import random
class player:
    def __init__(self,value):
        self.value=value

class  computer_move(player):
    """
    computer choices randomly
    """
    def __init__(self, value):
        super().__init__(value)
    
    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square


class HumanPlayer(player):
    def __init__(self, value):
        super().__init__(value)

    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.value+"Move Enter in betweeen 0,8:")
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("Invalid square, Try again!")

        return val

class superComputer(player):
    def __init__(self, value):
        super().__init__(value) 

    def get_move(self,game):
        if len(game.available_moves())==9:
            square=random.choice(game.available_moves())
        else:
            square=self.minMax(game,self.value)["position"]
        print(square)
        return square

    def minMax(self,state,player):
        max_player=self.value #computer 
        other_player="O" if player=="X" else "X"

        # check the winner first
        if state.current_winner==other_player:
            return {"position":None,"score":1*(state.num_empty_square()+1) if other_player==max_player else -1*(state.num_empty_square()+1) }

        elif not state.empty_square():
            return {"position":None,"score":0}

        if player==max_player:
            best= {"position":None,"score":-math.inf}   #each score should increase maxima
        else:
            best= {"position":None,"score":math.inf} #each score should increase the minima of other player

        for possible_move in state.available_moves():
            state.make_move(possible_move,player)
            sim_score=self.minMax(state,other_player)

            # undo the move
            state.board[possible_move]=" "
            state.current_winner=None

            sim_score["position"]=possible_move

            if player==max_player:
                if sim_score["score"]>best["score"]:
                    best=sim_score
            else:
                 if sim_score["score"]<best["score"]:
          
                    best=sim_score
        # print(best)
        return best




# import pygame, sys
# import numpy as np

# # initializes pygame
# pygame.init()

# # ---------
# # CONSTANTS
# # ---------
# WIDTH = 600
# HEIGHT = 600
# LINE_WIDTH = 15
# WIN_LINE_WIDTH = 15
# BOARD_ROWS = 3
# BOARD_COLS = 3
# SQUARE_SIZE = 200
# CIRCLE_RADIUS = 60
# CIRCLE_WIDTH = 15
# CROSS_WIDTH = 25
# SPACE = 55
# # rgb: red green blue
# RED = (255, 0, 0)
# color=(0,0,0)
# BG_COLOR = (28, 170, 156)
# LINE_COLOR = (23, 145, 135)
# CIRCLE_COLOR = (239, 231, 200)
# CROSS_COLOR = (66, 66, 66)

# # ------
# # SCREEN
# # ------
# screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# pygame.display.set_caption( 'TIC TAC TOE' )
# screen.fill( BG_COLOR )

# # -------------
# # CONSOLE BOARD
# # -------------
# board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

# # ---------
# # FUNCTIONS
# # ---------
# def draw_lines():
#     # gap=WIDTH/3
#     # for i in range(BOARD_ROWS):
#     #     for j in range(BOARD_COLS):
#     #         pygame.draw.line(screen,LINE_COLOR,(0,i*gap),(WIDTH,i*gap),10)
#     #         pygame.draw.line(screen,LINE_COLOR,(j*gap,0),(j*gap,HEIGHT),10)
# 	# 1 horizontal
# 	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
# 	# 2 horizontal
# 	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

# 	# 1 vertical
# 	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
# 	# 2 vertical
# 	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

# def draw_figures():
# 	for row in range(BOARD_ROWS):
# 		for col in range(BOARD_COLS):
# 			if board[row][col] == 1:
# 				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
# 			elif board[row][col] == 2:
# 				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
# 				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

# def mark_square(row, col, player):
# 	board[row][col] = player

# def available_square(row, col):
# 	return board[row][col] == 0

# def is_board_full():
# 	for row in range(BOARD_ROWS):
# 		for col in range(BOARD_COLS):
# 			if board[row][col] == 0:
# 				return False

# 	return True

# def check_win(player):
# 	# vertical win check
# 	for col in range(BOARD_COLS):
# 		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
# 			draw_vertical_winning_line(col, player)
# 			return True

# 	# horizontal win check
# 	for row in range(BOARD_ROWS):
# 		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
# 			draw_horizontal_winning_line(row, player)
# 			return True

# 	# asc diagonal win check
# 	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
# 		draw_asc_diagonal(player)
# 		return True

# 	# desc diagonal win chek
# 	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
# 		draw_desc_diagonal(player)
# 		return True

# 	return False

# def draw_vertical_winning_line(col, player):
#     # global color
# 	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

# 	if player == 1:
# 		color = CIRCLE_COLOR
# 	elif player == 2:
# 		color = CROSS_COLOR

# 	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

# def draw_horizontal_winning_line(row, player):
# 	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

# 	if player == 1:
# 		color = CIRCLE_COLOR
# 	elif player == 2:
# 		color = CROSS_COLOR

# 	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

# def draw_asc_diagonal(player):
# 	if player == 1:
# 		color = CIRCLE_COLOR
# 	elif player == 2:
# 		color = CROSS_COLOR

# 	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

# def draw_desc_diagonal(player):
# 	if player == 1:
# 		color = CIRCLE_COLOR
# 	elif player == 2:
# 		color = CROSS_COLOR

# 	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

# def restart():
# 	screen.fill( BG_COLOR )
# 	draw_lines()
# 	for row in range(BOARD_ROWS):
# 		for col in range(BOARD_COLS):
# 			board[row][col] = 0

# draw_lines()

# # ---------
# # VARIABLES
# # ---------
# player = 1
# game_over = False

# # --------
# # MAINLOOP
# # --------
# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()

# 		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

# 			mouseX = event.pos[0] # x
# 			mouseY = event.pos[1] # y

# 			clicked_row = int(mouseY // SQUARE_SIZE)
# 			clicked_col = int(mouseX // SQUARE_SIZE)

# 			if available_square( clicked_row, clicked_col ):

# 				mark_square( clicked_row, clicked_col, player )
# 				if check_win( player ):
# 					game_over = True
# 				player = player % 2 + 1

# 				draw_figures()

# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_r:
# 				restart()
# 				player = 1
# 				game_over = False

# 	pygame.display.update()


































