import requests
import pytest
import allure


@allure.feature('User Data Management')
@allure.suite('Login API Tests')
@allure.title('Test Successful User Login')
@allure.description('This test verifies that a user can log in successfully with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email, password, expected_token", [
    ("eve.holt@reqres.in", "cityslicka", "QpwL5tke4Pnpja7X4")
])
def test_login_successful(email, password, expected_token):
    url = "https://reqres.in/api/login"
    payload = {
        "email": email,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send POST request to login user"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 200"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response contains the token"):
        response_data = response.json()
        print(response_data)
        assert "token" in response_data, "Token not found in the response"
        assert response_data["token"] == expected_token, f"Expected token '{expected_token}', but got {response_data['token']}"


@allure.feature('User Data Management')
@allure.suite('Login API Tests')
@allure.title('Test Unsuccessful User Login')
@allure.description('This test verifies that a user login fails when the password is missing.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email, expected_error", [
    ("peter@klaven", "Missing password")
])
def test_login_unsuccessful(email, expected_error):
    url = "https://reqres.in/api/login"
    payload = {
        "email": email
    }
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send POST request to login user with missing password"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Verify the response status code is 400"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    with allure.step("Verify the response contains the error message"):
        response_data = response.json()
        print(response_data)
        assert "error" in response_data, "Error message not found in the response"
        assert response_data["error"] == expected_error, f"Expected error '{expected_error}', but got {response_data['error']}"
