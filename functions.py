'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 1
'''

NEWLINE = "\n"
SEMICOLON = ";"
EMPTY_LIST = ['']
PARK_NAME_INDEX = 1
HEADER_INDEX = 0
NEIGHBOURHOOD_INDEX = -4
DOGPARK_INDEX = -1
CARRIAGE_RETURN = "\r"
DOG_NEIGHBOURHOOD_INDEX = -2
STRIPPED_CONTENT = "Park"
EMPTY_DOGPARK_NAME = ''
UNKNOWN_PARK = " unknown Park"
LABEL_ZERO = 0
LABEL_ONE= 1
LABEL_TWO = 2
LABEL_THREE = 3
labels = ["Neighbourhood", "Number of parks", "Number of dog off-leash parks", "Dog off-leash park percentage"]

import requests
from requests.exceptions import *
from class_Park import *
from class_Neighbourhood import *
from class_Dogpark import*
import pandas as pd

def get_file(url):
	'''
	Function -- get_file
		Gets a csv online dataset from an url and turn into a string containing all the information in the dataset
	Parameters: 
		url -- a url string
	Returns a string
	Raises HTTPError/ConnectionError/MissingSchema
	'''

	try:
		response = requests.get(url)
		response.raise_for_status()
		file = response.text
		return file
	except ConnectionError as err:
		print(f'No response: {err}')		
	except MissingSchema:
		print('URL is not complete')

def get_parks_list(file):
	'''
	Function -- get_parks_list
		Turns a dataset string into a list of lists in which each sublist contains one park's information
	Parameters: 
		file -- a string
	Returns a list of lists
	Raises TypeError
	'''

	if not isinstance(file, str):
		raise TypeError("The argument of get_parks_list() shoud be a string.")
	list_of_strings = file.split(NEWLINE)
	list_of_lists = []
	for i in list_of_strings:
		each = i.split(SEMICOLON)
		if not (each == EMPTY_LIST):
			list_of_lists.append(each)
	return list_of_lists	

def get_park_name_list(parks_list):
	'''
	Function -- get_park_name_list
		Gets a list of all the park names from parks_list
	Parameters: 
		parks_list -- a list of lists
	Returns a list of all the park names from parks_list
	Raises TypeError
	'''

	if not isinstance(parks_list, list):
		raise TypeError("The argument of get_park_name_list() shoud be a list.")
	park_name_list = []
	for parkname in parks_list:
		park_name_list.append(parkname[PARK_NAME_INDEX])
	park_name_list.pop(HEADER_INDEX)
	return park_name_list

def get_neighbourhood_list(parks_list):
	'''
	Function -- get_neighbourhood_list
		Gets a list of all the neighbourhood names from parks_list
	Parameters: 
		parks_list -- a list of lists
	Returns a list of all the neighbourhood names from parks_list
	Raises TypeError
	'''

	if not isinstance(parks_list, list):
		raise TypeError("The argument of get_neighbourhood_list() shoud be a list.")
	neighbourhood_list = []
	for neighbourhood in parks_list:
		neighbourhood_list.append(neighbourhood[NEIGHBOURHOOD_INDEX])
	neighbourhood_list.pop(HEADER_INDEX)
	return neighbourhood_list

def create_park_object_list(park_name_list, neighbourhood_list):
	'''
	Function -- create_park_object_list
		Turns park_name_list into a list of Park class objects
	Parameters: 
		park_name_list -- a list of park names
		neighbourhood_list -- a list of corresponding neighbourhood names
	Returns a list of Park class objects
	Raises TypeError
	'''

	if not isinstance(park_name_list, list) or not isinstance(neighbourhood_list, list):
		raise TypeError("The arguments of create_park_object_list() shoud be lists.")
	for i in range(len(park_name_list)):
		park_name_list[i] = Park(park_name_list[i], neighbourhood_list[i])
	return park_name_list


def get_dogpark_name_list(dog_parks_list):
	'''
	Function -- get_dogpark_name_list
		Gets a list of all the dog off-leash park names from dog_parks_list
	Parameters: 
		dog_parks_list -- a list of lists
	Returns a list
	Raises TypeError
	'''

	if not isinstance(dog_parks_list, list):
		raise TypeError("The argument of get_dogpark_name_list() shoud be a list.")
	dogpark_name_list = []
	for dogparkname in dog_parks_list:
		dogpark_name_list.append(dogparkname[DOGPARK_INDEX].rstrip(CARRIAGE_RETURN))
	dogpark_name_list.pop(HEADER_INDEX)
	return dogpark_name_list

def get_dog_neighbourhood_list(dog_parks_list):
	'''
	Function -- get_dog_neighbourhood_list
		Gets a list of all the neighbourhoods of dog off-leash parks from dog_parks_list
	Parameters: 
		dog_parks_list -- a list of lists
	Returns a list
	Raises TypeError
	'''

	if not isinstance(dog_parks_list, list):
		raise TypeError("The argument of get_dog_neighbourhood_list() shoud be a list.")
	dog_neighbourhood_list = []
	for neighbourhood in dog_parks_list:
		dog_neighbourhood_list.append(neighbourhood[DOG_NEIGHBOURHOOD_INDEX])
	dog_neighbourhood_list.pop(HEADER_INDEX)
	return dog_neighbourhood_list	

def create_dogpark_object_list(dogpark_name_list, dog_neighbourhood_list):
	'''
	Function -- create_dogpark_object_list
		Turns dogpark_name_list into a list of Dogpark class objects
	Parameters: 
		dogpark_name_list -- a list of dog off-leash park names
		dog_neighbourhood_list -- a list of corresponding neighbourhood names
	Returns a list of Dogpark class objects
	Raises TypeError
	'''

	if not isinstance(dogpark_name_list, list) or not isinstance(dog_neighbourhood_list, list):
		raise TypeError("The arguments of create_dogpark_object_list() shoud be lists.")
	for i in range(len(dogpark_name_list)):
		if dogpark_name_list[i] == EMPTY_DOGPARK_NAME:
			dogpark_name_list[i] = Dogpark(str(i) + UNKNOWN_PARK, dog_neighbourhood_list[i])
		else:
			dogpark_name_list[i] = Dogpark(dogpark_name_list[i], dog_neighbourhood_list[i])
	return dogpark_name_list

def update_dog_neighbourhood_attribute(dogpark_object_list1, park_object_list):
	'''
	Function -- update_dog_neighbourhood_attribute
		Finds missing neighbourhood attributes of some dogpark objects and updates dogpark_object_list1
	Parameters: 
		dogpark_object_list1 -- a list of Dogpark class objects
		park_object_list -- a list of Park class objects
	Returns a list of Dogpark class objects
	Raises TypeError
	'''

	if not isinstance(dogpark_object_list1, list) or not isinstance(park_object_list, list):
		raise TypeError("The arguments of update_dog_neighbourhood_attribute() shoud be lists.")
	for i in range(len(dogpark_object_list1)):
		for val in park_object_list:
			if (dogpark_object_list1[i].neighbourhood == EMPTY_DOGPARK_NAME) and (dogpark_object_list1[i].name.strip(STRIPPED_CONTENT) in val.name):
				dogpark_object_list1[i].neighbourhood = val.neighbourhood
	return dogpark_object_list1

def create_final_neighbourhood_list(park_object_list):
	'''
	Function -- create_final_neighbourhood_list
		Creates a list of neighbourhood names(Each one is unique in the list).
	Parameters: 
		park_object_list -- a list of Park class objects
	Returns a list of neighbourhood names(Each one is unique in the list).
	Raises TypeError
	'''

	if not isinstance(park_object_list, list):
		raise TypeError("The argument of create_final_neighbourhood_list() shoud be a list.")
	neighbourhood = []
	for park in park_object_list:
		if not park.neighbourhood in neighbourhood:
			neighbourhood.append(park.neighbourhood)
		else:
			continue
	return neighbourhood

def create_neighbourhood_object_list(final_neighbourhood_list):
	'''
	Function -- create_neighbourhood_object_list
		Creates a list of neighbourhood objects.
	Parameters: 
		final_neighbourhood_list -- a list of neighbourhood names
	Returns a list of neighbourhood objects.
	Raises TypeError
	'''

	if not isinstance(final_neighbourhood_list, list):
		raise TypeError("The argument of create_neighbourhood_object_list() shoud be a list.")
	neighbourhood_object_list = []
	for neighbourhood in final_neighbourhood_list:
		neighbourhood = Neighbourhood(neighbourhood)
		neighbourhood_object_list.append(neighbourhood)
	return neighbourhood_object_list

def update_park_attributes(park_object_list, neighbourhood_object_list):
	'''
	Function -- update_park_attributes
		Finds all the parks belong to each neighbourhood objects and updates their park attributes.
	Parameters: 
		park_object_list -- a list of Park class objects
		neighbourhood_object_list -- a list of Neighbourhood class objects
	Returns a list of neighbourhood objects.
	Raises TypeError
	'''

	if not isinstance(park_object_list, list) or not isinstance(neighbourhood_object_list, list):
		raise TypeError("The arguments of update_park_attributes() shoud be lists.")
	for neighbourhood in neighbourhood_object_list:
		for park in park_object_list:
			if park.neighbourhood == neighbourhood.name:
				neighbourhood.update_park_attribute(park.name)
	return neighbourhood_object_list
#new update
def update_dogpark_attributes(dogpark_object_list, neighbourhood_object_list):
	'''
	Function -- update_dogpark_attributes
		Finds all the dogparks belong to each neighbourhood objects and updates their dogpark attributes.
	Parameters: 
		dogpark_object_list -- a list of Dogpark class objects
		neighbourhood_object_list -- a list of Neighbourhood class objects
	Returns a list of neighbourhood objects.
	Raises TypeError
	'''

	if not isinstance(dogpark_object_list, list) or not isinstance(neighbourhood_object_list, list):
		raise TypeError("The arguments of update_dogpark_attributes() shoud be lists.")
	for i in neighbourhood_object_list:
		for v in dogpark_object_list:
			if v.neighbourhood == i.name:
				i.update_dogpark_attribute(v.name)
	return neighbourhood_object_list

def calculate_percentage(neighbourhood_object_list):
	'''
	Function -- calculate_percentage
		Calculates all the dog off-leash park percentage per neighbourhood.
	Parameters: 
		neighbourhood_object_list -- a list of Neighbourhood class objects
	Returns a list of neighbourhood objects.
	Raises TypeError
	'''

	if not isinstance(neighbourhood_object_list, list):
		raise TypeError("The argument of calculate_percentage() shoud be a list.")
	for neighbourhood in neighbourhood_object_list:
		neighbourhood.calculate_percentage()
	return neighbourhood_object_list

def display_dataframe(neighbourhood_object_list):
	'''
	Function -- display_dataframe 
		Displays each neighbourhood_object_list's attributes by DataFrame from pandas
	Parameters: 
		neighbourhood_object_list -- a list
	Returns a DataFrame
	Raises TypeError
	'''

	if not isinstance(neighbourhood_object_list, list):
		raise TypeError("The argument of display_dataframe() shoud be a list.")
	dataframe_dict = {}
	name_list = []
	park_num_list = []
	dogpark_num_list = []
	percentage_num_list = []
	for item in neighbourhood_object_list:
		name_list.append(item.name)
		park_num_list.append(len(item.park))
		dogpark_num_list.append(len(item.dogpark))
		percentage_num_list.append(item.percentage)
	dataframe_dict[labels[LABEL_ZERO]] = name_list
	dataframe_dict[labels[LABEL_ONE]] = park_num_list
	dataframe_dict[labels[LABEL_TWO]] = dogpark_num_list
	dataframe_dict[labels[LABEL_THREE]] = percentage_num_list
	data_frame = pd.DataFrame(dataframe_dict)
	return data_frame