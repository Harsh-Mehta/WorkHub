import pytest
from application import init_app
from application.extensions import db
from application.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(email = 'dhruv4218@gmail.com',password = '123',fname = 'Dhruv', lname = 'parmar',role_id = 2,contact = '7459642618')
    return user

@pytest.fixture(scope='module')
def test_client():
    flask_app = init_app()
    flask_app.config.from_object('config.Config')
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client  # this is where the testing happens!
    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
    # Insert user data
    user1 = User(email = 'abc@gmail.com',password = '123',fname = 'Rj', lname = 'parmar',role_id = 2,contact = '324235346')
    db.session.add(user1)
    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
