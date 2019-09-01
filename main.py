import argparse
from grid import *

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=int, help="Size of field", required=True)
parser.add_argument("-p", nargs=4, help="Probabilities of all creatures", default=['0.25', '0.25', '0.25', '0.25'])
parser.add_argument("-ss", type=int, help="Random Seed", default=179)
args = parser.parse_args()._get_kwargs()

for i in args:
	print(i)

seed = args[2][1]
size = args[1][1]
probabilities = list(map(float, args[0][1]))

if(abs(sum(probabilities) - 1) > 1e-9):
	print("sum of probabilities should be 1")
	exit(0)
else:
	f = field(size, probabilities, seed)
	f.startWork()
