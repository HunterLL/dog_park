'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

import unittest
from class_Park import *
from class_Neighbourhood import*

class testPark(unittest.TestCase):

    def test_init_basic(self):
        my_park = Park("Central Park", "Downtown")
        self.assertEqual(my_park.name, "Central Park")
        self.assertEqual(my_park.neighbourhood, "Downtown")

    def test_bad_init(self):
        with self.assertRaises(TypeError):
            your_park = Park(-2, "Downtown")
        with self.assertRaises(TypeError):
            his_park = Park("Central Park", 4)

    def test_str(self):
        my_park = Park("Central Park", "Downtown")
        self.assertEqual(str(my_park), "Central Park is located in Downtown.")

    def test_eq(self):
        my_park = Park("Central Park", "Downtown")
        your_park = Park("Stanley park", "Downtown")
        self.assertTrue(my_park == your_park)
        his_park = Park("George Park", "Sunset")
        self.assertFalse(my_park == his_park)

        with self.assertRaises(TypeError):
            my_neighbourhood = Neighbourhood("Downtown")
            my_park.__eq__(my_neighbourhood)

def main():
     unittest.main(verbosity = 3 )

main()