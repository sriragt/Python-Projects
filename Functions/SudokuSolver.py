puzzle = [
[8, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 6, 0, 0, 0, 0, 0],
[0, 7, 0, 0, 9, 0, 2, 0, 0],
[0, 5, 0, 0, 0, 7, 0, 0, 0],
[0, 0, 0, 0, 4, 5, 7, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 3, 0],
[0, 0, 1, 0, 0, 0, 0, 6, 8],
[0, 0, 8, 5, 0, 0, 0, 1, 0],
[0, 9, 0, 0, 0, 0, 4, 0, 0],
]

'''
cleancopy = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
]
'''

def checknum(x, y, n):
	for i in range(9):
		if puzzle[x][i] == n or puzzle[i][y] == n:
			return False
	boxx = (x // 3) * 3
	boxy = (y // 3) * 3
	for i in range(3):
		for j in range(3):
			if puzzle[boxx + i][boxy + j] == n:
				return False
	return True

def solution():
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] == 0:
				for n in range(1, 10):
					if checknum(i, j, n):
						puzzle[i][j] = n
						solve()
						puzzle[i][j] = 0
				return
	print('\n'.join([str(i) for i in puzzle]))
	input('More solutions?')

solution()
