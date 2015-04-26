from next_level import next_level
from urllib import request
import pickle


with open("banner.p", 'rb') as file:
	f = pickle.load(file)


for line in f:
	print("".join([item[0]*item[1] for item in line]))
	
#Answer is Channel