from .types import ClientSettings
from .constants import BASE_URL, DEV_BASE_URL
from .modules import ClaimsModule, DocfilesModule, LogtrailsModule

BASE_HEADERS = {
    "Content-Type": "application/json",
}

class HawkeyeClient:
    def __init__(self, auth_token: str, debug_mode: bool = False):
        base_url = DEV_BASE_URL if debug_mode else BASE_URL
        headers = {**BASE_HEADERS, "Authorization": f"Bearer {auth_token}"}
        
        self.settings = ClientSettings(
            auth_token=auth_token,
            dev_env=debug_mode,
            base_url=base_url,
            headers=headers
        )
        self.claims = ClaimsModule(self.settings)
        self.docfiles = DocfilesModule(self.settings)
        self.logtrails = LogtrailsModule(self.settings)