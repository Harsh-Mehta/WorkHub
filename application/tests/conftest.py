
import pytest
from application import init_app
from application.extensions import db
from application.models import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = init_app()
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
    user1 = User(email='dhruv4218@gmail.com', plaintext_password='123')

    db.session.add(user1)
    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
