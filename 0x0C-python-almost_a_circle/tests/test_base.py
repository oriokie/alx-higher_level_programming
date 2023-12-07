#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This is the unittest for the Base Class
    """
    def setUp(self):
        """
        Set_up Method: 

        """
        #creating instances to be used in tests

        self.instances = [Base()]

        #creating a list of methods to be tested
        self.methods = [
                Base.__init__
                ]


    def tearDown(self):
        """
        Tear Down Method

        """
        pass

    def test_doc_1(self):
        """
        PEP Validation 1
        """
        self.assertIsNotNone(Base.__doc__)

    def test_base_instance_doc(self):
        """ Checking if the __doc__attribute of the Base Instances """
        for instance in self.instances:
            with self.subTest(instance=instance):
                self.assertIsNotNone(instance.__doc__)

    def test_base_methods_doc(self):
        """ Method to check if docstrings exist for all methods """
        for method in self.methods:
            with self.subTest(method=method):
                self.assertTrue(method.__doc__)

   
if __name__ == '__main__':
    unittest.main()
