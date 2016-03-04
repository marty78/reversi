import sys
import string

DARK = 1
LIGHT = 2


class Board:
	boardsize = None
	gameboard = None
	DARK = 1
	LIGHT = 2

	def __init__(self, boardsize):
		self.boardsize = boardsize
		self.gameboard = self.board = [[0 for x in range(0, boardsize)] for x in range(0, boardsize)] #Maa endre denne pga kopi?
		for i in range(0,boardsize):
		self.board[int(boardsize/2) - 1][int(boardsize/2) - 1] = LIGHT
		self.board[int(boardsize/2)][int(boardsize/2)] = LIGHT
		self.board[int(boardsize/2)][int(boardsize/2) - 1] = DARK
		self.board[int(boardsize/2) - 1][int(boardsize/2)] = DARK

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
				if self.gameboard[i][j] == LIGHT:
					sys.stdout.write(" L |")
				elif self.gameboard[i][j] == DARK:
					sys.stdout.write(" D |")
				else:
					sys.stdout.write("   |")
			sys.stdout.write("\n   +")
			for k in range(0, self.boardsize):
				sys.stdout.write("---+")
			sys.stdout.write("\n")


def main():
	board = Board(4)
	board.printboard()

main()



