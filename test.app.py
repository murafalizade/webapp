from app import app
def test_home():
    client = app.test_client()
    response = client.get(’/’) 
    assert response.status_code == 200
    assert response.data == b’Hello, World!’

def test_greet():
    client = app.test_client()
    response = client.get(’/greet/John’)
    assert response.status_code == 200
    assert b’Hello, John!’ in response.data
