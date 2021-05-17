import pytest
from application import models
from application.extensions import db
from application.models import User

def test_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.email == 'dhruv4218@gmail.com'
    assert new_user.password == '123'
    assert new_user.fname == 'Dhruv'
    assert  new_user.lname == 'parmar'
    assert new_user.role_id == 2
    assert new_user.contact == '7459642618'


