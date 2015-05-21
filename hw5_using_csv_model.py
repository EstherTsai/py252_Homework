# -*- coding: utf-8 -*-
import csv

new = []
with open('stores_old.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		new.append([row['sid'], row['name'], row['tel'], row['wifi']])
	print (new)

with open('stores_new.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['id', 'name', 'tel', 'wifi'])
	for new_row in new:
		spamwriter.writerow(new_row)
	
