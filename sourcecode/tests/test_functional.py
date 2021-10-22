import random
from flask import Flask, request
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# def test_login(app, client):
#     page = client.post('/login', data=dict(
#         email="cmbaumann@crimson.ua.edu",
#         password="password"
#     ), follow_redirects=True)
#     assert b'Hello' in page.data

# def test_register(app, client):
#     num = random.randint(0, 10000000000)
#     email_string = str(num) + "@crimson.ua.edu"
#     page = client.post('/register', data=dict(
#         firstname="Test",
#         lastname="Case",
#         email=email_string,
#         password1="password",
#         password2="password",
#         major="Chemical Engineering"
#     ), follow_redirects=True)
#     assert b"Hello You have Logged in as" in page.data

# def test_register_fail(app, client):
#     page = client.post('/register', data=dict(
#         firstname="",
#         lastname="",
#         email="",
#         password1="",
#         password2="",
#         major="Chemical Engineering"
#     ), follow_redirects=True)
#     assert b'Please enter your first name' in page.data

# def test_logout(app, client):
#         client.post('/login', data=dict(
#         email="flowcharttest@crimson.ua.edu",
#         password="password"
#     ), follow_redirects=True)
#         page = client.post('/logout', follow_redirects=True)
#         assert b'You are signed out!' in page.data

# def test_flowchart_name_fail(app, client):
#     client.post('/login', data=dict(
#         email="flowcharttest@crimson.ua.edu",
#         password="password"
#     ), follow_redirects=True)
#     page = client.post('/flowchart', data=dict(
#         flowchartname="test"
#     ))
#     assert b'You already have a flowchart named test' in page.data

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