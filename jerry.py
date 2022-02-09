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


