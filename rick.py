import pickle

class X:
	def __init__(self, xx):
		self.x = xx

class Y:
	def __init__(self):
		self.s = ""

class Z:
	def __init__(self):
		self.x = X(5)
		self.y = Y()

if __name__=="__main__":
	z = Z()
	with open("c-137.txt", "wb") as file:
		pickle.dump(z, file)
