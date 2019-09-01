from cell import *
import time
import random
from os import system
from termcolor import colored

class field(object):
	def __init__(self, size, probabilities, seed):
		super(field, self).__init__()
		self.ways = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
		self.size = size
		self.probabilities = probabilities
		self.seed = seed
		random.seed(self.seed)
		self.matr = [[Cell(probabilities, random.random()) for j in range(self.size)] for i in range(size)]

	def printField(self):
		for i in range(self.size):
			for j in range(self.size):
				attr = self.matr[i][j].getAttr()
				print(colored(attr[0], attr[1]), end = " ")
			print()

	def inField(self, i, j):
		return i >= 0 and i < self.size and j >= 0 and j < self.size

	def getConnected(self, mod, i, j):
		cnt = 0
		for w in self.ways:
			newI = i + w[0]
			newJ = j + w[1]
			if self.inField(newI, newJ) and self.matr[newI][newJ].mod == mod:
				cnt += 1
		return cnt

	def changeField(self):
		nextMatr = self.matr.copy()
		for i in range(self.size):
			for j in range(self.size):
				if(self.matr[i][j].mod == 0):
					cnt2 = self.getConnected(2, i, j)
					cnt3 = self.getConnected(3, i, j)
					if(cnt2 == 3):
						nextMatr[i][j].mod = 2
					elif(cnt3 == 3):
						nextMatr[i][j].mod = 3
				elif(self.matr[i][j].mod == 2):
					cnt2 = self.getConnected(2, i, j)
					if(cnt2 < 2 or cnt2 > 3):
						nextMatr[i][j].mod = 0
				elif(self.matr[i][j].mod == 3):
					cnt3 = self.getConnected(3, i, j)
					if(cnt3 < 2 or cnt3 > 3):
						nextMatr[i][j].mod = 0
		self.matr = nextMatr.copy()
		del nextMatr

	def startWork(self):
		while(True):
			self.printField()
			self.changeField()
			time.sleep(1)
			system("clear")






















