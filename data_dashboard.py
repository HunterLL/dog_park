'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

URL_PARKS = "https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B" 
URL_DOG_PARKS = "https://opendata.vancouver.ca/explore/dataset/dog-off-leash-parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B"
MENU = '''\
A. Show the total number of parks per neighbourhood in descending order(Graph View)\n\
B. Show the total number of dog parks per neighbourhood in ascending order(Graph View)\n\
C. Show the total number of dog park percentage per neighbourhood in descending order(Graph View)\n\
D. Show the total number of parks and dog parks per neighbourhood(Graph View)\n\
Please enter a choice (A, B, C, D or Q):
'''
OPTION_1 = "a"
OPTION_2 = "b"
OPTION_3 = "c"
OPTION_4 = "d"
OPTION_5 = "q"
TITLE_1 = "Number of parks per neighbourhood"
TITLE_2 = "Number of dog off-leash parks per neighbourhood"
TITLE_3 = "Dog off-leash park percentage per neighbourhood"
TITLE_4 = "Number of parks and off-leash parks per neighbourhood"
ASCENDING_ORDER = True
DESCENDING_ORDER = False

import requests
from requests.exceptions import *
from functions import *
from starter_code import *
from class_Park import *
from class_Neighbourhood import *
from class_Dogpark import*
import pandas as pd
import matplotlib.pyplot as plt


def main():
	try:
		#get an online dataset and turn into a list of lists
		parks_file_string = get_file(URL_PARKS)
		parks_list = get_parks_list(parks_file_string)
		#get a list of all the park names from parks_list
		park_name_list = get_park_name_list(parks_list)
		#get a list of all the neighbourhood names corresponding to park names from parks_list
		neighbourhood_list = get_neighbourhood_list(parks_list)
		#turn park_name_list into a list of park objects each of whose attributes include park name and neighbourhood name
		park_object_list = create_park_object_list(park_name_list, neighbourhood_list)

		#get an online dataset and turn into a list of lists
		dog_parks_file_string = get_file(URL_DOG_PARKS)
		dog_parks_list = get_parks_list(dog_parks_file_string)
		#get a list of all the dog park names from dog_parks_list
		dogpark_name_list = get_dogpark_name_list(dog_parks_list)
		#get a list of all the dog neighbourhood names from dog_parks_list
		dog_neighbourhood_list = get_dog_neighbourhood_list(dog_parks_list)
		#create a dogpark class object list
		dogpark_object_list1 = create_dogpark_object_list(dogpark_name_list, dog_neighbourhood_list)
		#add mssing neighbour attributes of some dogpark objects in the dogpark class object list
		dogpark_object_list = update_dog_neighbourhood_attribute(dogpark_object_list1, park_object_list)
		
		#create neighbourhood_object class
		final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
		neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list)
		updated_neighbourhood_object_list = update_park_attributes(park_object_list, neighbourhood_object_list)
		updated_neighbourhood_object_list2 = update_dogpark_attributes(dogpark_object_list, updated_neighbourhood_object_list)
		updated_neighbourhood_object_list3 = calculate_percentage(updated_neighbourhood_object_list2)

		#display each of Neighourhood objects and their attributes by DataFrame
		print(display_dataframe(updated_neighbourhood_object_list3))

		#data visualization
		main_df = display_dataframe(updated_neighbourhood_object_list3)
		DONE = False
		while not DONE :
			user_input = input(MENU)
			if user_input.lower() == OPTION_1: #Graph: "Number of parks per neighbourhood"
				title1 = TITLE_1 
				df1 = main_df.sort_values(by = [labels[LABEL_ONE]], ascending = DESCENDING_ORDER)
				df1 = df1.loc[:, [labels[LABEL_ZERO], labels[LABEL_ONE]]]
				xticklabels1= df1[labels[LABEL_ZERO]].tolist()
				make_park_graph_from_data_frame(df1, xticklabels1, title1)
			elif user_input.lower() == OPTION_2: #Graph: "Number of dog off-leash parks per neighbourhood"
				title1 = TITLE_2 
				df1 = main_df.sort_values(by = [labels[LABEL_TWO]], ascending = ASCENDING_ORDER)
				df1 = df1.loc[:, [labels[LABEL_ZERO], labels[LABEL_TWO]]]
				xticklabels1 = df1[labels[LABEL_ZERO]].tolist()
				make_dog_park_graph_from_data_frame(df1, xticklabels1, title1)
			elif user_input.lower() == OPTION_3: #Graph: "Dog off-leash park percentage"
				title1 = TITLE_3 
				df1 = main_df.sort_values(by = [labels[LABEL_THREE]], ascending = DESCENDING_ORDER)
				df1 = df1.loc[:, [labels[LABEL_ZERO], labels[LABEL_THREE]]]
				xticklabels1 = df1[labels[LABEL_ZERO]].tolist()
				make_percentage_graph_from_data_frame(df1, xticklabels1, title1)
			elif user_input.lower() == OPTION_4: #Graph: "The number of parks and off-leash parks per neighbourhood"
				title1 = TITLE_4 
				df1 = main_df.loc[:, [labels[LABEL_ZERO], labels[LABEL_ONE], labels[LABEL_TWO]]]
				xticklabels1 = df1[labels[LABEL_ZERO]].tolist()
				make_overall_graph_from_data_frame(df1, xticklabels1, title1)
			elif user_input.lower() == OPTION_5: #Exit the program
				DONE = True
			else:
				print("Wrong input!")
	except MissingSchema:
		print("URL is not complete")
	except HTTPError as err:
		print(err)
	except ConnectionError as err:
		print(err)
	except NameError as err:
		print(err)
	except TypeError as err:
		print(err)

if __name__ == "__main__":
	main()










