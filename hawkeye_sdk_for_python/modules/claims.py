from typing import Optional
from ..types import Claim, ClientSettings, ApiResponse
from ..utils import type_claim
import requests
import json

class ClaimsModule:
    def __init__(self, client: ClientSettings):
        self.client = client

    def get_claims(self, include_inactive: bool = False) -> list[Claim]:
        query = requests.get(
            url=f"{self.client.base_url}/getclaims/all/{include_inactive}",
            headers=self.client.headers
        )
        portal_json = json.loads(query.text)
        claim_list = []
        for file in portal_json:
            claim = type_claim(file)
            claim_list.append(claim)
        return claim_list
    
    def get_single_claim(self, filenumber: int) -> Claim:
        query = requests.get(
            url=f"{self.client.base_url}/getclaims/{filenumber}",
            headers=self.client.headers
        )
        portal_json = json.loads(query.text)[0]
        return type_claim(portal_json)
    
    def create_claim(
            self,
            rentername: str,
            insurancecompany: str,
            dateofloss: str,
            vehmake: str,
            vehmodel: str,
            vehcolor: str,
            vehvin: str,
            clientclaimno: Optional[str]=None,
            claimnumber: Optional[str]=None,
            note: Optional[str]=None,
            insuredname: Optional[str]=None,
            policynumber: Optional[str]=None,
            renterphone: Optional[str]=None,
            renteremail: Optional[str]=None,
            vehlocationdetails: Optional[str]=None,
            vehlocationcity: Optional[str]=None,
            vehlocationstate: Optional[str]=None,
            vehyear: Optional[int]=None,
            vehedition: Optional[str]=None,
            vehplatenumber: Optional[str]=None,
            vehuninumber: Optional[str]=None
    ) -> ApiResponse :
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        response = requests.post(
            url=f"{self.client.base_url}/createclaim",
            headers=self.client.headers,
            data=data
        )
        response_json: ApiResponse = json.loads(response.text)
        return response_json
    
    def update_claim(
            self,
            filenumber: int,
            clientclaimno: Optional[str],
            claimnumber: Optional[str],
            note: Optional[str],
            rentername: Optional[str],
            insurancecompany: Optional[str],
            insuredname: Optional[str],
            policynumber: Optional[str],
            renterphone: Optional[str],
            renteremail: Optional[str],
            dateofloss: Optional[str],
            vehlocationdetails: Optional[str],
            vehlocationcity: Optional[str],
            vehlocationstate: Optional[str],
            vehyear: Optional[int],
            vehmake: Optional[str],
            vehmodel: Optional[str],
            vehedition: Optional[str],
            vehcolor: Optional[str],
            vehvin: Optional[str],
            vehplatenumber: Optional[str],
            vehuninumber: Optional[str]
    ) -> ApiResponse:
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        response = requests.put(
            url=f"{self.client.base_url}/updateclaim",
            headers=self.client.headers,
            data=data
        )
        response_json: ApiResponse = json.loads(response.text)
        return response_json