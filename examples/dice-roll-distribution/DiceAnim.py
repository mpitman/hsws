#!/usr/bin/python
import sys
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation

count = []

def animate(i):
	d1 = np.random.randint(1,7)
	d2 = np.random.randint(1,7)
	num = d1+d2
	count.append(num)
	plt.clf()
	plt.xticks(np.arange(2,14) + 0.5, ('2', '3', '4', '5','6','7','8','9','10','11','12'))
	plt.xlabel("Roll")
	plt.ylabel("Count")
	title = str(i) + " Rolls"
	plt.title(title)

	#
	# Plot actual accumulations
	#
	n,bins,patches = plt.hist(count,bins=np.arange(2,14),color='Blue')
	x = bins + 0.5


	if (i > 100):
		#
		# Plot theoretical bins
		#
		idealy = np.empty(12)
		idealy[0] = i/36
		idealy[1] = 2*i/36
		idealy[2] = 3*i/36
		idealy[3] = 4*i/36
		idealy[4] = 5*i/36
		idealy[5] = 6*i/36
		idealy[6] = 5*i/36
		idealy[7] = 4*i/36
		idealy[8] = 3*i/36
		idealy[9] = 2*i/36
		idealy[10] = i/36
		idealy[11] = None
		plt.plot([x-0.46,x+0.46],[idealy,idealy],color='Red',linewidth=3,alpha=0.5)
	
	if (i>200):
		#
		# Plot Poisson error bars
		#
		for i in np.arange(0,11):
			plt.errorbar(x[i],n[i],yerr=np.sqrt(n[i]),color='Black',linewidth=2)
	
	return patches,
	

fig,ax = plt.subplots()
count = []	
#ani = animation.FuncAnimation(fig, animate, init_func=None, interval=10, blit=False)
ani = animation.FuncAnimation(fig, animate, init_func=None, blit=False)
plt.show()
