def test_home_page(test_client):

    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(email='dhruv4218@gmail.com', password='123'),
                                follow_redirects=True)
    assert response.status_code == 200


    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


