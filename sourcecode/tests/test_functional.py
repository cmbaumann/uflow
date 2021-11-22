import random
from flask import Flask, request
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# must be the chromedriver file path specific to your machine
chromepath = "/Users/bradywachs/Downloads/chromedriver" 


#1
def test_login(app, client):
    page = client.post('/login', data=dict(
        email="email@email.com",
        password="password"
    ), follow_redirects=True)
    assert b'You are logged in as' in page.data


#2
def test_register(app, client):
    num = random.randint(0, 10000000000)
    email_string = str(num) + "@crimson.ua.edu"
    page = client.post('/register', data=dict(
        firstname="Test",
        lastname="Case",
        email=email_string,
        password1="password",
        password2="password",
        major="Computer Science",
        year="2018"
    ), follow_redirects=True)
    assert b"You are logged in as" in page.data


#3
def test_register_fail(app, client):
    page = client.post('/register', data=dict(
        firstname="",
        lastname="",
        email="",
        password1="",
        password2="",
        major="Chemical Engineering"
    ), follow_redirects=True)
    assert b'Please enter your first name' in page.data


#4
def test_logout(app, client):
        client.post('/login', data=dict(
        email="flowcharttest@crimson.ua.edu",
        password="password"
    ), follow_redirects=True)
        page = client.post('/logout', follow_redirects=True)
        assert b'You are signed out' in page.data


#5
def test_flowchart_name_fail(app, client):
    client.post('/login', data=dict(
        email="flowcharttest@crimson.ua.edu",
        password="password"
    ), follow_redirects=True)
    page = client.post('/flowchart-new', data=dict(
        flowchartname="test"
    ))
    assert b'You already have a flowchart named test' in page.data


#6
def test_future_semesters(app, client):
    client.post('/login', data=dict(
        email="flowcharttest@crimson.ua.edu",
        password="password"
    ), follow_redirects=True)
    page = client.post('/flowchart-edit/test', data=dict(
        name="test",
        d1="taken",
        d2="taken",
        d3="taken",
        d4="taken",
        d5="taken",
        d6="taken",
        d7="taken",
        d8="inprogress",
        d9="inprogress",
        d10="inprogress",
        d11="inprogress",
        d12="inprogress",
        d13="fall1",
        d14="fall1",
        d15="fall1",
        d16="fall1",
        d17="fall2",
        d18="fall2",
        d19="fall2",
        d20="fall2",
        d21="fall2",
        d22="fall2",
        d23="spring3",
        d24="spring3",
        d25="spring3",
        d26="spring3",
        d27="spring3",
        d28="fall3",
        d29="fall3",
        d30="fall3",
        d31="fall3",
        d32="fall3",
        d33="spring4",
        d34="spring4",
        d35="spring4",
        d36="spring4",
        d37="spring4"
    ))
    assert b'Your flowchart has been saved' in page.data


#7
def test_color(app, client):
    driver = webdriver.Chrome(chromepath)
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


#8
def test_deselect(app, client):
    driver = webdriver.Chrome(chromepath)
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_edit")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("taken")
    element.click()
    element = driver.find_element_by_id("2")
    element.click()
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("deselect")
    element.click()
    element = driver.find_element_by_id("2")
    element.click()
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))

    element = driver.find_element_by_id("2")
    value = element.value_of_css_property("backgroundColor")
    assert value == "rgba(255, 255, 255, 1)"


#9
def test_edit_elective(app, client):
    driver = webdriver.Chrome(chromepath)
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_edit")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("7electiveText")
    element.send_keys("MUS 121")
    element = driver.find_element_by_id("7hours")
    element.send_keys("3")
    element = driver.find_element_by_id("7Button")
    element.click()

    element = driver.find_element_by_id("7OutputElective")
    value = element.get_attribute('innerHTML')
    assert value == "MUS 121 (3 hours)"


#10
def test_color_save(app, client):
    driver = webdriver.Chrome(chromepath)
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_edit")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("taken")
    element.click()
    element = driver.find_element_by_id("1")
    element.click()
    element = driver.find_element_by_id("btn-change")
    element.click()
    element = driver.find_element_by_class_name("c-red")
    element.send_keys("0")
    element = driver.find_element_by_id("taken")
    element.click()
    element = driver.find_element_by_id("btn-change")
    element.click()
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("taken")
    element.click()
    value = element.value_of_css_property("backgroundColor")
    assert value == "rgba(0, 0, 0, 1)"


#11
def test_render_elective(app, client):
    """
    Test that the elective information still renders after website is saved
    """
    
    driver = webdriver.Chrome(chromepath)
    driver.get("https://uflow-alabama.herokuapp.com/login")
    element = driver.find_element_by_id("InputEmail")
    element.send_keys("test@crimson.ua.edu")
    element = driver.find_element_by_id("InputPassword")
    element.send_keys("password")
    element = driver.find_element_by_class_name("btn")
    element.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/logged_in'))
    element = driver.find_element_by_class_name("fc_edit")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))
    element = driver.find_element_by_id("7electiveText")
    element.send_keys("MUS 121")
    element = driver.find_element_by_id("7hours")
    element.send_keys("3")
    element = driver.find_element_by_id("7Button")
    element.click()

    # save flowchart to DB
    element = driver.find_element_by_id("saveButton")
    element.click()
    wait.until(EC.url_to_be('https://uflow-alabama.herokuapp.com/flowchart-edit/testflowchart?'))

    # Assert that the information still renders after the save
    element = driver.find_element_by_id("7OutputElective")
    value = element.get_attribute('innerHTML')
    assert value == "MUS 121 (3 hours)"


#15
def test_delete(app, client):
    driver = webdriver.Chrome(chromepath)
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