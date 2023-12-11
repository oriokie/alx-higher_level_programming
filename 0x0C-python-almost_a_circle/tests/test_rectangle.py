#!/usr/bin/python3
"""
Test Rectangle Module
"""
import unittest
from models.base import *
from models.rectangle import *
import sys
import io


class TestRectangle(unittest.TestCase):
    """
    This is the unittest for the Rectangle Class
    """
    def test_init(self):
        """
        Testing initialization of the variables
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_doc_1(self):
        """
        PEP Validation 1
        """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_doc_2(self):
        """
        PEP Validation 2
        """
        self.assertIsNotNone(Rectangle.__init__.__doc__)

    def test_doc_3(self):
        """
        PEP Validation 3
        """
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_width_setter(self):
        """
        Testing width
        """
        rect = Rectangle(1, 1)
        rect.width = 85
        self.assertEqual(rect.width, 85)

    def test_width_setter_invalid(self):
        """
        Testing width
        """
        rect = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            rect.width = "hey"

    def test_width_value(self):
        """
        Testing width
        """
        rect = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter(self):
        """
        Testing height
        """
        rect = Rectangle(1, 1)
        rect.height = 10
        self.assertEqual(rect.height, 10)

    def test_height_setter_invalid(self):
        """
        Testing Height
        """
        rect = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            rect.height = "hey"

    def test_height_value(self):
        """
        Testing width
        """
        rect = Rectangle(1, 1)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x(self):
        """
        Testing x
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.x, 2)

    def test_empty_args(self):
        """
        Testing empty args
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_more_args(self):
        """
        Testing more args
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_less_args(self):
        """
        Testing less args
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_private_width_attribute(self):
        """
        Testing private attribute (width)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__width

    def test_private_height_attribute(self):
        """
        Testing private attribute (height)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__height

    def test_private_x_attribute(self):
        """
        Testing private attribute (x)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__x

    def test_private_y_attribute(self):
        """
        Testing private attribute (y)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__y

    def test_height_attribute(self):
        """
        Testing height attribute
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.height, 10)

    def test_width_attribute(self):
        """
        Testing width attribute
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)

    def test_x_attribute(self):
        """
        Testing x attribute
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.x, 2)

    def test_y_attribute(self):
        """
        Testing y attribute
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.y, 3)

    def test_given_id(self):
        """
        Testing given id
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.id, 1)


class TestAttributes(unittest.TestCase):
    """
    Testing attributes
    """
    def test_private_width_attribute(self):
        """
        Testing private attribute (width)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__width

    def test_private_height_attribute(self):
        """
        Testing private attribute (height)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__height

    def test_private_x_attribute(self):
        """
        Testing private attribute (x)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__x

    def test_private_y_attribute(self):
        """
        Testing private attribute (y)
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(AttributeError):
            rect.__y

    def test_raises_typoe_error(self):
        """
        Testing raises type error
        """
        with self.assertRaises(TypeError) as err:
            Rectangle("5", 10)
        self.assertEqual("width must be an integer",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(5, "10")
        self.assertEqual("height must be an integer",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(5, 10, "2")
        self.assertEqual("x must be an integer",
                         str(err.exception))

        with self.assertRaises(TypeError) as err:
            Rectangle(5, 10, 2, "3")
        self.assertEqual("y must be an integer",
                         str(err.exception))

    def test_other_typeerrors(self):
        """
        Testing other type errors
        """
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 10)
        self.assertEqual("width must be > 0",
                         str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(5, 0)
        self.assertEqual("height must be > 0",
                         str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(5, 10, -2)
        self.assertEqual("x must be >= 0",
                         str(err.exception))

        with self.assertRaises(ValueError) as err:
            Rectangle(5, 10, 2, -3)
        self.assertEqual("y must be >= 0",
                         str(err.exception))


class TestArea(unittest.TestCase):
    """
    Testing area
    """
    def test_area(self):
        """
        Testing area
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_area_allargs(self):
        """
        Testing area with all args
        """
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.area(), 50)


class TestDisplay(unittest.TestCase):
    """
    Testing display
    """
    def test_str_representation(self):
        """
        Testing string representation
        """
        rect = Rectangle(5, 10, 0, 0, 1)
        self.assertEqual(rect.__str__(), "[Rectangle] (1) 0/0 - 5/10")


class TestUpdate(unittest.TestCase):
    """
    Testing update
    """
    def test_update(self):
        """
        Testing update
        """
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

        rect.update(x=12)
        self.assertEqual("[Rectangle] (89) 12/10 - 2/3", str(rect))

        rect.update(size=7, y=1)
        self.assertEqual("[Rectangle] (89) 12/1 - 2/3", str(rect))


class TestDict(unittest.TestCase):
    """
    Testing dictionary
    """
    def test_dictionary(self):
        """
        Testing dictionary
        """
        rect = Rectangle(10, 10, 10, 10, 1)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict["id"], 1)
        self.assertEqual(rect_dict["width"], 10)
        self.assertEqual(rect_dict["height"], 10)
        self.assertEqual(rect_dict["x"], 10)
        self.assertEqual(rect_dict["y"], 10)


if __name__ == "__main__":
    unittest.main()
