from typing import Optional
import httpx
from ..types import Claim, ApiResponse
from ..utils import type_claim
from .base import BaseModule

class ClaimsModule(BaseModule):
    def get_claims(self, include_inactive: bool = False) -> list[Claim]:
        response = self._client.get(
                url=f"/getclaims/all/{str(include_inactive).lower()}",
                )
        
        portal_json = response.json()

        self._check_response(response)

        claim_list = [type_claim(claim) for claim in portal_json]

        return claim_list
    
    def get_single_claim(self, filenumber: int) -> Claim:
        response = self._client.get(
                url=f"/getclaims/{filenumber}",
                )
        portal_json = response.json()

        self._check_response(response)

        if not portal_json:
            raise ValueError(f"Claim with filenumber {filenumber} not found.")

        return type_claim(portal_json[0])
    
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
        
        response = self._client.post(
                url="/create_claim",
                json=data
                )

        self._check_response(response)

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
        
        response = self._client.post(
                url="/update_claim",
                json=data
               )

        self._check_response(response)

        response_json: ApiResponse = response.json()
        return response_json
