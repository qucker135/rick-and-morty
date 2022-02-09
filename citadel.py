class X:
    def __init__(self):
        self.x = 5

xx = X()
print(xx.x)
print(type(xx))

class X:
    def __init__(self):
        self.x = 3

print(xx.x) 
print(type(xx)) #old X type

yy = X()
print(yy.x) 
print(type(yy)) #new X type
