'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''
ZERO_PERCENTAGE = 0
PERCENTAGE = 100

class Neighbourhood:
	'''
    Neighbourhood is a class to represent a neighbourhood. Constructor: 
	__init__(self, name, park_num, dogpark_num, percentage) constructs necessary attributes: 
	neighbourhood name, park number,  dog park number and dog park percentage. __str__() 
	returns the string representation of the object: how many dog parks and parks each 
	neighbourhood has. __eq__(self, another) can check equality with other neighbourhoods 
	based on dog park percentage.Method include update_park_attribute(self, newpark) adds 
	a park string into the park attribute(a list). Method update_dogpark_attribute(self, 
	newdogpark) adds a dog off-leash park string into the dogpark attribute(a list). Method
	calculate_percentage(self) calculates the dog off-leash park percentage per neighbourhood 
	and update the percentage attribute.
	'''

	def __init__(self, name):
		'''
    	Purpose: constructs all the necessary attributes for the neighbourhood object.
    	Parameters:
        	self: the neighbourhood object that is calling the method
			name: a string representing the name of each neighbourhood
    	Return: None.
    	Raise error: TypeError
		'''

		if not isinstance(name, str):
			raise TypeError("The argument name should be a string.")

		self.name = name
		self.park = []
		self.dogpark = []
		self.percentage = ZERO_PERCENTAGE

	def __str__(self):
		'''
		Purpose: returns a string, describing how many dog parks and parks each neighbourhood has.
		Parameters:
			self: the neighbourhood object that is calling the method
		Return: returns a string, describing how many dog parks and parks each neighbourhood has.
		Raise error: N/A
		'''

		return f"{self.name} has {len(self.park)} parks among which the number of dog off-leash park(s) is {len(self.dogpark)}."

	def __eq__(self, another):
		'''
		Purpose: check equality with another neighbourhood class object based on dog park percentage.
		Parameters:
			self: the neighbourhood object that is calling the method
			another: another neighbourhood object
		Return: returns a boolean True if two objects' percentages are the same or False if not.
		Raise error: 
			raises TypeError if the other object being compared is not a neighbourhood class object.
		'''

		if not isinstance(another, Neighbourhood):
			raise TypeError("The argument compared is not a neighbourhood class object.")
		return self.percentage == another.percentage

	def update_park_attribute(self, newpark):
		'''
		Purpose: adds a park string into the park attribute(a list).
		Parameters:
			self: the neighbourhood object that is calling the method
			newpark: a string
		Return: N/A
		Raise error:
			raises TypeError if newpark is not a string.
		'''

		if not isinstance(newpark, str):
			raise TypeError("The argument of update_park_attribute() is not a string.")
		self.park.append(newpark)
	
	def update_dogpark_attribute(self, newdogpark):
		'''
		Purpose: adds a dog off-leash park string into the dogpark attribute(a list).
		Parameters:
			self: the neighbourhood object that is calling the method
			newpark: a string
		Return: N/A
		Raise error:
			raises TypeError if newpark is not a string.
		'''

		if not isinstance(newdogpark, str):
			raise TypeError("The argument of update_dogpark_attribute() is not a string.")
		self.dogpark.append(newdogpark)
	
	def calculate_percentage(self):
		'''
		Purpose: calculates the dog off-leash park percentage per neighbourhood and update the percentage attribute.
		Parameters:
			self: the neighbourhood object that is calling the method
		Return: N/A
		Raise error: N/A
		'''

		result = (len(self.dogpark)/len(self.park)) * PERCENTAGE
		self.percentage = int(result)
		if self.park == ZERO_PERCENTAGE:
			raise ZeroDivisionError




