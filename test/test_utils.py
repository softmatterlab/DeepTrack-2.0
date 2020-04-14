import sys
sys.path.append("..") # Adds the module to path

import unittest

import deeptrack.utils as utils



class TestUtils(unittest.TestCase):
    
    def test_hasmethod(self):
        self.assertTrue(utils.hasmethod(utils, 'hasmethod'))
        self.assertFalse(utils.hasmethod(utils, 'this_is_definetely_not_a_method_of_utils'))
    

    def test_isiterable(self):
        self.assertFalse(utils.isiterable(1))
        
        non_iterable_obj = ('apple', 'banana', 'cherry')
        self.assertFalse(utils.isiterable(non_iterable_obj))

        iterable_obj = iter(('apple', 'banana', 'cherry'))
        self.assertTrue(utils.isiterable(iterable_obj))
    

    def test_as_list(self):
        
        obj = 1
        self.assertEqual(utils.as_list(obj), [obj])

        list_obj = [1, 2, 3]
        self.assertEqual(utils.as_list(list_obj), list_obj)


    def test_get_kwarg_names(self):

        def func1():
            pass    
        self.assertEqual(utils.get_kwarg_names(func1), [])

        def func2(key1):
            pass    
        self.assertEqual(utils.get_kwarg_names(func2), ['key1'])

        def func3(key1, key2=2):
            pass    
        self.assertEqual(utils.get_kwarg_names(func3), ['key1', 'key2'])

        def func4(key1, *argv, key2=2):
            pass    
        self.assertEqual(utils.get_kwarg_names(func4), ['key2'])

        def func5(*argv, key1, key2=2):
            pass    
        self.assertEqual(utils.get_kwarg_names(func5), ['key1', 'key2'])
        
        def func6(key1, key2, key3, *argv):
            pass    
        self.assertEqual(utils.get_kwarg_names(func6), [])

        def func7(key1, key2=1, key3=3, **kwargs):
            pass
        self.assertEqual(utils.get_kwarg_names(func7), ['key1', 'key2', 'key3'])



if __name__ == '__main__':
    unittest.main()