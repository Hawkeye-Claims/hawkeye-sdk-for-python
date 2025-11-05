import unittest
from unittest.mock import patch, Mock
import json

from hawkeye_sdk_for_python import HawkeyeClient, InsCompany


class TestInsCompaniesModule(unittest.TestCase):
    def setUp(self):
        """Set up test client for each test case."""
        self.client = HawkeyeClient("test-auth-token")

    @patch('httpx.Client.get')
    def test_get_all_insurance_companies(self, mock_get):
        """Test retrieving all insurance companies without a search query."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "data": [
                {"id": 1, "name": "State Farm Insurance"},
                {"id": 2, "name": "Allstate Insurance Company"},
                {"id": 3, "name": "GEICO"},
                {"id": 4, "name": "Progressive Insurance"},
                {"id": 5, "name": "Liberty Mutual Insurance"}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method
        companies = self.client.inscompanies.get_insurance_companies()

        # Verify the request
        mock_get.assert_called_once_with("/inscompanies")
        
        # Verify the response
        self.assertIsInstance(companies, list)
        self.assertEqual(len(companies), 5)
        self.assertIsInstance(companies[0], InsCompany)
        self.assertEqual(companies[0].id, 1)
        self.assertEqual(companies[0].name, "State Farm Insurance")

    @patch('httpx.Client.get')
    def test_get_insurance_companies_with_query(self, mock_get):
        """Test searching for insurance companies with a query string."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "State Farm Insurance", "probability": 95},
                {"id": 2, "name": "Farmers Insurance", "probability": 88},
                {"id": 3, "name": "Farm Bureau Insurance", "probability": 75}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method
        companies = self.client.inscompanies.get_insurance_companies(query="farm")

        # Verify the request
        mock_get.assert_called_once_with("/inscompanies?q=farm&limit=5")
        
        # Verify the response
        self.assertIsInstance(companies, list)
        self.assertEqual(len(companies), 3)
        self.assertIsInstance(companies[0], InsCompany)
        self.assertEqual(companies[0].name, "State Farm Insurance")
        self.assertEqual(companies[0].probability, 95)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_with_custom_limit(self, mock_get):
        """Test retrieving insurance companies with a custom limit."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "Progressive Insurance", "probability": 98},
                {"id": 2, "name": "Progressive Casualty Insurance", "probability": 92},
                {"id": 3, "name": "Progressive Direct Insurance", "probability": 85},
                {"id": 4, "name": "Progressive County Mutual Insurance", "probability": 80},
                {"id": 5, "name": "Progressive Mountain Insurance", "probability": 75},
                {"id": 6, "name": "Progressive Preferred Insurance", "probability": 70},
                {"id": 7, "name": "Progressive Commercial", "probability": 68},
                {"id": 8, "name": "Progressive Advantage Insurance", "probability": 65},
                {"id": 9, "name": "Progressive Select Insurance", "probability": 62},
                {"id": 10, "name": "Progressive Universal Insurance", "probability": 60}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method with custom limit
        companies = self.client.inscompanies.get_insurance_companies(
            query="progressive",
            limit=10
        )

        # Verify the request
        mock_get.assert_called_once_with("/inscompanies?q=progressive&limit=10")
        
        # Verify the response
        self.assertEqual(len(companies), 10)
        self.assertIsInstance(companies[0], InsCompany)
        self.assertEqual(companies[0].probability, 98)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_max_limit(self, mock_get):
        """Test that limit is capped at maximum of 20."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {"suggestions": []}
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method with limit > 20
        self.client.inscompanies.get_insurance_companies(
            query="insurance",
            limit=50
        )

        # Verify the limit was capped at 20
        mock_get.assert_called_once_with("/inscompanies?q=insurance&limit=20")

    @patch('httpx.Client.get')
    def test_get_insurance_companies_empty_query(self, mock_get):
        """Test that empty query string is treated as no query."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "data": [
                {"id": 1, "name": "Test Insurance"}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method with empty query
        companies = self.client.inscompanies.get_insurance_companies(query="")

        # Verify no query parameters were added
        mock_get.assert_called_once_with("/inscompanies")

    @patch('httpx.Client.get')
    def test_get_insurance_companies_no_results(self, mock_get):
        """Test handling of no search results."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {"suggestions": []}
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method
        companies = self.client.inscompanies.get_insurance_companies(
            query="nonexistentinsurance"
        )

        # Verify empty list is returned
        self.assertIsInstance(companies, list)
        self.assertEqual(len(companies), 0)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_special_characters(self, mock_get):
        """Test searching with special characters in query."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "A&B Insurance Co.", "probability": 90}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method with special characters
        companies = self.client.inscompanies.get_insurance_companies(query="A&B")

        # Verify the request was made
        mock_get.assert_called_once_with("/inscompanies?q=A&B&limit=5")
        self.assertEqual(len(companies), 1)
        self.assertEqual(companies[0].name, "A&B Insurance Co.")

    @patch('httpx.Client.get')
    def test_get_insurance_companies_partial_match(self, mock_get):
        """Test fuzzy matching with partial company names."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "American Family Insurance", "probability": 85},
                {"id": 2, "name": "American National Insurance", "probability": 82},
                {"id": 3, "name": "American Modern Insurance", "probability": 78}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method with partial name
        companies = self.client.inscompanies.get_insurance_companies(query="american")

        # Verify fuzzy matching results
        self.assertEqual(len(companies), 3)
        # Verify results are ordered by probability
        self.assertIsNotNone(companies[0].probability)
        self.assertIsNotNone(companies[1].probability)
        self.assertIsNotNone(companies[2].probability)
        self.assertGreater(companies[0].probability or 0, companies[1].probability or 0)
        self.assertGreater(companies[1].probability or 0, companies[2].probability or 0)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_network_error(self, mock_get):
        """Test handling of network errors."""
        mock_get.side_effect = Exception("Network connection failed")

        # Verify that the exception is raised
        with self.assertRaises(Exception) as context:
            self.client.inscompanies.get_insurance_companies()
        
        self.assertIn("Network connection failed", str(context.exception))

    @patch('httpx.Client.get')
    def test_get_insurance_companies_without_probability(self, mock_get):
        """Test handling companies returned without probability scores."""
        # Setup mock response (data response doesn't have probability)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "data": [
                {"id": 1, "name": "Test Insurance"},
                {"id": 2, "name": "Example Insurance"}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call the method
        companies = self.client.inscompanies.get_insurance_companies()

        # Verify probability is None for non-search results
        self.assertEqual(len(companies), 2)
        self.assertIsNone(companies[0].probability)
        self.assertIsNone(companies[1].probability)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_case_insensitive(self, mock_get):
        """Test that search is case insensitive."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "GEICO", "probability": 95},
                {"id": 2, "name": "Geico Casualty", "probability": 88}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call with lowercase query
        companies = self.client.inscompanies.get_insurance_companies(query="geico")

        # Verify results returned
        self.assertEqual(len(companies), 2)
        self.assertEqual(companies[0].name, "GEICO")

    @patch('httpx.Client.get')
    def test_get_insurance_companies_minimum_limit(self, mock_get):
        """Test with minimum limit of 1."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "suggestions": [
                {"id": 1, "name": "Liberty Mutual", "probability": 99}
            ]
        }
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call with limit of 1
        companies = self.client.inscompanies.get_insurance_companies(
            query="liberty",
            limit=1
        )

        # Verify request
        mock_get.assert_called_once_with("/inscompanies?q=liberty&limit=1")
        self.assertEqual(len(companies), 1)

    @patch('httpx.Client.get')
    def test_get_insurance_companies_default_limit(self, mock_get):
        """Test that default limit is 5."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {"suggestions": []}
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        # Call without specifying limit
        companies = self.client.inscompanies.get_insurance_companies(query="test")

        # Verify default limit of 5
        mock_get.assert_called_once_with("/inscompanies?q=test&limit=5")


if __name__ == "__main__":
    unittest.main()
