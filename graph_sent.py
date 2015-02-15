import sys
import csv
import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib
import time
import pylab
from datetime import datetime

def main():
	csvfile = open("sentiments.csv", 'rb')
	dat = csv.reader(csvfile, delimiter=',')
	values = []
	date_list = []
	for row in enumerate(dat):
		values.append(float(row[1][0]))
		date_list.append(datetime.fromtimestamp(int(row[1][1])/1000))
	values = np.array(values)
	dates = matplotlib.dates.date2num(date_list)
	plt.plot_date(dates, values, fmt = "o")
	plt.show()
	return
	
main()