import httpx
from .types import ClientSettings
from .constants import BASE_URL, DEV_BASE_URL
from .modules import ClaimsModule, DocfilesModule, LogtrailsModule, InsCompaniesModule


class HawkeyeClient:
    def __init__(self, auth_token: str, debug_mode: bool = False):
        """
        Initializes the Hawkeye API client with the provided authentication token and debug mode setting.
        Args:
            auth_token (str): The authentication token for API access.
            debug_mode (bool, optional): If True, uses the development environment. Defaults to False.
        """
        base_url = DEV_BASE_URL if debug_mode else BASE_URL
        headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {auth_token}",
                }
        
        self.settings = ClientSettings(
            auth_token=auth_token,
            dev_env=debug_mode,
            base_url=base_url,
        )
        self._http_client = httpx.Client(
                base_url=base_url,
                headers=headers,
                timeout=60.0,
                )
        self.claims = ClaimsModule(self._http_client)
        self.docfiles = DocfilesModule(self._http_client)
        self.logtrails = LogtrailsModule(self._http_client)
        self.inscompanies = InsCompaniesModule(self._http_client)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            self._http_client.close()

        def close(self):
            self._http_client.close()
