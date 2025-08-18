from typing import Optional
from ..types import ClientSettings, DocType
import requests

class DocfilesModule:
    def __init__(self, client: ClientSettings):
        self.client = client

    def upload_file(
            self,
            filenumber: int,
            fileurl: str,
            category: Optional[DocType] = DocType.DEFAULT,
            visibleToClient: Optional[bool] = False,
            notes: Optional[str] = ""
            ):
        requests.post(
            url=f"{self.client.base_url}/savefile",
            headers=self.client.headers,
            data = {
                "filenumber": filenumber,
                "link": fileurl,
                "category": category,
                "visibleToClient": visibleToClient,
                "notes": notes
            }
        )
        return