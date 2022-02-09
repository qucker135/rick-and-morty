import pickle
import jerry

if __name__=="__main__":
	z = jerry.Z()
	print(type(z))
	print(type(z.x))
	print(type(z.y))
	with open("c-137.txt", "wb") as file:
		pickle.dump(z, file)
