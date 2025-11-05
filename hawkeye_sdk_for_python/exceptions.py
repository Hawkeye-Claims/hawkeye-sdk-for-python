class HawkeyeSDKError(Exception):
    pass

class APIError(HawkeyeSDKError):
    def __init__(self, message: str, status_code: int = 0, response: dict = {}):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response

class APIResourceNotFoundError(APIError):
    def __init__(self, message: str, response: dict = {}):
        super().__init__(message, status_code=404, response=response)

