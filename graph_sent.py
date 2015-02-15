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
	column1 = []
	date_list = []
	for row in enumerate(dat):
		column1.append(float(row[1][0]))
		date_list.append(datetime.fromtimestamp(int(row[1][1])/1000))
	column1 = np.array(column1)
	dates = matplotlib.dates.date2num(date_list)
	plt.plot_date(dates, column1, fmt = "o")
	plt.show()
	#pylab.figure(1)
	#x = range(len(column2))
	#pylab.xticks(x, column2)
	#pylab.plot(x, column1, "g")
	#pylab.show()
	return

"""def main():
	csvfile = open("sentiments.csv", 'rb')
	dat = csv.reader(csvfile, delimiter=',')
	column1 = []
	column2 = []
	for row in enumerate(dat):
		column1.append(float(row[1][0]))
		print time.localtime(int(row[1][1])/1000)
		column2.append(time.localtime(int(row[1][1])/1000))
	column1 = np.array(column1)
	pylab.figure(1)
	x = range(len(column2))
	pylab.xticks(x, column2)
	pylab.plot(x, column1, "g")
	pylab.show()
	return"""
	
main()