'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

class Park:
	'''
    Park is a class to represent a park. Constructor: __init__(self, name, neighbourhood)
    constructs necessary attributes: name and neighbourhood. __str__() returns the string
     representation of the object: which neighbourhood each park is located in. 
	 __eq__(self, another) can check equality with other parks based on neighbourhood.
    '''

	def __init__(self, name, neighbourhood):
		'''
    	Purpose: constructs all the necessary attributes for the park object.
    	Parameters:
        	self: the park object that is calling the method
			name: a string representing the name of each park
        	neighbourhood: a string representing the neighbourhood each park belongs to
    	Return: None.
    	Raise error: TypeError
    	'''

		if not isinstance(name, str) or not isinstance(neighbourhood, str):
			raise TypeError
		self.name = name
		self.neighbourhood = neighbourhood

	def __str__(self):
		'''
		Purpose: returns a string, describing which neighbourhood each park is located in.
		Parameters:
			self: the park object that is calling the method
		Return: returns a string, describing which neighbourhood each park is located in.
		Raise error: None
		'''

		return f"{self.name} is located in {self.neighbourhood}."

	def __eq__(self, another):
		'''
		Purpose: check equality with another park class object
		Parameters:
			self: the park object that is calling the method
			another: another park object
		Return: returns a boolean True if two objects' neighbourhoods are the same or False if not.
		Raise error: 
			raises TypeError if the other object being compared is not a park class object.
		'''

		if not isinstance(another, Park):
			raise TypeError("The argument compared is not a park class object.")
		return self.neighbourhood == another.neighbourhood
