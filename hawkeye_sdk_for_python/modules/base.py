import httpx
from ..exceptions import APIError, APIResourceNotFoundError

class BaseModule:
    def __init__(self, client: httpx.Client):
        self._client = client

    def _check_response(self, response: httpx.Response):
        if response.is_error:
            try:
                error_details = response.json()
            except httpx.ReadError:
                error_details = {"message": "No response body provided."}

            if response.status_code == 404:
                raise APIResourceNotFoundError(
                    message=f"Resource not found: {response.url}. Details: {error_details.get('message', 'No additional information provided.')}",
                    response=error_details
                )

            raise APIError(
                message=f"API request failed with status {response.status_code}: {response.url}. Details: {error_details.get('message', 'No additional information provided.')}",
                status_code=response.status_code,
                response=error_details
                    )
