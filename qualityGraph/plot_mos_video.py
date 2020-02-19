#!/usr/bin/python

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
import sys

from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

plt.plot(x_vals, y_vals)

def animate(i):
	data = pd.read_csv(sys.argv[1])
	x = data['x_value']
	y1 = data['mos']

	plt.cla()	
	plt.plot(x,y1, label='MOS')

	plt.legend(loc='upper right')
	plt.tight_layout()
	
	os.system(window)

# add new value to MOS graph
ani = FuncAnimation(plt.gcf(),animate,interval=sys.argv[2])

window = "wmctrl -r Figure 1 -e 1,100,200,450,400"

plt.tight_layout()
plt.show()


