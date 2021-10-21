import random
from flask import Flask, request

def test_login(app, client):
    page = client.post('/login', data=dict(
        email="email@email.com",
        password="password"
    ), follow_redirects=True)
    assert b'You are logged in as' in page.data

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

def test_logout(app, client):
        client.post('/login', data=dict(
        email="flowcharttest@crimson.ua.edu",
        password="password"
    ), follow_redirects=True)
        page = client.post('/logout', follow_redirects=True)
        assert b'You are signed out' in page.data

def test_flowchart_name_fail(app, client):
    client.post('/login', data=dict(
        email="flowcharttest@crimson.ua.edu",
        password="password"
    ), follow_redirects=True)
    page = client.post('/flowchart-new', data=dict(
        flowchartname="test"
    ))
    assert b'You already have a flowchart named test' in page.data

     

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
