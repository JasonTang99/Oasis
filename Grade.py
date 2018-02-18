"""Does a math"""
import csv
from fractions import Fraction

AST = "AST121.csv"

course = ""
work = []
scales = []
grade = []

def readfile(inputfile):
	with open(inputfile) as csvfile:
		readCSV = csv.reader(csvfile, delimiter = ",")

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

def getsomeinput():
	total_got = 0
	total_mark = 0

	c = 0
	
	print("")
	print("Enter the values as decimals or fractions")
	print("")
	print("For something you dont know yet just press enter")
	print("")

	while c < len(work):
		while True: 
			g = input("What did you get for " + work[c] + "? ")
			if g.replace(".", "", 1).replace("/", "", 1).isdigit():
				grade.append(g)
				total_got += ( float(sum(Fraction(s) for s in g.split())) * int(scales[c]) ) / 100
				total_mark += int(scales[c])
				break 
			if g == "":
				grade.append(g)
				break
		c += 1

	lol = total_got/total_mark * 100 * 100

	print(grade)
	print("Your current percentage is " + str(lol))


if __name__ == "__main__":
	readfile(AST)
	getsomeinput()
