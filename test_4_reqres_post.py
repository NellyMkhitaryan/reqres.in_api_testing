import requests
import pytest
import allure
from datetime import datetime


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test Create User')
@allure.description('This test verifies that a new user can be created successfully.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("name, job", [
    ("morpheus", "leader")
])
def test_create_user(name, job):
    url = "https://reqres.in/api/users"
    payload = {
        "name": name,
        "job": job
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send POST request to create a new user"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 201"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    with allure.step("Verify the response contains the correct user data"):
        response_data = response.json()
        print(response_data)
        assert response_data["name"] == name, "User name is incorrect"
        assert response_data["job"] == job, "User job is incorrect"
        assert "id" in response_data, "User ID is missing"
        assert "createdAt" in response_data, "CreatedAt field is missing"

    with allure.step("Verify the 'createdAt' field is a valid timestamp"):
        try:
            datetime.fromisoformat(response_data["createdAt"].replace("Z", "+00:00"))
        except ValueError:
            assert False, "CreatedAt field is not a valid timestamp"
