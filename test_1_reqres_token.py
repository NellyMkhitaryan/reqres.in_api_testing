import pytest
import requests
import allure


@allure.feature('User Data Management')
@allure.suite('Registration API Tests')
@allure.title('Test Successful User Registration')
@allure.description('This test verifies that a user can register successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email, password, expected_token", [
    ("eve.holt@reqres.in", "pistol", "QpwL5tke4Pnpja7X4")
])
def test_register_user(email, password, expected_token):
    url = "https://reqres.in/api/register"
    payload = {
        "email": email,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send POST request to register user"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 200"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response contains the token"):
        response_data = response.json()
        print(response_data)
        assert "token" in response_data, "Token not found in the response"
        assert response_data[
                   "token"] == expected_token, f"Expected token '{expected_token}', but got {response_data['token']}"


@allure.feature('User Data Management')
@allure.suite('Registration API Tests')
@allure.title('Test Unsuccessful User Registration')
@allure.description('This test verifies that a user registration fails when the password is missing.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email, expected_error", [
    ("sydney@fife", "Missing password")
])
def test_register_user_unsuccessful(email, expected_error):
    url = "https://reqres.in/api/register"
    payload = {
        "email": email
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send POST request to register user with missing password"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 400"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    with allure.step("Verify the response contains the error message"):
        response_data = response.json()
        print(response_data)
        assert "error" in response_data, "Error message not found in the response"
        assert response_data[
                   "error"] == expected_error, f"Expected error '{expected_error}', but got {response_data['error']}"
