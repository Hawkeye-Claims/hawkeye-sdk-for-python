import httpx

from .base import BaseModule
from ..types import DocType

class DocfilesModule(BaseModule):
    def __init__(self, client: httpx.Client):
        self._client = client

    def upload_file(
            self,
            filenumber: int,
            fileurl: str,
            category: DocType = DocType.DEFAULT,
            visibleToClient: bool = False,
            notes: str = ""
            ):
        response = self._client.post(
                url="/savefile",
                json={
                    "filenumber": filenumber,
                    "link": fileurl,
                    "category": category.value,
                    "visibleToClient": visibleToClient,
                    "notes": notes
                    }
                )

        self._check_response(response)


        return
