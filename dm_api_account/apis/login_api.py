import allure
from requests import Response
from dm_api_account.models import *
from restclient.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(
            self,
            json: LoginCredentials,
            expected_status_code: int = 200,
            **kwargs
    ) -> Response:
        """
        Authenticate via credentials
        :param expected_status_code:
        :param json: login_credentials_model
        :return:
        """

        with allure.step("User authorization"):
            response = self.client.post(
                path="/v1/account/login",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        return response

    def delete_v1_account_login(
            self,
            expected_status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout as current user
        :param expected_status_code:
        :return:
        """
        with allure.step("User logout"):
            response = self.client.delete(
                path="/v1/account/login",
                **kwargs
            )

        validate_status_code(response, expected_status_code)

        return response

    def delete_v1_account_login_all(
            self,
            expected_status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout from every device
        :param expected_status_code:
        :return:
        """
        with allure.step("User logout from all devices"):
            response = self.client.delete(
                path="/v1/account/login/all",
                **kwargs
            )

        validate_status_code(response, expected_status_code)

        return response
