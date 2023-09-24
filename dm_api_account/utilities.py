import allure
from pydantic import BaseModel
from requests import Response


def validate_request_json(json: str | BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(exclude_none=True)


def validate_status_code(response: Response, expected_status_code: int):
    with allure.step("Status code validation"):
        assert response.status_code == expected_status_code, (
            f"Unexpected status code! Expected: {expected_status_code}. "
            f"Actual: {response.status_code}")
