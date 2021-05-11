import pytest
from application import models
from application.extensions import db
from application.models import User

def test_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    user = User(email = 'dhruv4218@gmail.com',password = '123',fname = 'Dhruv', lname = 'parmar',role_id = 2,contact = '7459642618')
    assert user.email == 'dhruv4218@gmail.com'
    assert user.password == '123'
    assert user.fname == 'Dhruv'
    assert  user.lname == 'parmar'
    assert user.role_id == 2
    assert user.contact == '7459642618'


