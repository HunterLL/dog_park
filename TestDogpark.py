'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

import unittest
from class_Dogpark import *
from class_Neighbourhood import*

class testDogpark(unittest.TestCase):

    def test_init_basic(self):
        my_dogpark = Dogpark("George Park", "Sunset")
        self.assertEqual(my_dogpark.name, "George Park")
        self.assertEqual(my_dogpark.neighbourhood, "Sunset")

    def test_bad_init(self):
        with self.assertRaises(TypeError):
            your_dogpark = Dogpark(-2, "Sunset")
        with self.assertRaises(TypeError):
            his_dogpark = Dogpark("George Park", 4)

    def test_str(self):
        my_park = Dogpark("George Park", "Sunset")
        self.assertEqual(str(my_park), "George Park is located in Sunset.")

    def test_eq(self):
        my_dogpark = Dogpark("George Park", "Sunset")
        your_dogpark = Dogpark("Sunset Park", "Sunset")
        self.assertTrue(my_dogpark == your_dogpark)
        his_dogpark = Dogpark("Valdez Park", "Dunbar-Southlands")
        self.assertFalse(my_dogpark == his_dogpark)

        with self.assertRaises(TypeError):
            my_neighbourhood = Neighbourhood("Downtown", 100, 20, "20%")
            my_dogpark.__eq__(my_neighbourhood)

def main():
     unittest.main(verbosity = 3 )

main()