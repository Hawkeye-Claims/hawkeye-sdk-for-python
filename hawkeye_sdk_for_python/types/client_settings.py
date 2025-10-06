from dataclasses import dataclass

@dataclass
class ClientSettings:
    auth_token: str
    dev_env: bool
    base_url: str
