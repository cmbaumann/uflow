import random
from flask import Flask, request
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_color(app, client):
    driver = webdriver.Chrome("C:\\Users\\cassi\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_add")
    element.click()
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-new?'))
    element = driver.find_element_by_id("inputFlowchartName")
    element.send_keys("testflowchart")
    element = driver.find_element_by_id("taken")
    element.click()
    element = driver.find_element_by_id("1")
    element.click()
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart'))
    element = driver.find_element_by_id("1")
    value = element.value_of_css_property("backgroundColor")
    assert value == "rgba(0, 128, 0, 1)"

def test_delete(app, client):
    driver = webdriver.Chrome("C:\\Users\\cassi\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_delete")
    element.click()
    page = driver.page_source
    print(page)
    if "testflowchart" in page:
        assert False
    else:
        assert True