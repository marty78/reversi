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
		self.board[int(boardsize/2) - 1][int(boardsize/2) - 1] = WHITE
		self.board[int(boardsize/2)][int(boardsize/2)] = WHITE
		self.board[int(boardsize/2)][int(boardsize/2) - 1] = BLACK
		self.board[int(boardsize/2) - 1][int(boardsize/2)] = BLACK

	def printboard(self):
		sys.stdout.write("  ")
		i = 0
		for c in string.ascii_lowercase:
			i += 1
			if i > self.boardsize:
				break
			sys.stdout.write("   %s" % c)
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

	def makeMove(self, col, row, color):
		self.board[row][col] = color



def main():
	board = Board(4)
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



