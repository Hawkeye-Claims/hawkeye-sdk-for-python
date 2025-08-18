from typing import Optional
from ..types import ClientSettings, ApiResponse
from datetime import datetime
import requests
import json

class LogtrailsModule:
    def __init__(self, client: ClientSettings):
        self.client = client

    def create_log_trail(
            self, 
            file_number: int,
            activity: str,
            date: Optional[str] = datetime.now().strftime("%m/%d/%Y")
            ) -> ApiResponse:
        response = requests.post(
            url=f"{self.client.base_url}/createLogTrailEntry",
            headers=self.client.headers,
            json={
                "file_number": file_number,
                "date": date,
                "activity": activity
            }
        )
        response_json: ApiResponse = json.loads(response.text)
        return response_json 