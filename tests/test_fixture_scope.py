import pytest
@pytest.fixture(scope="class")
def class_fixture():
    print("\n Class Setup")
    yield
    print("\n Class Teardown")

class TestLogin:
    def test_login_valid(self, class_fixture):
        print("\n Valid Login")
    def test_login_invalid(self, class_fixture):
        print("\n Invalid Login")

# @pytest.fixture(scope="module")
# def module_fixture():
#     print("\n Module Setup")
#     yield
#     print("\n Module teardown")
#
# def test_one(module_fixture):
#     print("\n Test one")
# def test_two(module_fixture):
#     print("\n Test two")