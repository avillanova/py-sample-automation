# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(os.getcwd()+"/resources/webdrivers/chromedriver")

def start():
	print "################ Start Teste 1 #################"
	driver.get("http://www.python.org")
        driver.implicitly_wait(10)

def getTitle():
    element = driver.find_element_by_id("homepage")
    return element.text

def finish():
    print "################ Finish Teste 1 #################"
    driver.quit()

def screenShot(methodName):
    caminho = os.getcwd()+"/resources/files/output/"+methodName+".png"
    #print "ScreenShot em:"+caminho
    driver.save_screenshot(caminho)
