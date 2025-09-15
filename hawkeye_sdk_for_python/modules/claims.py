from typing import Optional
from ..types import Claim, ClientSettings, ApiResponse
from ..utils import type_claim
import requests
import json

class ClaimsModule:
    def __init__(self, client: ClientSettings):
        self.client = client

    def get_claims(self, include_inactive: bool = False) -> list[Claim]:
        response = requests.get(
            url=f"{self.client.base_url}/getclaims/all/{include_inactive}",
            headers=self.client.headers
        )
        response.raise_for_status()
        portal_json = response.json()
        claim_list = []
        for file in portal_json:
            claim = type_claim(file)
            claim_list.append(claim)
        return claim_list
    
    def get_single_claim(self, filenumber: int) -> Claim:
        response = requests.get(
            url=f"{self.client.base_url}/getclaims/{filenumber}",
            headers=self.client.headers
        )
        response.raise_for_status()
        portal_json = response.json()[0]
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
            vehunitnumber: Optional[str]=None
    ) -> ApiResponse:
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        
        session = requests.Session()
        req = requests.Request(
            method="POST",
            url=f"{self.client.base_url}/createclaim",
            headers=self.client.headers,
            json=data
        )
        prepared = req.prepare()
        
        response = session.send(prepared)
        response.raise_for_status()
        response_json: ApiResponse = response.json()
        return response_json
    
    def update_claim(
            self,
            filenumber: int,
            clientclaimno: Optional[str]=None,
            claimnumber: Optional[str]=None,
            note: Optional[str]=None,
            rentername: Optional[str]=None,
            insurancecompany: Optional[str]=None,
            insuredname: Optional[str]=None,
            policynumber: Optional[str]=None,
            renterphone: Optional[str]=None,
            renteremail: Optional[str]=None,
            dateofloss: Optional[str]=None,
            vehlocationdetails: Optional[str]=None,
            vehlocationcity: Optional[str]=None,
            vehlocationstate: Optional[str]=None,
            vehyear: Optional[int]=None,
            vehmake: Optional[str]=None,
            vehmodel: Optional[str]=None,
            vehedition: Optional[str]=None,
            vehcolor: Optional[str]=None,
            vehvin: Optional[str]=None,
            vehplatenumber: Optional[str]=None,
            vehunitnumber: Optional[str]=None
    ) -> ApiResponse:
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        
        session = requests.Session()
        req = requests.Request(
            method="POST",
            url=f"{self.client.base_url}/updateclaim",
            headers=self.client.headers,
            json=data
        )
        prepared = req.prepare()
        
        response = session.send(prepared)
        response.raise_for_status()
        response_json: ApiResponse = response.json()
        return response_json
