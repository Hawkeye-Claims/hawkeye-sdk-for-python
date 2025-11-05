from .base import BaseModule
from ..types import DocType

class DocfilesModule(BaseModule):
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
