import requests
import pytest
import allure


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test List Users')
@allure.description('This test verifies that the list users API returns the correct user details.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_list_users():
    url = "https://reqres.in/api/users?page=2"
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send GET request to list users"):
        response = requests.get(url, headers=headers)

    with allure.step("Verify the response status code is 200"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response contains the correct user data"):
        response_data = response.json()
        print(response_data)
        assert response_data["page"] == 2, "Page number is incorrect"
        assert response_data["per_page"] == 6, "Per page count is incorrect"
        assert response_data["total"] == 12, "Total count is incorrect"
        assert response_data["total_pages"] == 2, "Total pages count is incorrect"
        assert len(response_data["data"]) == 6, "Number of users in data is incorrect"

        for user in response_data["data"]:
            assert "id" in user, "User ID is missing"
            assert "email" in user, "User email is missing"
            assert "first_name" in user, "User first name is missing"
            assert "last_name" in user, "User last name is missing"
            assert "avatar" in user, "User avatar is missing"

        assert "support" in response_data, "Support info is missing"
        assert "url" in response_data["support"], "Support URL is missing"
        assert "text" in response_data["support"], "Support text is missing"


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test Find Single User')
@allure.description('This test verifies that the API returns the correct details for a single user.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_find_single_user():
    url = "https://reqres.in/api/users/2"
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send GET request to find a single user"):
        response = requests.get(url, headers=headers)

    with allure.step("Verify the response status code is 200"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response contains the correct user details"):
        response_data = response.json()
        print(response_data)

        user_data = response_data["data"]
        assert user_data["id"] == 2, "User ID is incorrect"
        assert user_data["email"] == "janet.weaver@reqres.in", "User email is incorrect"
        assert user_data["first_name"] == "Janet", "User first name is incorrect"
        assert user_data["last_name"] == "Weaver", "User last name is incorrect"
        assert user_data["avatar"] == "https://reqres.in/img/faces/2-image.jpg", "User avatar URL is incorrect"

        support_info = response_data["support"]
        assert "url" in support_info, "Support URL is missing"
        assert "text" in support_info, "Support text is missing"


@allure.feature('User Data Management')
@allure.suite('User API Tests')
@allure.title('Test Find Single User Not Found')
@allure.description('This test verifies that the API returns a 404 status code when the user is not found.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_find_single_user_not_found():
    url = "https://reqres.in/api/users/23"
    headers = {
        "Content-Type": "application/json"
    }

    with allure.step("Send GET request to find a non-existent user"):
        response = requests.get(url, headers=headers)

    with allure.step("Verify the response status code is 404"):
        print(f"Response Status Code: {response.status_code}")
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

    with allure.step("Verify the response body is empty"):
        response_data = response.json()
        print(response_data)
        assert response_data == {}, "Expected an empty response body for a 404 error"
