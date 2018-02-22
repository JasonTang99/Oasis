import csv
from fractions import Fraction
from typing import List

class Reader:
	filename = ""
	course = ""
	work = []
	scales = []
	grade = []

	def __init__(self, filename: str):
		self.filename = filename
		print("Initializing Skynet v0.23")
		print("")

	def readfile(self):
		with open(self.filename) as csvfile:
			readCSV = csv.reader(csvfile, delimiter = ",")
			b = 0

			for row in readCSV:
				if row != "":
					if   b == 0:
						self.course = row
					elif b == 1:
						self.work   = row
					elif b == 2:
						self.scales = row
					elif b == 3:
						self.grade  = row
				b += 1

		print("Course: "      + str(self.course) )
		print("Assignments: " + str(self.work)   )
		print("Scales: "      + str(self.scales) )
		print("Grades: "      + str(self.grade)  )

	def getsomeinput(self):
		total_got = 0
		total_mark = 0
		c = 0
		self.grade = []
		
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

		per = total_got/total_mark * 100

		print(self.grade)
		print("Your current percentage is " + str(per))

	def calcGrade(self):
		a = 0
		total1 = 0.0
		total2 = 0.0

		while a < len(self.grade):
			if self.grade[a] != '':
				total1 += float(self.grade[a]) * float(self.scales[a])
				total2 += float(self.scales[a])
			a += 1

		if total2 != 0:
			p = total1 / total2
			print(p)
		else:
			print("Make sure your csv file has proper scales inputed")

	def newGrades(self):
		f = open(self.filename, "w")
		f.write(self.course[0])
		f.write("\n" + listToCSV(self.work))
		f.write("\n" + listToCSV(self.scales))
		f.write("\n" + listToCSV(self.grade))

	def fillIn(self):
		a = 0
		while a < len(self.grade):
			if self.grade[a] == '':
				g = input("What did you get for " + self.work[a] + "? ")
				if g.replace(".", "", 1).replace("/", "", 1).isdigit():
					g = float(sum(Fraction(s) for s in g.split()))
					self.grade[a] = g
			a += 1

	def gradeStatus(self) -> int:
		# Returns 0,1,2 if the grade variable is empty, almost filled, and filled, respectively
		num_elements = 0

		for a in self.grade:
			if a != "":
				num_elements += 1

		if num_elements == 0:
			return 0
		elif num_elements == len(self.grade):
			return 2
		else:
			return 1

	def howMuch(self) -> float:
		counter = 0
		missing_index = 0
		a = 0
		total_grade = 0

		while a < len(self.grade):
			if self.grade[a] == '':
				counter += 1
				missing_index = a
			else:
				total_grade += float(self.grade[a]) * float(self.scales[a]) / 100.0
			a += 1

		if counter > 1:
			print("Fill up the grades until only one is left blank plz")
		else:
			final = float(input("What final grade do you want? "))
			return float( (final - total_grade) * 100 / float(self.scales[missing_index])  )




		

	def run(self):
		self.readfile()
		a = self.gradeStatus()

		if a == 0:
			self.getsomeinput()
			self.newGrades()

		elif a == 1:
			print("1 = Fill in the missing grades")
			print("2 = Calculate the current grade")
			print("3 = Rewrite the grades")
			print("")
			num = input("What do you want to do? ")
			if num == "1":
				self.fillIn()
				self.newGrades()
			elif num == "2":
				self.calcGrade()
			elif num == "3":
				self.getsomeinput()
				self.newGrades()
			else:
				print("Pick a valid option please")
				self.run()

		elif a == 2:
			print("1 = Calculate the current grade")
			print("2 = Rewrite the grades")
			print("")
			num = input("What do you want to do? ")
			if num == "1":
				self.calcGrade()
			elif num == "2":
				self.getsomeinput()
				self.newGrades()
			else:
				print("Pick a valid number please")
				self.run()

		else:
			print("Pick an option please")
			self.run()

	def test(self):
		self.readfile()
		print(self.howMuch())


def listToCSV(lst: List) -> str:
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

	a = input("What marks do you want? ")

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
		return freeWill()

if __name__ == "__main__":
	inp = freeWill()
	r = Reader(inp)
	# r.run()
	r.test()