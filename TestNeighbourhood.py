'''
    CS5001 2022 Fall
    Hunter(Chenlei Luo)
    Milestone 2
'''

import unittest
from class_Neighbourhood import *
from class_Park import *

class testNeighbourhood(unittest.TestCase):

    def test_init_basic(self):
        my_neighbourhood = Neighbourhood("Sunset")
        self.assertEqual(my_neighbourhood.name, "Sunset")
        self.assertEqual(my_neighbourhood.park, [])
        self.assertEqual(my_neighbourhood.dogpark, [])
        self.assertEqual(my_neighbourhood.percentage, 0)

    def test_bad_init(self):
        with self.assertRaises(TypeError):
            my_neighbourhood = Neighbourhood(100)

    def test_str(self):
        my_neighbourhood = Neighbourhood("Sunset")
        self.assertEqual(str(my_neighbourhood), "Sunset has 0 parks among which the number of dog off-leash park(s) is 0.")

    def test_eq(self):
        my_neighbourhood = Neighbourhood("Downtown")
        her_neighbourhood = Neighbourhood("Sunset")
        self.assertTrue(my_neighbourhood.__eq__(her_neighbourhood)) #Their initial percentages are equal

        his_neighbourhood = Neighbourhood("West End")
        his_neighbourhood.update_park_attribute("Adden Park")
        his_neighbourhood.update_park_attribute("Bit Park")
        his_neighbourhood.update_dogpark_attribute("Bit Park")
        his_neighbourhood.calculate_percentage()
        self.assertFalse(my_neighbourhood.__eq__(his_neighbourhood))

        with self.assertRaises(TypeError):
            my_park = Park("Central Park", "Downtown")
            my_neighbourhood.__eq__(my_park)

    def test_update_park_attribute(self):
        my_neighbourhood = Neighbourhood("Sunset")
        my_neighbourhood.update_park_attribute("Abbey Park")
        self.assertTrue("Abbey Park" in my_neighbourhood.park)
        with self.assertRaises(TypeError):
            my_neighbourhood.update_park_attribute(123)

    def test_update_dogpark_attribute(self):
        my_neighbourhood = Neighbourhood("Sunset")
        my_neighbourhood.update_dogpark_attribute("Abbey Park")
        self.assertTrue("Abbey Park" in my_neighbourhood.dogpark)
        with self.assertRaises(TypeError):
            my_neighbourhood.update_park_attribute(123)

    def test_calculate_percentage(self):
        my_neighbourhood = Neighbourhood("Sunset")
        my_neighbourhood.update_park_attribute("Abbey Park")
        my_neighbourhood.update_park_attribute("Jennifer Park")
        my_neighbourhood.update_dogpark_attribute("Abbey Park")
        my_neighbourhood.calculate_percentage()
        self.assertEqual(my_neighbourhood.percentage, 50)
        with self.assertRaises(ZeroDivisionError):
            his_neighbourhood = Neighbourhood("Sunset")
            his_neighbourhood.update_dogpark_attribute("Abbey Park")
            his_neighbourhood.calculate_percentage()
            his_neighbourhood.percentage


def main():
     unittest.main(verbosity = 3 )

main()