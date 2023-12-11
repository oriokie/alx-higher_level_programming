#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import *
from models.square import *


class TestBase(unittest.TestCase):
    """
    This is the unittest for the Base Class
    """
    @classmethod
    def setUp(cls):
        """
        Set_up Method:

        """
        cls.instances = [Base(), Base(12)]

        cls.methods = [
                Base.__init__
                ]

    @classmethod
    def tearDown(self):
        """
        Tear Down Method

        """
        pass

    def test_increment(self):
        """Testing Increment of the __nb_object"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 6)
        self.assertEqual(b2.id, 7)
        self.assertEqual(b3.id, 8)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 9)

    def test_doc_1(self):
        """
        PEP Validation 1
        """
        self.assertIsNotNone(Base.__doc__)

    def test_base_instance_doc(cls):
        """ Checking if the __doc__attribute of the Base Instances """
        for instance in cls.instances:
            with cls.subTest(instance=instance):
                cls.assertIsNotNone(instance.__doc__)

    def test_base_methods_doc(cls):
        """ Method to check if docstrings exist for all methods """
        for method in cls.methods:
            with cls.subTest(method=method):
                cls.assertTrue(method.__doc__)


class OtherTests(unittest.TestCase):
    """
    Other tests for the Base Class
    """
    def test_returns_json_dict(self):
        """
        Tests Dictionary Serializing
        """
        rect = Rectangle(10, 7, 2, 8, 1)
        json_dictionary = rect.to_dictionary()
        self.assertEqual(type(json_dictionary), dict)
        self.assertEqual(len(json_dictionary), 5)
        self.assertEqual(json_dictionary["id"], 1)
        self.assertEqual(json_dictionary["width"], 10)
        self.assertEqual(json_dictionary["height"], 7)
        self.assertEqual(json_dictionary["x"], 2)
        self.assertEqual(json_dictionary["y"], 8)
        json_string = Base.to_json_string([rect.to_dictionary()])
        self.assertEqual(type(json_string), str)

    def test_writing_json_string_to_file(self):
        """
        Tests Writing JSON String to File
        """
        rect = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4)
        list_rectangles_input = [rect, rect2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(type(file.read()), str)

        with open("Rectangle.json", "r") as file:
            my_file = file.read()
            self.assertNotEqual(my_file, "")

    def test_from_json_string(self):
        """
        Tests from_json_string
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)
        expected_output = [{'id': 89, 'width': 10, 'height': 4},
                           {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(list_input, expected_output)


if __name__ == '__main__':
    unittest.main()
