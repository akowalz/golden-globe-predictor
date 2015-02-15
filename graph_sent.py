import sys
import csv
import numpy as np
import copy
import matplotlib.pyplot as plt


def main():
	csvfile = open("sentiments.csv", 'rb')
	dat = csv.reader(csvfile, delimiter=',')
	column1 = []
	column2 = []
	for row in enumerate(dat):
		column1.append(float(row[1][0]))
		column2.append(int(row[1][1]))
		print int(row[1][1])/1000
		print time.strftime("%c", time.localtime(int(row[1][1])/1000))
	column1 = np.array(column1)
	column2 = np.array(column2)
	plt.plot(column1)
	plt.show()
	return
	
main()