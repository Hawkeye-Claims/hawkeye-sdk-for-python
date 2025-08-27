from ..types import ClientSettings, DocType
import requests

class DocfilesModule:
    def __init__(self, client: ClientSettings):
        self.client = client

    def upload_file(
            self,
            filenumber: int,
            fileurl: str,
            category: DocType = DocType.DEFAULT,
            visibleToClient: bool = False,
            notes: str = ""
            ):
        response = requests.post(
            url=f"{self.client.base_url}/savefile",
            headers=self.client.headers,
            json = {
                "filenumber": filenumber,
                "link": fileurl,
                "category": category.value,
                "visibleToClient": visibleToClient,
                "notes": notes
            }
        )
        return