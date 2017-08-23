# coding: latin-1
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import FS

sys.path.append("TC01Test")
print(sys.path)
from TC01Test import TC01Test

TC01 = TC01Test()
print TC01.printTest("TESTE")


driver = FS.criaDriver("chrome", "C:/users/alex.villanova.ext/driver/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
dir = "C:\Users\alex.villanova.ext\Documents\develop\Projeto1Teste"
FS.geraEvidencia(driver, dir)
print "Geraria Evidencia"
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


driver.close()
