import allure
from requests import Response
from restclient.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code
from dm_api_account.models import *


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(
            self,
            json: Registration,
            expected_status_code: int = 201,
            **kwargs
    ) -> Response:
        """
        Register new user
        :param expected_status_code:
        :param json: registration_model
        :return:
        """
        with allure.step("New user registration"):
            response = self.client.post(
                path="/v1/account",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            expected_status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Reset registered user password
        :param expected_status_code:
        :param json: reset_password_model
        :return:
        """
        with allure.step("User password reset"):
            response = self.client.post(
                path="/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 201:
            return UserEnvelope(**response.json())

        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            expected_status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user email
        :param expected_status_code:
        :param json: change_email_model
        :return:
        """
        with allure.step("Change user email"):
            response = self.client.put(
                path="/v1/account/email",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            expected_status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Change registered user password
        :param expected_status_code:
        :param json: change_password_model
        :return:
        """
        with allure.step("Change user password"):
            response = self.client.put(
                path="/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            expected_status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        Activate registered user
        :param expected_status_code:
        :param token: str
        :return:
        """
        with allure.step("Activate user"):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(
            self,
            expected_status_code: int = 200,
            **kwargs
    ) -> UserDetailsEnvelope | Response:
        """
        Get current user
        :param expected_status_code:
        :return:
        """
        with allure.step("Get user details"):
            response = self.client.get(
                path="/v1/account",
                **kwargs
            )

        validate_status_code(response, expected_status_code)
        if response.status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response
