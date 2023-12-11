#!/usr/bin/python3
"""
Testing the Square Class
"""
import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class TestSquare(unittest.TestCase):
    """
    This is the unittest for the Square Class
    """
    def test_doc_1(self):
        """
        PEP Validation 1
        """
        self.assertIsNotNone(Square.__doc__)

    def test_doc_2(self):
        """
        PEP Validation 2
        """
        self.assertIsNotNone(Square.__init__.__doc__)

    def test_doc_3(self):
        """
        PEP Validation 3
        """
        self.assertIsNotNone(Square.__str__.__doc__)

    def test_doc_4(self):
        """
        PEP Validation 4
        """
        self.assertIsNotNone(Square.area.__doc__)

    def test_doc_5(self):
        """
        PEP Validation 5
        """
        self.assertIsNotNone(Square.display.__doc__)

    def test_doc_6(self):
        """
        PEP Validation 6
        """
        self.assertIsNotNone(Square.update.__doc__)

    def test_doc_7(self):
        """
        PEP Validation 7
        """
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_doc_8(self):
        """
        PEP Validation 8
        """
        self.assertIsNotNone(Square.__repr__.__doc__)

    def test_doc_9(self):
        """
        PEP Validation 9
        """
        self.assertIsNotNone(Square.__eq__.__doc__)

    def test_doc_10(self):
        """
        PEP Validation 10
        """
        self.assertIsNotNone(Square.__lt__.__doc__)

    def test_doc_11(self):
        """
        PEP Validation 11
        """
        self.assertIsNotNone(Square.__le__.__doc__)

    def test_create_instance(self):
        """
        Testing the creation of the instance
        """
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_raise_error(self):
        """
        Testing the raise error
        """
        with self.assertRaises(TypeError) as err:
            Square("5")
        self.assertEqual("width must be an integer",
                         str(err.exception))

        with self.assertRaises(ValueError) as err:
            Square(0, 10)
        self.assertEqual("width must be > 0",
                         str(err.exception))

        with self.assertRaises(ValueError) as err:
            Square(-10, 10)
        self.assertEqual("width must be > 0",
                         str(err.exception))


class TestSquareUpdates(unittest.TestCase):
    """
    Testing the updates
    """

    def test_update(self):
        """
        Testing the update
        """
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

        s.update(x=12)
        self.assertEqual("[Square] (89) 12/4 - 2", str(s))

        s.update(size=7, y=1)
        self.assertEqual("[Square] (89) 12/1 - 7", str(s))

        s.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 12/1 - 7", str(s))


class TestDictionary(unittest.TestCase):
    """
    Testing the dictionary
    """

    def test_to_dictionary(self):
        """
        Testing the dictionary
        """
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict["id"], 9)
        self.assertEqual(s_dict["size"], 10)
        self.assertEqual(s_dict["x"], 2)
        self.assertEqual(s_dict["y"], 1)


if __name__ == '__main__':
    unittest.main()
