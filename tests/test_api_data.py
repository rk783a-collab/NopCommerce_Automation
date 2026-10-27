import pytest

from utils.api_client import APIClient
from utils.test_data import PostData

@pytest.mark.api
def test_create_post():
    client = APIClient()
    payload = PostData.create_post()
    response = client.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=payload,
        headers={
            "Content-Type": "application/json"
        }
    )

    print("Payload:", payload)
    print("Response:", response.json())
    client.assert_status(response, 201)
    data = client.get_json(response)
    print("Response JSON:", data)
    print("Response Keys:", data.keys())
    client.assert_json_value(response,"title","Playwright Automation")
    client.assert_json_value(response,"userId",1)