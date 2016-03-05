import sys
import string

BLACK = 1
WHITE = 2


class Board:
	boardsize = None
	gameboard = None
	BLACK = 1
	WHITE = 2

	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.gameboard = self.board = [[0 for x in range(0, boardsize)] for x in range(0, boardsize)] #Maa endre denne pga kopi?
		self.gameboard[int(boardsize/2) - 1][int(boardsize/2) - 1] = WHITE
		self.gameboard[int(boardsize/2)][int(boardsize/2)] = WHITE
		self.gameboard[int(boardsize/2)][int(boardsize/2) - 1] = BLACK
		self.gameboard[int(boardsize/2) - 1][int(boardsize/2)] = BLACK
		#testing
		# self.gameboard[3][3] = BLACK
		self.gameboard[4][5] = WHITE	
		# self.gameboard[5][2] = WHITE


	def printboard(self):
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

		direction = None
		validity = False

		#Check if the square is valid and empty
		if(col < 0 or col > self.boardsize - 1 or row < 0 or row > self.boardsize - 1):
			return False
		if(self.board[row][col] != 0):
			return False

		#Now check in all directions:
		#Left
		if(col-2 >= 0 and self.gameboard[row][col-1] == opponent_color):
			for i in range(2,col):
				if(self.gameboard[row][col-i] == 0):
					break
				if(self.gameboard[row][col-i] == my_color):
					validity = True
					direction = 'west'
					# print 'left'
					break
		#Right
		if(col+2 <= self.boardsize-1 and self.gameboard[row][col+1] == opponent_color):
			for i in range(2, self.boardsize-1-col):
				if(self.gameboard[row][col+i] == 0):
					break
				if(self.gameboard[row][col+i] == my_color):
					validity = True
					direction = 'east'
					# print 'right'
					break
		#Up
		if(row-2 >= 0 and self.gameboard[row-1][col] == opponent_color):
			for i in range(2,row):
				if(self.gameboard[row-i][col] == 0):
					break
				if(self.gameboard[row-i][col] == my_color):
					validity = True
					direction = 'north'
					# print 'up'
					break
		#Down
		if(row+2 <= self.boardsize-1 and self.gameboard[row+1][col] == opponent_color):

			for i in range(2, self.boardsize-1 - row):
				if(self.gameboard[row+i][col] == 0):
					break
				if(self.gameboard[row+i][col] == my_color):
					validity = True
					direction = 'south'
					# print 'down'
					break
		#Diagonally up to the left
		if(row-2 >= 0 and col-2 >= 0 and self.gameboard[row-1][col-1] == opponent_color):
			for i in range(2, min(row,col)):
				if(self.gameboard[row-i][col-i] == 0):
					break
				if(self.gameboard[row-i][col-i] == my_color):
					validity = True
					direction = 'northwest'
					# print 'diag up left'
					break
		#Diagonally up to the right
		if(row-2 >= 0 and col+2 <= self.boardsize-1 and self.gameboard[row-1][col+1] == opponent_color):
			for i in range(2,min(row,self.boardsize-1-col)):
				if(self.gameboard[row-i][col+i] == 0):
					break
				if(self.gameboard[row-i][col+i] == my_color):
					validity = True
					direction = 'northeast'
					# print 'diag up right'
					break
		#Diagonally down to the left
		if(row+2 <= self.boardsize-1 and col-2 >= 0 and self.gameboard[row+1][col-1] == opponent_color):
			for i in range(2,min(col, self.boardsize-1-row)):
				if(self.gameboard[row+i][col-i] == 0):
					break
				if(self.gameboard[row+i][col-i] == my_color):
					validity = True
					direction = 'southwest'
					# print 'diag down left'
					break
		#Diagonally down to the right
		if(row+2 <= self.boardsize-1 and col+2 <= self.boardsize-1 and self.gameboard[row+1][col+1] == opponent_color):
			for i in range(2,min(self.boardsize-1-row, self.boardsize-1-col)):
				if(self.gameboard[row+i][col+i] == 0):
					break
				if(self.gameboard[row+i][col+i] == my_color):
					validity = True
					direction = 'southeast'
					# print 'diag down right'
					break

		return validity, direction


	def executeMove(self, row, col, color, direction):
		if(direction == 'east'):
			for i in range(0,self.boardsize-1-col):
				if(self.gameboard[row][col+i] == color):
					break
				else:
					self.gameboard[row][col+i] = color
		if(direction == 'west'):
			for i in range(0,col):
				if(self.gameboard[row][col-i] == color):
					break
				else:
					self.gameboard[row][col-i] = color
		if(direction == 'north'):
			for i in range(0,row):
				if(self.gameboard[row-i][col] == color):
					break
				else:
					self.gameboard[row-i][col] = color
		if(direction == 'south'):
			for i in range(0, self.boardsize-1 - row):
				if(self.gameboard[row+i][col] == color):
					break
				else:
					self.gameboard[row+i][col] = color
		if(direction == 'northwest'):
			for i in range(0, min(row,col)):
				if(self.gameboard[row-i][col-i] == color):
					break
				else:
					self.gameboard[row-i][col-i] = color
		if(direction == 'northeast'):
			for i in range(0,min(row,self.boardsize-1-col)):
				if(self.gameboard[row-i][col+i] == color):
					break
				else:
					self.gameboard[row-i][col+i] = color
		if(direction == 'southwest'):
			for i in range(0,min(col, self.boardsize-1-row)):
				if(self.gameboard[row+i][col-i] == color):
					break
				else:
					self.gameboard[row+i][col-i] = color
		if(direction == 'southeast'):
			for i in range(0,min(self.boardsize-1-row, self.boardsize-1-col)):
				if(self.gameboard[row+i][col+i] == color):
					break
				else:
					self.gameboard[row+i][col+i] = color



	def makeMove(self, col, row, color):
		valid, direction = self.moveValid(col, row, color)
		if(valid == True):
			# self.board[row][col] = color
			self.executeMove(row, col, color, direction)

		else:
			sys.stdout.write('ERROR: Move not valid\n')



def main():
	board = Board(8)
	board.printboard()
	while(1):
		move = raw_input('Make a move: ')
		move = list(move)
		col = ord(move[0]) - ord('a')
		row = ord(move[1]) - ord('1')
		color = WHITE
		board.makeMove(col,row,color)
		board.printboard()


main()



