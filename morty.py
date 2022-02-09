import pickle
import jerry

if __name__=="__main__":
	with open("c-137.txt", "rb") as file:
		z = pickle.load(file)
		print(type(z))
		print(type(z.x))
		print(type(z.y))
