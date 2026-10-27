import pytest
import requests

@pytest.mark.api
def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts",params={"userId":1})
    print("URL:", response.url)
    print("Status Code:", response.status_code)
    assert response.status_code == 200
    data = response.json()
    print("Number of posts: ", len(data))
    assert len(data) > 0
    for post in data:
        assert post["userId"] == 1

def test_create_post():
    payload = {"title": "Playwright Automation",
        "body": "API testing with Python and Pytest",
        "userId": 1}
    response = requests.post("https://jsonplaceholder.typicode.com/posts/",json=payload)
    print("Status Code", response.status_code)
    print("Response Body", response.json())
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Playwright Automation"
    assert data["userId"] == 1

def test_get_with_headers():
    headers = {"Accept": "application/json"}
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body", response.json())
    print('Response Headers:', response.headers)
    assert response.status_code == 200