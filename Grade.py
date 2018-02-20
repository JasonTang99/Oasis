"""Does a math"""
import csv
from fractions import Fraction
# from typing import List

class Reader:
	filename = ""
	course = ""
	work = []
	scales = []
	grade = []

	def __init__(self, filename: str):
		self.filename = filename

	def readfile(self):
		with open(self.filename) as csvfile:
			readCSV = csv.reader(csvfile, delimiter = ",")
			b = 0

			for row in readCSV:
				if b == 0 and row != "":
					self.course = row
				elif b == 1 and row != "":
					self.work = row
				elif b == 2 and row != "":
					self.scales = row
				elif b == 3 and row != "":
					self.grade = row
				b += 1

		print(self.course)
		print(self.work)
		print(self.scales)
		print(self.grade)

	def getsomeinput(self):
		total_got = 0
		total_mark = 0
		c = 0
		
		print("")
		print("Enter the values as decimals")
		print("")
		print("For something you dont know yet just press enter")
		print("")

		while c < len(self.work):
			while True:
				g = input("What did you get for " + self.work[c] + "? ")
				if g.replace(".", "", 1).replace("/", "", 1).isdigit():
					g = float(sum(Fraction(s) for s in g.split()))
					self.grade.append(g)
					total_got += ( g * float(self.scales[c]) ) / 100
					total_mark += float(self.scales[c])
					break
				if g == "":
					self.grade.append(g)
					break
			c += 1

		lol = total_got/total_mark * 100

		print(self.grade)
		print("Your current percentage is " + str(lol))

	def calcGrade(self):
		a = 0
		total1 = 0.0
		total2 = 0.0

		while a < len(self.grade):
			if self.grade[a] != '':
				total1 += float(self.grade[a]) * float(self.scales[a])
				total2 += float(self.scales[a])
			a += 1

		p = total1 / total2
		print(p)



	def writeGrades(self):
		f = open(self.filename, "a+")
		f.write("\n" + listToCSV(self.grade))

	def run(self):
		self.readfile()
		if self.grade == []:
			self.getsomeinput()
			self.writeGrades()
		else:
			self.calcGrade()


def listToCSV(lst) -> str:
	strings = ""
	for a in lst:
		strings += str(a) + ","
	strings = strings[0:len(strings) - 1]
	return strings

def freeWill() -> str:
	
	print("1 = AST121")
	print("2 = MAT137 Version 1")
	print("3 = MAT137 Version 2")
	print("4 = MAT223")
	print("5 = CSC165")
	print("6 = BIO130")

	a = input("What marks do you want?")

	if a == "1":
		return "AST121.csv"
	elif a == "2":
		return "MAT137-1.csv"
	elif a == "3":
		return "MAT137-2.csv"
	elif a == "4":
		return "MAT223.csv"
	elif a == "5":
		return "CSC165.csv"
	elif a == "6":
		return "BIO130.csv"
	else:
		print("Go die")

if __name__ == "__main__":
	inp = freeWill()
	r = Reader(inp)
	r.run()