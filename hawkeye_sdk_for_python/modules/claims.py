from typing import Optional
from ..types import Claim, ApiResponse
from ..utils import type_claim
from .base import BaseModule

class ClaimsModule(BaseModule):
    def get_claims(self, include_inactive: bool = False) -> list[Claim]:
        """
        Retrieves a list of active (or all) claims. By default, only active claims are returned.
        Args:
            include_inactive (bool): If True, includes inactive claims in the results. Defaults to False.
        Returns:
            list[Claim]: A list of Claim objects.
        """
        response = self._client.get(
                url=f"/getclaims/all/{str(include_inactive).lower()}",
                )
        
        portal_json = response.json()

        self._check_response(response)

        claim_list = [type_claim(claim) for claim in portal_json]

        return claim_list
    
    def get_single_claim(self, filenumber: int) -> Claim:
        """
        Retrieves a single claim by its filenumber.
        Args:
            filenumber (int): The filenumber of the claim to retrieve.
        Returns:
            Claim: A Claim object.
        """
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
            inscompaniesid: str,
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
        """
        Creates a new claim with the provided details.
        Args:
            rentername (str): Name of the renter.
            inscompaniesid (str): ID of the insurance company.
            dateofloss (str): Date of loss.
            vehmake (str): Vehicle make.
            vehmodel (str): Vehicle model.
            vehcolor (str): Vehicle color.
            vehvin (str): Vehicle VIN.
            clientclaimno (Optional[str]): Client claim number.
            claimnumber (Optional[str]): Claim number.
            note (Optional[str]): Additional notes.
            insuredname (Optional[str]): Name of the insured.
            policynumber (Optional[str]): Policy number.
            renterphone (Optional[str]): Renter's phone number.
            renteremail (Optional[str]): Renter's email address.
            vehlocationdetails (Optional[str]): Vehicle location details.
            vehlocationcity (Optional[str]): Vehicle location city.
            vehlocationstate (Optional[str]): Vehicle location state.
            vehyear (Optional[int]): Vehicle year.
            vehedition (Optional[str]): Vehicle edition.
            vehplatenumber (Optional[str]): Vehicle plate number.
            vehunitnumber (Optional[str]): Vehicle unit number.
        Returns:
            ApiResponse: Response from the API indicating success or failure.
        """
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        
        response = self._client.post(
                url="/createclaim",
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
            inscompaniesid: Optional[str]=None,
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
        """
        Updates an existing claim with the provided details.
        Args:
            filenumber (int): Filenumber of the claim to update.
            clientclaimno (Optional[str]): Client claim number.
            claimnumber (Optional[str]): Claim number.
            note (Optional[str]): Additional notes.
            rentername (Optional[str]): Name of the renter.
            inscompaniesid (Optional[str]): ID of the insurance company.
            insuredname (Optional[str]): Name of the insured.
            policynumber (Optional[str]): Policy number.
            renterphone (Optional[str]): Renter's phone number.
            renteremail (Optional[str]): Renter's email address.
            dateofloss (Optional[str]): Date of loss.
            vehlocationdetails (Optional[str]): Vehicle location details.
            vehlocationcity (Optional[str]): Vehicle location city.
            vehlocationstate (Optional[str]): Vehicle location state.
            vehyear (Optional[int]): Vehicle year.
            vehmake (Optional[str]): Vehicle make.
            vehmodel (Optional[str]): Vehicle model.
            vehedition (Optional[str]): Vehicle edition.
            vehcolor (Optional[str]): Vehicle color.
            vehvin (Optional[str]): Vehicle VIN.
            vehplatenumber (Optional[str]): Vehicle plate number.
            vehunitnumber (Optional[str]): Vehicle unit number.
        Returns:
            ApiResponse: Response from the API indicating success or failure.
        """
        all_args = locals()
        data = {key: value for key, value in all_args.items() if value is not None and key != "self"}
        
        response = self._client.post(
                url="/updateclaim",
                json=data
               )

        self._check_response(response)

        response_json: ApiResponse = response.json()
        return response_json
