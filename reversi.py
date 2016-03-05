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
		#testing
		# self.gameboard[3][3] = WHITE
		# self.gameboard[3][4] = WHITE	
		# self.gameboard[3][5] = WHITE
		# self.gameboard[4][3] = BLACK
		# self.gameboard[4][4] = BLACK	
		# self.gameboard[4][5] = BLACK

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
			# print 'i = ', i
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
			for i in range(2,col):
				if(self.gameboard[row][col-i] == 0):
					break
				if(self.gameboard[row][col-i] == my_color):
					validity = True
					directions.append('west')
					# print 'left'
					break
		#Right
		if(col+2 <= self.boardsize-1 and self.gameboard[row][col+1] == opponent_color):
			for i in range(2, self.boardsize-1-col):
				if(self.gameboard[row][col+i] == 0):
					break
				if(self.gameboard[row][col+i] == my_color):
					validity = True
					directions.append('east')
					# print 'right'
					break
		#Up
		if(row-2 >= 0 and self.gameboard[row-1][col] == opponent_color):
			for i in range(2,row):
				if(self.gameboard[row-i][col] == 0):
					break
				if(self.gameboard[row-i][col] == my_color):
					validity = True
					directions.append('north')
					# print 'up'
					break
		#Down
		if(row+2 <= self.boardsize-1 and self.gameboard[row+1][col] == opponent_color):

			for i in range(2, self.boardsize-1 - row):
				if(self.gameboard[row+i][col] == 0):
					break
				if(self.gameboard[row+i][col] == my_color):
					validity = True
					directions.append('south')
					# print 'down'
					break
		#Diagonally up to the left
		if(row-2 >= 0 and col-2 >= 0 and self.gameboard[row-1][col-1] == opponent_color):
			for i in range(2, min(row,col)):
				if(self.gameboard[row-i][col-i] == 0):
					break
				if(self.gameboard[row-i][col-i] == my_color):
					validity = True
					directions.append('northwest')
					# print 'diag up left'
					break
		#Diagonally up to the right
		if(row-2 >= 0 and col+2 <= self.boardsize-1 and self.gameboard[row-1][col+1] == opponent_color):
			for i in range(2,min(row,self.boardsize-1-col)):
				if(self.gameboard[row-i][col+i] == 0):
					break
				if(self.gameboard[row-i][col+i] == my_color):
					validity = True
					directions.append('northeast')
					# print 'diag up right'
					break
		#Diagonally down to the left
		if(row+2 <= self.boardsize-1 and col-2 >= 0 and self.gameboard[row+1][col-1] == opponent_color):
			for i in range(2,min(col, self.boardsize-1-row)):
				if(self.gameboard[row+i][col-i] == 0):
					break
				if(self.gameboard[row+i][col-i] == my_color):
					validity = True
					directions.append('southwest')
					# print 'diag down left'
					break
		#Diagonally down to the right
		if(row+2 <= self.boardsize-1 and col+2 <= self.boardsize-1 and self.gameboard[row+1][col+1] == opponent_color):
			for i in range(2,min(self.boardsize-1-row, self.boardsize-1-col)):
				if(self.gameboard[row+i][col+i] == 0):
					break
				if(self.gameboard[row+i][col+i] == my_color):
					validity = True
					directions.append('southeast')
					# print 'diag down right'
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
			# self.board[row][col] = color
			self.executeMove(row, col, color, directions)
			self.last_move = [row, col]

		else:
			sys.stdout.write('ERROR: Move not valid\n\n')

	def printScore(self):
		score_white = 0
		score_black = 0
		for row in range(0,self.boardsize-1):
			for col in range(0, self.boardsize-1):
				if(self.gameboard[row][col] == 1):
					score_black += 1
				if(self.gameboard[row][col] == 2):
					score_white += 1

		sys.stdout.write('Score light: %2d'   % score_white)
		sys.stdout.write('        Score dark: %2d \n' % score_black)

	def getScore(self, color):
		score = 0
		for row in range(0,self.boardsize-1):
			for col in range(0, self.boardsize-1):
				if(self.gameboard[row][col] == color):
					score += 1
		return score

	def getValidMoves(self, color):
		valid_moves = []
		for row in range(0,self.boardsize-1):
			for col in range(0,self.boardsize-1):
				valid, directions = self.moveValid(col, row, color)
				if(valid == True):
					temp_board = copy.deepcopy(self)
					temp_board.executeMove(row, col, color, directions)
					valid_moves.append(temp_board)

		return valid_moves



	# This function may be redundant
	def checkIfValidMoves(self,color):
		any_valid = False
		for row in range(0,self.boardsize-1):
			for col in range(0,self.boardsize-1):
				valid, _ = moveValid(col,row,color)
				if(valid == True):
					any_valid = True
					break
		return any_valid


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

	# def minimax(board, depth, maximizer):

	def makeMoveAI(self):
		maximizer = True
		





def newGame(boardsize):
	color_human = WHITE
	color_ai = BLACK
	depth = 3
	board = Board(boardsize)
	ai = Ai(board, color_ai, depth)
	board.printBoard()

	valid_moves = board.getValidMoves(color_human)

	for valid_board in valid_moves:
		valid_board.printBoard()



	# while(1):
	# 	#Player make move
	# 	move_human = raw_input('Make a move: ')
	# 	move= list(move_human)
	# 	col = ord(move[0]) - ord('a')
	# 	row = ord(move[1]) - ord('1')
	# 	board.makeMove(col,row,color_human)
	# 	board.printBoard()
	# 	board.printScore()

	# 	#AI make move
	# 	move_ai = ai.makeMoveAI()
	# 	move = list(move_ai)
	# 	col = ord(move[0]) - ord('a')
	# 	row = ord(move[1]) - ord('1')
	# 	print 'AI moves ', move_ai 
	# 	board.makeMove(col,row,color_ai)
	# 	board.printBoard()
	# 	board.printScore()
	# 	print ''







def main():
	boardsize = 8
	newGame(boardsize)


main()



