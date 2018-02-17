"""Does a math"""
import csv

inputfile = "AST121.csv"

with open(inputfile) as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ",")
	course = ""
	work = []
	scales = []

	for row in readCSV:
		if len(row) == 0:
			print("empty row")
		elif len(row) == 1:
			course = row[0]
		else:
			work.append(row[0])
			scales.append(row[1])

	print(course)
	print(work)
	print(scales)

	grade = []

	total_got = 0
	total_mark = 0

	c = 0

	print("For something you dont know yet just press enter")
	while c < len(work):
		while True: 
			g = input("What did you get for " + work[c] + "? ")
			if g.isdigit():
				grade.append(g)
				total_got += int(g)
				total_mark += int(scales[c])
				break 
			if g == "":
				grade.append(g)
				break
		c += 1

	lol = total_got/total_mark * 100

	print(grade)
	print("Your current percentage is " + str(lol))

	# Add more writing fuunction

