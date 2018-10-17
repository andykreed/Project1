import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

"""
Andrew Reed
andyreed
SI206
"""

def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	lst = []
	infile = open(file,'r')

	#Get headers from first row
	header = infile.readline()
	h1 = header.split(',')

	#Read in first line
	line = infile.readline()
	l1 = line.split(',')

	#Loop through rest of lines
	while line:
		l1 = line.split(',')
		d = {}

		#Create value-key pairs
		first = d[h1[0]] = l1[0] #'First'
		last = d[h1[1]] = l1[1] #'Last'
		email = d[h1[2]] = l1[2] #'Email'
		class_ = d[h1[3]] = l1[3] #'Class'
		dob = d[h1[4].strip()] = l1[4].strip() #'DOB'

		#Add dictionary object to list and read next line
		lst.append(d)
		line = infile.readline()

	# close file and return list of dictionary objects
	infile.close()
	return(lst)

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	data.sort(key=lambda d: d[col])
	return str(data[0]["First"] + " " + data[0]["Last"])


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	numberOfSeniors = 0
	numberOfJuniors = 0
	numberOfSophomores = 0
	numberOfFreshmen = 0

	for student in data:
		if student['Class'] == 'Senior':
			numberOfSeniors += 1
		elif student['Class'] == 'Junior':
			numberOfJuniors += 1
		elif student['Class'] == 'Sophomore':
			numberOfSophomores += 1
		elif student['Class'] == 'Freshman':
			numberOfFreshmen += 1
		else:
			print("ERROR IN CLASSSIZES")
	classSizes = [('Senior', numberOfSeniors),('Junior',numberOfJuniors),
	('Sophomore',numberOfSophomores),('Freshman',numberOfFreshmen)]

	return sorted(classSizes,key=lambda classSizes: classSizes[1], reverse=True)

def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	d = {'1':0,
		 '2':0,
		 '3':0,
		 '4':0,
		 '5':0,
		 '6':0,
		 '7':0,
		 '8':0,
		 '9':0,
		 '10':0,
		 '11':0,
		 '12':0}

	for student in a:
		date = a[i]["DOB"].split('/')
		month = date[0]

		if month == 1:
			d['1'] += 1
		elif month ==2:
			d['2'] += 1
		elif month ==3:
			d['3'] += 1
		elif month ==4:
			d['4'] += 1
		elif month ==5:
			d['5'] += 1
		elif month ==6:
			d['6'] += 1
		elif month ==7:
			d['7'] += 1
		elif month ==8:
			d['8'] += 1
		elif month ==9:
			d['9'] += 1
		elif month ==10:
			d['10'] += 1
		elif month ==11:
			d['11'] += 1
		elif month ==12:
			d['12'] += 1
		else:
			print("FINDMONTH ERROR")

	return max(d,key=d.get)

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	a.sort(key=lambda d: d["First"]) #THIS IS HARDCODED
	a.sort(key=lambda d: d[col])

	outFile = open(fileName,'w')

	for student in a:
		outFile.write(student["First"] + "," + student["Last"] + "," + student["Email"] + "\n")

	outFile.close()

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	# print("\nThe most common month of the year to be born is:")
	# total += test(findMonth(data),3,15)
	# total += test(findMonth(data2),3,15)
	#
	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)
	#
	# print("\nTest of extra credit: Calcuate average age")
	# total += test(findAge(data), 40, 5)
	# total += test(findAge(data2), 42, 5)
	#
	# print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
