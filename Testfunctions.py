'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

import unittest
from class_Park import *
from class_Neighbourhood import*
from functions import*

class testfunctions(unittest.TestCase):

    def test_get_file(self):
        URL = "https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv"
        urls_string1 = '''1,"Eldon Base for stackable storage shelf, platinum",Muhammed MacIntyre,3,-213.25,38.94,35,Nunavut,Storage & Organization,0.8'''
        self.assertTrue(urls_string1 in get_file(URL))
        with self.assertRaises(HTTPError):
            get_file("https://api.github.com/invalid")

    def test_get_parks_list(self):
        file = "id;park;neighbourhood;year;facility;washroom\n1;Village Of Yorkville Park;Yorkville;1990;Y;Y\n2;Larry Sefton Park;Downtown;1990;Y;Y\n"
        file_list = [["id", "park", "neighbourhood", "year", "facility", "washroom"], ["1", "Village Of Yorkville Park", "Yorkville", "1990", "Y", "Y"], ["2", "Larry Sefton Park", "Downtown", "1990", "Y", "Y"]]
        self.assertEqual(get_parks_list(file), file_list)
        with self.assertRaises(TypeError):
            get_parks_list(123)

    def test_get_park_name_list(self):
        file_list = [["id", "park", "neighbourhood", "year", "facility", "washroom"], ["1", "Village Of Yorkville Park", "Yorkville", "1990", "Y", "Y"], ["2", "Larry Sefton Park", "Downtown", "1990", "Y", "Y"]]
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park"]
        self.assertEqual(get_park_name_list(file_list), park_name_list)
        with self.assertRaises(TypeError):
            get_park_name_list(123)

    def test_get_neighbourhood_list(self):
        file_list = [["id", "park", "neighbourhood", "year", "facility", "washroom"], ["1", "Village Of Yorkville Park", "Yorkville", "1990", "Y", "Y"], ["2", "Larry Sefton Park", "Downtown", "1990", "Y", "Y"]]
        neighbourhood_list = ["Yorkville", "Downtown"]
        self.assertEqual(get_neighbourhood_list(file_list), neighbourhood_list)
        with self.assertRaises(TypeError):
            get_park_name_list(123)

    def test_create_park_object_list(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park"]
        neighbourhood_list = ["Yorkville", "Downtown"]
        Village_Of_Yorkville_Park = Park("Village Of Yorkville Park", "Yorkville")
        Larry_Sefton_Park = Park("Larry Sefton Park", "Downtown")
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list)
        self.assertEqual(park_object_list, [Village_Of_Yorkville_Park, Larry_Sefton_Park])
        with self.assertRaises(TypeError):
            create_park_object_list(123, neighbourhood_list)
        with self.assertRaises(TypeError):
            create_park_object_list(park_name_list, 123)

    def test_get_dogpark_name_list(self):
        dog_parks_list = [["id", "neighbourhood", "park\r"], ["1", "Yorkville", "Village Of Yorkville Park\r"], ["2", "Downtown", "Larry Sefton Park\r"]]
        dogpark_name_list1 = get_dogpark_name_list(dog_parks_list)
        dogpark_name_list2 = ["Village Of Yorkville Park", "Larry Sefton Park"]
        self.assertEqual(dogpark_name_list1, dogpark_name_list2)
        with self.assertRaises(TypeError):
            get_dogpark_name_list(123)

    def test_get_dog_neighbourhood_list(self):
        dog_parks_list = [["id", "neighbourhood", "park\r"], ["1", "Yorkville", "Village Of Yorkville Park\r"], ["2", "Downtown", "Larry Sefton Park\r"]]
        dog_neighbourhood_list1 = get_dog_neighbourhood_list(dog_parks_list)
        dog_neighbourhood_list2 = ["Yorkville", "Downtown"]
        self.assertEqual(dog_neighbourhood_list1, dog_neighbourhood_list2)
        with self.assertRaises(TypeError):
            get_dog_neighbourhood_list(123)

    def test_create_dogpark_object_list(self):
        dog_parks_list = [["id", "neighbourhood", "park\r"], ["1", "Yorkville", "Village Of Yorkville Park\r"], ["2", "Downtown", "Larry Sefton Park\r"]]
        dogpark_name_list1 = get_dogpark_name_list(dog_parks_list)
        dog_neighbourhood_list1 = get_dog_neighbourhood_list(dog_parks_list)
        dogpark_object_list = create_dogpark_object_list(dogpark_name_list1, dog_neighbourhood_list1)
        Village_Of_Yorkville_Park = Dogpark("Village Of Yorkville Park", "Yorkville")
        Larry_Sefton_Park = Dogpark("Larry Sefton Park", "Downtown")
        self.assertEqual(dogpark_object_list, [Village_Of_Yorkville_Park, Larry_Sefton_Park])
        with self.assertRaises(TypeError):
            create_dogpark_object_list(123, dog_neighbourhood_list1)
        with self.assertRaises(TypeError):
            create_dogpark_object_list(dogpark_name_list1, 123)

    def test_update_dog_neighbourhood_attribute(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park"]
        neighbourhood_list = ["Yorkville", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list)   
        dogpark_name_list1 = ["Village Of Yorkville Park", "Larry Sefton Park"]
        dog_neighbourhood_list1 = ['', "Downtown"]
        dogpark_object_list = create_dogpark_object_list(dogpark_name_list1, dog_neighbourhood_list1)
        updated_dogpark_object_list = update_dog_neighbourhood_attribute(dogpark_object_list, park_object_list)
        Village_Of_Yorkville_Park = Dogpark("Village Of Yorkville Park", "Yorkville")
        Larry_Sefton_Park = Dogpark("Larry Sefton Park", "Downtown")
        self.assertEqual(updated_dogpark_object_list, [Village_Of_Yorkville_Park, Larry_Sefton_Park])
        with self.assertRaises(TypeError):
            update_dog_neighbourhood_attribute(123, park_object_list)
        with self.assertRaises(TypeError):
            update_dog_neighbourhood_attribute(dogpark_object_list, 123)

    def test_create_final_neighbourhood_list(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        self.assertEqual(final_neighbourhood_list, ["Yorkville", "Downtown"])
        with self.assertRaises(TypeError):
            create_final_neighbourhood_list(123)

    def test_create_neighbourhood_object_list(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list)
        Yorkville = Neighbourhood("Yorkville")
        Downtown = Neighbourhood("Downtown")
        self.assertEqual(neighbourhood_object_list, [Yorkville, Downtown])
        with self.assertRaises(TypeError):
            create_neighbourhood_object_list(123)

    def test_update_park_attributes(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list)
        updated_neighbourhood_object_list = update_park_attributes(park_object_list, neighbourhood_object_list)
        self.assertEqual(updated_neighbourhood_object_list[0].park, ["Village Of Yorkville Park"])
        self.assertEqual(updated_neighbourhood_object_list[1].park, ["Larry Sefton Park", "Grange Park"])
        with self.assertRaises(TypeError):
            update_park_attributes(123, neighbourhood_object_list)
        with self.assertRaises(TypeError):
            update_park_attributes(park_object_list, 123)

    def test_update_dogpark_attributes(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list) 
        dogpark_name_list1 = ["Village Of Yorkville Park", "Larry Sefton Park"]
        dog_neighbourhood_list1 = ["Yorkville", "Downtown"]
        dogpark_object_list = create_dogpark_object_list(dogpark_name_list1, dog_neighbourhood_list1)
        updated_neighbourhood_object_list = update_dogpark_attributes(dogpark_object_list, neighbourhood_object_list)
        self.assertEqual(updated_neighbourhood_object_list[0].dogpark, ["Village Of Yorkville Park"])
        self.assertEqual(updated_neighbourhood_object_list[1].dogpark, ["Larry Sefton Park"])
        with self.assertRaises(TypeError):
            update_dogpark_attributes(123, neighbourhood_object_list)
        with self.assertRaises(TypeError):
            update_dogpark_attributes(dogpark_object_list, 123)

    def test_calculate_percentage(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list) 
        dogpark_name_list1 = ["Village Of Yorkville Park", "Larry Sefton Park"]
        dog_neighbourhood_list1 = ["Yorkville", "Downtown"]
        dogpark_object_list = create_dogpark_object_list(dogpark_name_list1, dog_neighbourhood_list1)
        updated_neighbourhood_object_list1 = update_park_attributes(park_object_list, neighbourhood_object_list)
        updated_neighbourhood_object_list2 = update_dogpark_attributes(dogpark_object_list, updated_neighbourhood_object_list1)
        updated_neighbourhood_object_list3 = calculate_percentage(updated_neighbourhood_object_list2)
        self.assertEqual(updated_neighbourhood_object_list3[0].percentage, 100)
        self.assertEqual(updated_neighbourhood_object_list3[1].percentage, 50)
        with self.assertRaises(TypeError):
            calculate_percentage(123)

    def test_display_dataframe(self):
        park_name_list = ["Village Of Yorkville Park", "Larry Sefton Park", "Grange Park"]
        neighbourhood_list = ["Yorkville", "Downtown", "Downtown"]
        park_object_list = create_park_object_list(park_name_list, neighbourhood_list) 
        final_neighbourhood_list = create_final_neighbourhood_list(park_object_list)
        neighbourhood_object_list = create_neighbourhood_object_list(final_neighbourhood_list) 
        dogpark_name_list1 = ["Village Of Yorkville Park", "Larry Sefton Park"]
        dog_neighbourhood_list1 = ["Yorkville", "Downtown"]
        dogpark_object_list = create_dogpark_object_list(dogpark_name_list1, dog_neighbourhood_list1)
        updated_neighbourhood_object_list1 = update_park_attributes(park_object_list, neighbourhood_object_list)
        updated_neighbourhood_object_list2 = update_dogpark_attributes(dogpark_object_list, updated_neighbourhood_object_list1)
        updated_neighbourhood_object_list3 = calculate_percentage(updated_neighbourhood_object_list2)
        main_df = display_dataframe(updated_neighbourhood_object_list3)
        
        dataframe_dict = {"Neighbourhood": ["Yorkville", "Downtown"], "Number of parks": [1, 2], "Number of dog off-leash parks": [1, 1], "Dog off-leash park percentage": [100, 50]}
        data_frame = pd.DataFrame(dataframe_dict)

        self.assertEqual(main_df["Neighbourhood"].tolist(), data_frame["Neighbourhood"].tolist())
        self.assertEqual(main_df["Number of parks"].tolist(), data_frame["Number of parks"].tolist())
        self.assertEqual(main_df["Number of dog off-leash parks"].tolist(), data_frame["Number of dog off-leash parks"].tolist())
        self.assertEqual(main_df["Dog off-leash park percentage"].tolist(), data_frame["Dog off-leash park percentage"].tolist())
        
        with self.assertRaises(TypeError):
            display_dataframe(123)

def main():
     unittest.main(verbosity = 3 )

main()