#!/usr/bin/python3
import unittest
from models.base import Base


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

        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 6)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 8)

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


if __name__ == '__main__':
    unittest.main()
