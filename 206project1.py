import os
import filecmp
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	fh = open(file)
	final_list = []
	header_list = ["First", "Last", "Email", "Class", "DOB"]
	for line in fh:
		personal_dict = {}
		line = line.split(",")
		count = 0
		if line[0] not in header_list:
			for key in header_list:
				personal_dict[key] = line[count]
				count += 1
			final_list.append(personal_dict)
	return final_list



#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorted_data = sorted(data, key = lambda x: x[col])
	firstName = sorted_data[0]["First"]
	lastName = sorted_data[0]["Last"]
	return firstName + " " + lastName


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	class_dict = {}
	for user_dict in data:
		class_dict[user_dict["Class"]] = class_dict.get(user_dict["Class"], 0) + 1
	class_list = class_dict.items()
	return sorted(class_list, key = lambda x: x[1], reverse = True)




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_dict = {}
	for user_dict in a:
		day_dict[int(user_dict["DOB"].split("/")[1])] = day_dict.get(int(user_dict["DOB"].split("/")[1]), 0) + 1
	day_list = sorted (day_dict.items(), key = lambda x: x[1], reverse = True)
	return (day_list[0][0])





# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	age_list = []
	for user_dict in a:
		birth_year = int(user_dict["DOB"].split('/')[2])
		age = 2017 - birth_year
		age_list.append(age)
	total_years = 0
	for age in age_list:
		total_years += age
	return int(total_years/len(age_list))
#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	sorted_data = sorted(a, key = lambda x: x[col])
	user_file = open(fileName, "w")
	header_list = ["First", "Last", "Email"]
	for data in sorted_data:
		for header in header_list:
				user_file.write(data[header] + ",")
		user_file.write('\n')
	user_file.close()




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
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
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

