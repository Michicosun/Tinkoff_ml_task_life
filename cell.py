class Cell:
	def __init__(self, probabilities, prob):
		summ = 0
		for i in range(0, 4):
			if prob >= summ and prob <= summ + probabilities[i]:
				self.mod = i
			summ += probabilities[i]

	def getAttr(self):
		if self.mod == 0:
			return [' ', 'grey']
		elif self.mod == 1:
			return ['R', 'yellow']
		elif self.mod == 2:
			return ['F', 'blue']
		elif self.mod == 3:
			return ['S', 'cyan']