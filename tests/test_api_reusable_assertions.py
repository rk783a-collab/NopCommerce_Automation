from utils.api_client import APIClient


def test_get_post_with_reusable_assertions():

    client = APIClient()

    response = client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    client.assert_status(response, 200)

    data = client.get_json(response)

    print("Response:", data)

    client.assert_json_value(
        response,
        "id",
        1
    )