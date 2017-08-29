#*-* coding: latin-1 *-*
import setup
setup.setUp()
import unittest
import pytest
import login_test

suite = unittest.TestLoader().loadTestsFromTestCase(login_test.Login)
unittest.TextTestRunner(verbosity=2).run(suite)
