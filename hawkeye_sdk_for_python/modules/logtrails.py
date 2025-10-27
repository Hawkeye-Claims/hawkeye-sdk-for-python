import httpx

from .base import BaseModule
from ..types import ApiResponse
from datetime import datetime
import json

class LogtrailsModule(BaseModule):
    def __init__(self, client: httpx.Client):
        self._client = client

    def create_log_trail(
            self, 
            file_number: int,
            activity: str,
            date: str = "" 
            ) -> ApiResponse:
        if date == "":
            date = datetime.now().strftime("%m/%d/%Y")
        response = self._client.post(
                url="/createLogTrailEntry",
                json={
                    "filenumber": file_number,
                    "activity": activity,
                    "date": date
                    }
                )
        self._check_response(response)
        response_json: ApiResponse = json.loads(response.text)
        return response_json 
