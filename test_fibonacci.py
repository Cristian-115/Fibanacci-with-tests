import unittest
import pytest
import fibonacci

class TestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fibonacci.Fibonacci(9), 34)
    def test_fib2(self):
        self.assertEqual(fibonacci.Fibonacci(0), 0)
       
    def test_fib3(self):
        with self.assertRaises(Exception):
                fibonacci.Fibonacci(-1),
       

if __name__ == '__main__':
    unittest.main()

def test_fibb1():
    assert fibonacci.Fibonacci(0) == 0 

def test_fibb2():
    assert fibonacci.Fibonacci(2) == 1

def test_fibb3():
    with pytest.raises(Exception):
         fibonacci.Fibonacci(-1),
           
