import requests
import pytest
import allure
from datetime import datetime


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test Update User')
@allure.description('This test verifies that an existing user can be updated successfully.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.parametrize("user_id, name, job", [
    (2, "morpheus", "zion resident")
])
def test_update_user(user_id, name, job):
    url = f"https://reqres.in/api/users/{user_id}"
    payload = {
        "name": name,
        "job": job
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send PUT request to update the user"):
        response = requests.put(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 200"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response contains the updated user data"):
        response_data = response.json()
        print(response_data)
        assert response_data["name"] == name, "User name is incorrect"
        assert response_data["job"] == job, "User job is incorrect"
        assert "updatedAt" in response_data, "UpdatedAt field is missing"

    with allure.step("Verify the 'updatedAt' field is a valid timestamp"):
        try:
            datetime.fromisoformat(response_data["updatedAt"].replace("Z", "+00:00"))
        except ValueError:
            assert False, "UpdatedAt field is not a valid timestamp"
