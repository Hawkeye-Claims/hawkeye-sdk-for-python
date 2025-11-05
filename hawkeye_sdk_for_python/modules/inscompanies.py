from ..types import InsCompany
from .base import BaseModule

class InsCompaniesModule(BaseModule):
    def get_insurance_companies(self, query: str = "", limit: int = 5) -> list[InsCompany]:
        """
         Retrieves a list of insurance companies. When no search query is provided, returns all companies.
         When a search query is provided, returns intelligent suggestions with probability scores on fuzzy matching.
         Args:
             query (str): The search query to filter insurance companies by name. If omitted, returns all companies.
             limit (int): The maximum number of suggestions to return. Defaults to 5, maximum is 20.
         Returns:
             list[InsCompany]: A list of InsCompany objects.
         """ 
        MAX_LIMIT = 20
        
        if limit > MAX_LIMIT:
            limit = MAX_LIMIT
        
        url = "/inscompanies"
        
        if query:
            url += f"?q={query}&limit={limit}"
        
        response = self._client.get(url)
        
        portal_json = response.json()

        self._check_response(response)

        ins_companies = [InsCompany(**item) for item in portal_json.get("suggestions", portal_json.get("data", []))]

        return ins_companies
