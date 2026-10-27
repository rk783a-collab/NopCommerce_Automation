from utils.api_client import APIClient


def test_get_post():

    client = APIClient()

    response = client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data

def test_create_post():

    client = APIClient()

    payload = {
        "title": "Playwright Automation",
        "body": "API testing with Python and Pytest",
        "userId": 1
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = client.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=payload,
        headers=headers
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Playwright Automation"
    assert data["body"] == "API testing with Python and Pytest"
    assert data["userId"] == 1

def test_update_post():

    client = APIClient()

    payload = {
        "id": 1,
        "title": "Updated Playwright Automation",
        "body": "Updated API testing with Python",
        "userId": 1
    }

    response = client.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        data=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated Playwright Automation"
    assert data["userId"] == 1

def test_delete_post():

    client = APIClient()

    response = client.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    print("Status Code:", response.status_code)

    assert response.status_code == 200

def test_patch_post():

    client = APIClient()

    payload = {
        "title": "Updated Title Only"
    }

    response = client.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        data=payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Updated Title Only"
def test_basic_auth_success():

    client = APIClient()

    response = client.get_with_auth(
        "https://httpbin.org/basic-auth/testuser/testpass",
        "testuser",
        "testpass"
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["authenticated"] is True
    assert data["user"] == "testuser"
def test_basic_auth_failure():

    client = APIClient()

    response = client.get_with_auth(
        "https://httpbin.org/basic-auth/testuser/testpass",
        "wronguser",
        "wrongpass"
    )

    print("Status Code:", response.status_code)

    assert response.status_code == 401
def test_bearer_auth_success():

    client = APIClient()

    response = client.get_with_token(
        "https://httpbin.org/bearer",
        "my-test-token"
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["authenticated"] is True
    assert data["token"] == "my-test-token"
def test_bearer_auth_missing():

    response = requests.get(
        "https://httpbin.org/bearer"
    )

    print("Status Code:", response.status_code)

    assert response.status_code == 401