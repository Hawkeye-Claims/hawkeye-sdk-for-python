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
        """
        Uploads a document to a specific filenumber with the given details.
        Args:
            filenumber (int): The filenumber to associate the file with.
            fileurl (str): The URL of the file to be uploaded.
            category (DocType, optional): The category of the document. Defaults to DocType.DEFAULT.
            visibleToClient (bool, optional): Whether the file should be visible to the client. Defaults to False.
            notes (str, optional): Additional notes about the file. Defaults to an empty string.
        Returns:
            None
        """
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
