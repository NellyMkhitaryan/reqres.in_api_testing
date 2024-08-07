import requests
import pytest
import allure


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test Delete User')
@allure.description('This test verifies that an existing user can be deleted successfully.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("user_id", [
    2
])
def test_delete_user(user_id):
    url = f"https://reqres.in/api/users/{user_id}"
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send DELETE request to delete the user"):
        response = requests.delete(url, headers=headers)

    with allure.step("Verify the response status code is 204"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

    with allure.step("Verify the response body is empty for a 204 status code"):
        assert response.text == "", "Response body should be empty for a 204 status code"
