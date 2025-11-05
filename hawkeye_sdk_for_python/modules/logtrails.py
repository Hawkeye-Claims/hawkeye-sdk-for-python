from .base import BaseModule
from ..types import ApiResponse
from datetime import datetime
import json

class LogtrailsModule(BaseModule):
    def create_log_trail(
            self, 
            file_number: int,
            activity: str,
            date: str = "" 
            ) -> ApiResponse:
        """
        Creates a status entry for a specific file number with the given activity and date.
        Args:
            file_number (int): The file number to associate the log trail entry with.
            activity (str): The activity description for the log trail entry.
            date (str, optional): The date of the activity in MM/DD/YYYY format. Defaults to the current date if not provided.
        Returns:
            ApiResponse: The API response indicating the success or failure of the operation.
        """
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
