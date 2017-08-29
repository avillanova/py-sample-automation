# -*- coding: utf-8 -*-
import unittest
import pytest
import sys
sys.path.append("python/poms/Login")
import loginPom

lg = loginPom

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
       lg.start()

    @classmethod
    def tearDownClass(cls):
        lg.finish()

    def test_01_MakeALogin(self):
        lg.screenShot(self._testMethodName)
        self.assertIn("Python", lg.getTitle())
        self.assertNotEqual("Java", lg.getTitle())

    def test_02_MakeALogout(self):
        lg.screenShot(self._testMethodName)
        self.assertTrue('FOsO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_03_TryOtherPass(self):
        lg.screenShot(self._testMethodName)
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
