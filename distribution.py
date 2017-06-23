from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np
import math
from random import randint

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def Expected(N,distri):
	# calculate expected outcome when N people are in this game, with specific choice distribution
	expected = []
	for i in xrange(100):
		# expected.append(distri[i]*(1-distri[i])**(N-1)*(i+60))
		expected.append(distri[i]*(1-distri[i])**(N-1)*(i))
	return expected

def main(stat_path,randomness_ratio=0,num_of_player = 1000,):
	my_data = genfromtxt(stat_path, delimiter=',')

	# adding random choice to original stat
	ran_player = int(my_data.size*randomness_ratio)
	for i in xrange(ran_player):
		my_data = np.append(my_data, randint(1,100))

	plt.figure(1)
	fig = plt.gcf()
	fig.canvas.set_window_title("Hokkaido Test")
	# plot the normalized distribution
	plt.subplot(211)
	n, bins, patches = plt.hist(my_data,100,normed=1)
	plt.title('LiHKG Distribution (with randomness ratio %s)' % randomness_ratio)
	plt.xlabel("Value")
	plt.ylabel("Normalized Frequency")
	plt.grid(True)
	plt.xlim([1,100])

	expected = []
	best_choice = []

	for i in xrange(num_of_player):
		expected.append(Expected(i+1,n))
		best_choice.append(np.argmax(expected[i])+1)
		# print i+1,best_choice[i]

	plt.subplot(212)
	x = np.arange(0, num_of_player, 1)
	plt.plot(x, best_choice, 'bo')
	plt.grid(True)
	plt.title('Best choice against number of player')
	plt.xlabel("Number of player")
	plt.ylabel("Best choice")
	plt.grid(True)
	plt.xlim([1,num_of_player])
	plt.ylim([1,100])
	plt.show()

if __name__ == "__main__":
	stat_path = './result.txt'
	randomness_ratio = 1
	num_of_player = 1000

	main(stat_path,randomness_ratio,num_of_player)