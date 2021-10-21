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
        major="Computer Science"
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