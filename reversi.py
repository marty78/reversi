import sys
import string
import copy 

BLACK = 1
WHITE = 2

class Board:
	BLACK = 1
	WHITE = 2
	boardsize = None
	gameboard = None
	last_move = None

	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.gameboard = self.board = [[0 for x in range(0, boardsize)] for x in range(0, boardsize)] #Maa endre denne pga kopi?
		self.gameboard[int(boardsize/2) - 1][int(boardsize/2) - 1] = WHITE
		self.gameboard[int(boardsize/2)][int(boardsize/2)] = WHITE
		self.gameboard[int(boardsize/2)][int(boardsize/2) - 1] = BLACK
		self.gameboard[int(boardsize/2) - 1][int(boardsize/2)] = BLACK

	def printBoard(self):
		sys.stdout.write("  ")
		i = 0
		for c in string.ascii_lowercase:
			i += 1
			if i > self.boardsize:
				break
			sys.stdout.write('   %s' % c)
		sys.stdout.write("\n   +")
		for i in range(0, self.boardsize):
			sys.stdout.write("---+")
		sys.stdout.write("\n")

		for i in range(0, self.boardsize):
			sys.stdout.write("%2d |" % (i + 1))
			for j in range(0, self.boardsize):
				if self.gameboard[i][j] == WHITE:
					sys.stdout.write(" L |")
				elif self.gameboard[i][j] == BLACK:
					sys.stdout.write(" D |")
				else:
					sys.stdout.write("   |")
			sys.stdout.write("\n   +")
			for k in range(0, self.boardsize):
				sys.stdout.write("---+")
			sys.stdout.write("\n")

	def moveValid(self, col, row, color):
		if(color == BLACK):
			my_color = BLACK
			opponent_color = WHITE
		else:
			my_color = WHITE
			opponent_color = BLACK

		directions = []
		validity = False

		#Check if the square is valid and empty
		if(col < 0 or col > self.boardsize - 1 or row < 0 or row > self.boardsize - 1):
			return False, directions
		if(self.board[row][col] != 0):
			return False, directions

		#Now check in all directions:
		#Left
		if(col-2 >= 0 and self.gameboard[row][col-1] == opponent_color):
			for i in range(2,col+1):
				if(self.gameboard[row][col-i] == 0):
					break
				if(self.gameboard[row][col-i] == my_color):
					validity = True
					directions.append('west')
					break
		#Right
		if(col+2 <= self.boardsize-1 and self.gameboard[row][col+1] == opponent_color):
			for i in range(2, self.boardsize-col):
				if(self.gameboard[row][col+i] == 0):
					break
				if(self.gameboard[row][col+i] == my_color):
					validity = True
					directions.append('east')
					break
		#Up
		if(row-2 >= 0 and self.gameboard[row-1][col] == opponent_color):
			for i in range(2,row+1):
				if(self.gameboard[row-i][col] == 0):
					break
				if(self.gameboard[row-i][col] == my_color):
					validity = True
					directions.append('north')
					break
		#Down
		if(row+2 <= self.boardsize-1 and self.gameboard[row+1][col] == opponent_color):
			for i in range(2, self.boardsize - row):
				if(self.gameboard[row+i][col] == 0):
					break
				if(self.gameboard[row+i][col] == my_color):
					validity = True
					directions.append('south')
					break
		#Diagonally up to the left
		if(row-2 >= 0 and col-2 >= 0 and self.gameboard[row-1][col-1] == opponent_color):
			for i in range(2, min(row+1,col+1)):
				if(self.gameboard[row-i][col-i] == 0):
					break
				if(self.gameboard[row-i][col-i] == my_color):
					validity = True
					directions.append('northwest')
					break
		#Diagonally up to the right
		if(row-2 >= 0 and col+2 <= self.boardsize-1 and self.gameboard[row-1][col+1] == opponent_color):
			for i in range(2,min(row+1,self.boardsize-col)):
				if(self.gameboard[row-i][col+i] == 0):
					break
				if(self.gameboard[row-i][col+i] == my_color):
					validity = True
					directions.append('northeast')
					break
		#Diagonally down to the left
		if(row+2 <= self.boardsize-1 and col-2 >= 0 and self.gameboard[row+1][col-1] == opponent_color):
			for i in range(2,min(col+1, self.boardsize-row)):
				if(self.gameboard[row+i][col-i] == 0):
					break
				if(self.gameboard[row+i][col-i] == my_color):
					validity = True
					directions.append('southwest')
					break
		#Diagonally down to the right
		if(row+2 <= self.boardsize-1 and col+2 <= self.boardsize-1 and self.gameboard[row+1][col+1] == opponent_color):
			for i in range(2,min(self.boardsize-row, self.boardsize-col)):
				if(self.gameboard[row+i][col+i] == 0):
					break
				if(self.gameboard[row+i][col+i] == my_color):
					validity = True
					directions.append('southeast')
					break

		return validity, directions

	def executeMove(self, row, col, color, directions):
		for direction in directions:
			if(direction == 'east'):
				for i in range(1,self.boardsize-1-col):
					if(self.gameboard[row][col+i] == color):
						break
					else:
						self.gameboard[row][col+i] = color
			if(direction == 'west'):
				for i in range(1,col):
					if(self.gameboard[row][col-i] == color):
						break
					else:
						self.gameboard[row][col-i] = color
			if(direction == 'north'):
				for i in range(1,row):
					if(self.gameboard[row-i][col] == color):
						break
					else:
						self.gameboard[row-i][col] = color
			if(direction == 'south'):
				for i in range(1, self.boardsize-1 - row):
					if(self.gameboard[row+i][col] == color):
						break
					else:
						self.gameboard[row+i][col] = color
			if(direction == 'northwest'):
				for i in range(1, min(row,col)):
					if(self.gameboard[row-i][col-i] == color):
						break
					else:
						self.gameboard[row-i][col-i] = color
			if(direction == 'northeast'):
				for i in range(1,min(row,self.boardsize-1-col)):
					if(self.gameboard[row-i][col+i] == color):
						break
					else:
						self.gameboard[row-i][col+i] = color
			if(direction == 'southwest'):
				for i in range(1,min(col, self.boardsize-1-row)):
					if(self.gameboard[row+i][col-i] == color):
						break
					else:
						self.gameboard[row+i][col-i] = color
			if(direction == 'southeast'):
				for i in range(1,min(self.boardsize-1-row, self.boardsize-1-col)):
					if(self.gameboard[row+i][col+i] == color):
						break
					else:
						self.gameboard[row+i][col+i] = color

			self.gameboard[row][col] = color

	def makeMove(self, col, row, color):

		valid, directions = self.moveValid(col, row, color)
		if(valid == True):
			self.executeMove(row, col, color, directions)
			self.last_move = [row, col]

		else:
			sys.stdout.write('ERROR: Move not valid\n\n')
		return valid

	def printScore(self):
		score_white = self.getScore(WHITE)
		score_black = self.getScore(BLACK)
		sys.stdout.write('Score light: %2d'   % score_white)
		sys.stdout.write('        Score dark: %2d \n' % score_black)

	def getScore(self, color):
		score = 0
		for row in range(0,self.boardsize):
			for col in range(0, self.boardsize):
				if(self.gameboard[row][col] == color):
					score += 1
		return score

	def getValidMoves(self, color):
		valid_moves = []
		for row in range(0,self.boardsize):
			for col in range(0,self.boardsize):
				valid, directions = self.moveValid(col, row, color)
				if(valid == True):
					temp_board = copy.deepcopy(self)
					temp_board.makeMove(col, row, color)
					valid_moves.append(temp_board)

		return valid_moves

	def checkIfAnyValidMoves(self,color):
		any_valid = False
		for row in range(0,self.boardsize):
			for col in range(0,self.boardsize):
				valid, _ = self.moveValid(col,row,color)
				if(valid == True):
					any_valid = True
					break
		return any_valid

	def gameOver(self):
		game_over = False
		if(self.checkIfAnyValidMoves(BLACK) == False and self.checkIfAnyValidMoves(WHITE) == False):
			game_over = True
		return game_over


class Ai:
	depth = None
	my_color = None
	opponent_color = None
	root_board = None

	def __init__(self, board, color, depth):
		self.my_color = color
		if(self.my_color == BLACK):
			self.opponent_color = WHITE
		else:
			self.opponent_color = BLACK
		self.depth = depth
		self.root_board = board

	def updateRootBoard(self, board):
		self.root_board = board

	def minimax(self, board, depth, maximizer):
		if(depth == 0):
			return board.getScore(self.my_color)

		if(maximizer == True):
			if(board.checkIfAnyValidMoves(self.my_color) == False):	#Check if terminal node
				return board.getScore(self.my_color)
			best_score = -999999
			valid_moves = board.getValidMoves(self.my_color)
			for move in valid_moves:
				score = self.minimax(move, depth-1, False)
				best_score = max(best_score, score)
			return best_score

		else: #minimizer
			if(board.checkIfAnyValidMoves(self.opponent_color) == False):	#Check if terminal node
				return board.getScore(self.opponent_color)
			best_score = 999999
			valid_moves = board.getValidMoves(self.opponent_color)
			for move in valid_moves:
				score = self.minimax(move, depth-1, True)
				best_score = min(best_score, score)
			return best_score

	def makeMoveAI(self):
		maximizer = False
		valid_moves = self.root_board.getValidMoves(self.my_color)
		best_score = 0
		best_move = None
		for move in valid_moves:
			score = self.minimax(move, self.depth, maximizer)
			if(score > best_score):
				best_score = score
				best_move = move

		return best_move.last_move
		

def aiVSai(boardsize):
	depth = 2
	board = Board(boardsize)
	ai1 = Ai(board,WHITE, depth)
	ai2 = Ai(board,BLACK, depth)

	while(True):
		#AI1 make move
		if(board.checkIfAnyValidMoves(WHITE) == True):
			move_ai = ai1.makeMoveAI()
			row_int = move_ai[0]
			col_int = move_ai[1]
			board.makeMove(col_int,row_int,WHITE)
			row = str(row_int + 1)
			col = str(unichr(col_int + 97))
			move = col + row
			board.printBoard()
			board.printScore()
			print 'LIGHT ', move
			board.printScore()
			if(board.gameOver() == True):
				break

		#AI2 make move
		if(board.checkIfAnyValidMoves(BLACK) == True):
			move_ai = ai2.makeMoveAI()
			row_int = move_ai[0]
			col_int = move_ai[1]
			board.makeMove(col_int,row_int,BLACK)
			row = str(row_int + 1)
			col = str(unichr(col_int + 97))
			move = col + row
			board.printBoard()
			board.printScore()
			print 'DARK ', move
			if(board.gameOver() == True):
				break

	if(board.getScore(WHITE) > board.getScore(BLACK)):
		winner = 'WHITE'
	else:
		winner = 'BLACK'

	print 'Game over! The winner is:', winner

def newGame(boardsize, color_human):
	if(color_human == BLACK):
		color_ai = WHITE
	else:
		color_ai = BLACK

	depth = 2
	board = Board(boardsize)
	ai = Ai(board, color_ai, depth)
	board.printBoard()

	if(color_human == BLACK): #Human plays first
		while(True):
			#Player make move
			if(board.checkIfAnyValidMoves(color_human) == True):
				while(True):
					move_human = raw_input('<move> ')
					move = list(move_human)
					move[1:len(move)] = [''.join(move[1:len(move)])]
					col = ord(move[0]) - ord('a')
					row = int(move[1]) - 1
					valid = board.makeMove(col,row,color_human)
					if(valid == True):
						board.printBoard()
						board.printScore()
						print 'Move played: ' + move_human
						sys.stdout.flush()
						break
				if(board.gameOver() == True):
					break

			#AI make move
			if(board.checkIfAnyValidMoves(color_ai) == True):
				move_ai = ai.makeMoveAI()
				row_int = move_ai[0]
				col_int = move_ai[1]
				board.makeMove(col_int,row_int,color_ai)
				row = str(row_int + 1)
				col = str(unichr(col_int + 97))
				move = col + row
				board.printBoard()
				board.printScore()
				print 'Move played: ' + move
				sys.stdout.flush()
				if(board.gameOver() == True):
					break

	else:	#AI plays first
		while(True):
			#AI make move
			if(board.checkIfAnyValidMoves(color_ai) == True):
				move_ai = ai.makeMoveAI()
				row_int = move_ai[0]
				col_int = move_ai[1]
				board.makeMove(col_int,row_int,color_ai)
				row = str(row_int + 1)
				col = str(unichr(col_int + 97))
				move = col + row
				board.printBoard()
				board.printScore()
				print 'Move played: ' + move
				sys.stdout.flush()
				if(board.gameOver() == True):
					break

			#Player make move
			if(board.checkIfAnyValidMoves(color_human) == True):
				while(True):
					move_human = raw_input('<move> ')
					move = list(move_human)
					move[1:len(move)] = [''.join(move[1:len(move)])]
					col = ord(move[0]) - ord('a')
					row = int(move[1]) - 1
					valid = board.makeMove(col,row,color_human)
					if(valid == True):
						board.printBoard()
						board.printScore()
						print 'Move played: ' + move_human
						sys.stdout.flush()
						break
				if(board.gameOver() == True):
					break

	if(board.getScore(color_human) > board.getScore(color_ai)):
		winner = 'human'
	elif(board.getScore(color_human) == board.getScore(color_ai)):
		winner = 'It is actually a tie!'
	else:
		winner = 'AI'

	print 'Game over! The winner is:', winner


def main():
	boardsize = 0
	color_human = BLACK
	for i in range(0,len(sys.argv)):
		if(sys.argv[i] == '-n'):
			boardsize = int(sys.argv[i+1])
		if(sys.argv[i] == '-l'): #Human is going to play with light pieces
			color_human = WHITE

	if(boardsize == 0):
		boardsize = 8	#Custom board size if nothing else specified

	print 'Board size =', boardsize
	print 'Human color =', color_human

	newGame(boardsize, color_human)
	# aiVSai(boardsize)


main()



