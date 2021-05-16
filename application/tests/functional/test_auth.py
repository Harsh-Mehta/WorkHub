from application import models

def test_valid_login_logout(test_client, init_database):
    response = test_client.post('/login',
                                data=dict(email='abc@gmail.com', password='123'),
                                follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


def test_login(test_client, init_database):
    response = test_client.post('/login',
                                data=dict(email='abc@gmail.com', password='123'),
                                follow_redirects=True)
    assert response.status_code == 200

def test_logout(test_client, init_database):
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200



