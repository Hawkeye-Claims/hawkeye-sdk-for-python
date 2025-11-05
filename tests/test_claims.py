import unittest
from unittest.mock import patch, Mock
import json

from hawkeye_sdk_for_python import HawkeyeClient, Claim, APIError, APIResourceNotFoundError


class TestClaimsModule(unittest.TestCase):
    def setUp(self):
        """Set up test client for each test case."""
        self.client = HawkeyeClient("test-auth-token")
        self.test_filenumber = 12345

    @patch('httpx.Client.get')
    def test_get_claims_success(self, mock_get):
        # Setup mock response with proper attributes
        mock_response = Mock()
        mock_response.status_code = 200
        
        # Anonymized mock data for testing
        mock_data = [
            {
                "filenumber": 24111756,
                "customername": "Test Company - City, ST",
                "clientclaimno": "12345678 (Cross Claim 98765432)",
                "rentername": "John Doe",
                "ranumber": "123456789",
                "insuredname": "John Doe",
                "insurancecompany": "Test Insurance Co.",
                "claimnumber": "1234567890123456789",
                "policynumber": "POL123456",
                "dateofloss": "2024-12-22",
                "adjuster": "Test Adjuster",
                "adjusterphone": "1-800-000-0000",
                "firstparty": True,
                "thirdparty": None,
                "cdw": None,
                "hc_adj": "Test Martinez",
                "officephone": "(555) 123-4567",
                "email": "test@example.com",
                "vin": "1ABCD23E45FG67890",
                "vehyear": 2022,
                "vehmake": "Test",
                "vehmodel": "Model 3500",
                "vehedition": "15 ft. box",
                "color": "White",
                "platenumber": "ST-ABC123",
                "unitnumber": "12345678",
                "inspectiondate": "2024-12-23",
                "estimateamount": 2933.95,
                "totalloss": None,
                "continuedrentalamt": 439.96,
                "dv_amt": 6812.89,
                "liabilityaccepted": "2025-02-19",
                "liabilitydenied": None,
                "settlement_pd": 2092.75,
                "settlement_salvage": None,
                "settlement_cr": 0,
                "settlement_dv": 0,
                "settlement_other": None,
                "settlement_deductable": 0,
                "administrativefee": 0,
                "appraisalfee": 0,
                "datefileclosed": None,
                "settlementoffer": None,
                "supplement": None,
                "settlementtowing": None,
                "settlementstorage": None,
                "demand_admin_fee": 300,
                "demand_appraisal_fee": 65,
                "estimatedate": None,
                "demanddate": None,
                "policystartdate": None,
                "policyenddate": None,
                "vehicleowner": None,
                "docfiles": [
                    {
                        "doctype": "Images",
                        "dateadded": "2024-12-23T18:40:16.435945",
                        "user": "Test User",
                        "notes": "photos",
                        "filename": "https://example.cdn.space.com/14915/Images_24111756_15428.JPG"
                    },
                    {
                        "doctype": "Rental Agreement",
                        "dateadded": "2024-12-23T18:42:15.541078",
                        "user": "Test User",
                        "notes": None,
                        "filename": "https://example.cdn.space.com/14915/Rental_Agreement_24111756_35461.pdf"
                    },
                    {
                        "doctype": "Insurance Card",
                        "dateadded": "2024-12-23T18:42:41.635703",
                        "user": "Test User",
                        "notes": "Test note",
                        "filename": "https://example.cdn.space.com/14915/Insurance_Card_24111756_61565.pdf"
                    }
                ],
                "logtrail": [
                    {
                        "date": "04/07/2025",
                        "activity": "Contacted insurance company for status update",
                        "user": "Test User"
                    },
                    {
                        "date": "03/20/2025",
                        "activity": "Received correspondence from insurance requesting estimate",
                        "user": "Test User"
                    },
                    {
                        "date": "03/18/2025",
                        "activity": "Called client regarding vehicle repair status",
                        "user": "Test User"
                    }
                ]
            },
            {
                "filenumber": 25111512,
                "customername": "Test Company 2 - Another City, ST",
                "clientclaimno": "87654321",
                "rentername": "Jane Smith",
                "ranumber": "987654321",
                "insuredname": "Jane Smith / Test Business LLC",
                "insurancecompany": "Another Insurance Company",
                "claimnumber": "Unknown",
                "policynumber": "POL987654",
                "dateofloss": "2025-07-25",
                "adjuster": "Test Adjuster 2",
                "adjusterphone": "501-000-0000",
                "firstparty": True,
                "thirdparty": None,
                "cdw": None,
                "hc_adj": "Test Admin",
                "officephone": "(555) 987-6543",
                "email": "admin@example.com",
                "vin": "9ZYXW87V65U43210",
                "vehyear": 2025,
                "vehmake": "Test Make",
                "vehmodel": "Transport Van",
                "vehedition": "",
                "color": "White",
                "platenumber": "ABC8139",
                "unitnumber": "87654321",
                "inspectiondate": "2025-07-30",
                "estimateamount": 6551.79,
                "totalloss": None,
                "continuedrentalamt": None,
                "dv_amt": None,
                "liabilityaccepted": None,
                "liabilitydenied": None,
                "settlement_pd": None,
                "settlement_salvage": None,
                "settlement_cr": None,
                "settlement_dv": None,
                "settlement_other": None,
                "settlement_deductable": None,
                "administrativefee": None,
                "appraisalfee": None,
                "datefileclosed": None,
                "settlementoffer": None,
                "supplement": None,
                "settlementtowing": None,
                "settlementstorage": None,
                "demand_admin_fee": 300,
                "demand_appraisal_fee": None,
                "estimatedate": "2025-07-31",
                "demanddate": None,
                "policystartdate": None,
                "policyenddate": None,
                "vehicleowner": None,
                "docfiles": [
                    {
                        "doctype": "Images",
                        "dateadded": "2025-07-30T16:35:18.361016",
                        "user": "Test User 2",
                        "notes": None,
                        "filename": "https://example.cdn.space.com/16603/Images_25111512_16856.JPG"
                    },
                    {
                        "doctype": "Rental Agreement",
                        "dateadded": "2025-07-30T16:35:59.793683",
                        "user": "Test User 2",
                        "notes": None,
                        "filename": "https://example.cdn.space.com/16603/Rental_Agreement_25111512_59410.jpeg"
                    }
                ],
                "logtrail": [
                    {
                        "date": "08/12/2025",
                        "activity": "Emailed insurance adjuster for status update",
                        "user": "Test Admin"
                    },
                    {
                        "date": "08/06/2025",
                        "activity": "Spoke with client regarding appraisal authorization",
                        "user": "Test Admin"
                    },
                    {
                        "date": "07/30/2025",
                        "activity": "Reviewed incident report and images",
                        "user": "Test Admin"
                    }
                ]
            }
        ]
        mock_response.is_error = False
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        # Create client and call method
        client = HawkeyeClient("mock_token")
        claims = client.claims.get_claims()
        
        # Assert expected behavior
        mock_get.assert_called_once()
        self.assertIsInstance(claims, list)
        if claims:
            self.assertIsInstance(claims[0], Claim)
            self.assertEqual(claims[0].filenumber, 24111756)
            print("Get Claims Test Passed\n")

    @patch('httpx.Client.get')
    def test_get_single_claim_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = [{
                "filenumber": 24111756,
                "customername": "Test Company - City, ST",
                "clientclaimno": "12345678 (Cross Claim 98765432)",
                "rentername": "John Doe",
                "ranumber": "123456789",
                "insuredname": "John Doe",
                "insurancecompany": "Test Insurance Co.",
                "claimnumber": "1234567890123456789",
                "policynumber": "POL123456",
                "dateofloss": "2024-12-22",
                "adjuster": "Test Adjuster",
                "adjusterphone": "1-800-000-0000",
                "firstparty": True,
                "thirdparty": None,
                "cdw": None,
                "hc_adj": "Test Martinez",
                "officephone": "(555) 123-4567",
                "email": "test@example.com",
                "vin": "1ABCD23E45FG67890",
                "vehyear": 2022,
                "vehmake": "Test",
                "vehmodel": "Model 3500",
                "vehedition": "15 ft. box",
                "color": "White",
                "platenumber": "ST-ABC123",
                "unitnumber": "12345678",
                "inspectiondate": "2024-12-23",
                "estimateamount": 2933.95,
                "totalloss": None,
                "continuedrentalamt": 439.96,
                "dv_amt": 6812.89,
                "liabilityaccepted": "2025-02-19",
                "liabilitydenied": None,
                "settlement_pd": 2092.75,
                "settlement_salvage": None,
                "settlement_cr": 0,
                "settlement_dv": 0,
                "settlement_other": None,
                "settlement_deductable": 0,
                "administrativefee": 0,
                "appraisalfee": 0,
                "datefileclosed": None,
                "settlementoffer": None,
                "supplement": None,
                "settlementtowing": None,
                "settlementstorage": None,
                "demand_admin_fee": 300,
                "demand_appraisal_fee": 65,
                "estimatedate": None,
                "demanddate": None,
                "policystartdate": None,
                "policyenddate": None,
                "vehicleowner": None,
                "docfiles": [
                    {
                        "doctype": "Images",
                        "dateadded": "2024-12-23T18:40:16.435945",
                        "user": "Test User",
                        "notes": "photos",
                        "filename": "https://example.cdn.space.com/14915/Images_24111756_15428.JPG"
                    },
                    {
                        "doctype": "Rental Agreement",
                        "dateadded": "2024-12-23T18:42:15.541078",
                        "user": "Test User",
                        "notes": None,
                        "filename": "https://example.cdn.space.com/14915/Rental_Agreement_24111756_35461.pdf"
                    }
                ],
                "logtrail": [
                    {
                        "date": "04/07/2025",
                        "activity": "Contacted insurance company for status update",
                        "user": "Test User"
                    },
                    {
                        "date": "03/20/2025",
                        "activity": "Received correspondence from insurance requesting estimate",
                        "user": "Test User"
                    }
                ]
            }]
        mock_response.is_error = False
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        client = HawkeyeClient("mock_token")
        claim = client.claims.get_single_claim(24111756)

        mock_get.assert_called_once_with(
            url="/getclaims/24111756"
        )
        self.assertIsInstance(claim, Claim)
        if claim:
            self.assertEqual(claim.filenumber, 24111756)
            self.assertEqual(claim.rentername, "John Doe")
            print("Get Single Claim Test Passed\n")

    @patch('httpx.Client.post')
    def test_create_claim_success(self, mock_post):
        """Test successful claim creation."""
        # Mock the response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": 24111756,
            "message": "Claim created successfully! Filenumber is 24111756",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.create_claim(
            rentername="John Doe",
            insurancecompany="Test Insurance Co.",
            dateofloss="2024-12-01",
            vehmake="Toyota",
            vehmodel="Camry",
            vehcolor="Blue",
            vehvin="1HGBH41JXMN109186"
        )

        # Verify post was called
        mock_post.assert_called_once()
        
        self.assertEqual(response.get("filenumber"), 24111756)
        self.assertEqual(response.get("success"), True)

    # ============== EDGE CASE TESTS ==============

    @patch('httpx.Client.get')
    def test_get_claims_with_inactive(self, mock_get):
        """Test getting claims including inactive ones."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = []  # Empty list for simplicity
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        claims = self.client.claims.get_claims(include_inactive=True)

        mock_get.assert_called_once_with(
            url="/getclaims/all/true"
        )
        self.assertIsInstance(claims, list)

    @patch('httpx.Client.get')
    def test_get_claims_empty_response(self, mock_get):
        """Test handling of empty claims list."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        claims = self.client.claims.get_claims()

        self.assertIsInstance(claims, list)
        self.assertEqual(len(claims), 0)

    @patch('httpx.Client.get')
    def test_get_claims_network_error(self, mock_get):
        """Test handling of network errors."""
        mock_get.side_effect = Exception("Network connection failed")
        
        with self.assertRaises(Exception) as context:
            self.client.claims.get_claims()
        
        self.assertIn("Network connection failed", str(context.exception))

    @patch('httpx.Client.get')
    def test_get_single_claim_not_found(self, mock_get):
        """Test handling of non-existent claim."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.is_error = True
        mock_response.json.return_value = {"message": "Claim not found"}
        mock_get.return_value = mock_response

        with self.assertRaises(APIResourceNotFoundError) as context:
            self.client.claims.get_single_claim(999999)
        
        self.assertIn("not found", str(context.exception))

    @patch('httpx.Client.get')
    def test_get_single_claim_network_error(self, mock_get):
        """Test network error handling for single claim."""
        mock_get.side_effect = Exception("Connection timeout")
        
        with self.assertRaises(Exception) as context:
            self.client.claims.get_single_claim(12345)
        
        self.assertIn("Connection timeout", str(context.exception))

    @patch('httpx.Client.post')
    def test_create_claim_with_all_optional_parameters(self, mock_post):
        """Test creating a claim with all optional parameters."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": 99999,
            "message": "Claim created successfully! Filenumber is 99999",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.create_claim(
            rentername="Jane Smith",
            insurancecompany="Comprehensive Insurance Co.",
            dateofloss="2025-01-15",
            vehmake="Honda",
            vehmodel="Civic",
            vehcolor="Red",
            vehvin="2HGFC2F59MH123456",
            # Optional parameters
            clientclaimno="CLM-2025-001",
            claimnumber="INS-987654321",
            note="Customer reported vehicle damage after rental period",
            insuredname="Jane Smith",
            policynumber="POL-ABC123456",
            renterphone="555-123-4567",
            renteremail="jane.smith@email.com",
            vehlocationdetails="Parking lot at 123 Main St",
            vehlocationcity="Springfield",
            vehlocationstate="IL",
            vehyear=2021,
            vehedition="LX",
            vehplatenumber="ABC123",
            vehunitnumber="UNIT456"
        )

        # Verify post was called
        mock_post.assert_called_once()
        self.assertEqual(response.get("success"), True)

    @patch('httpx.Client.post')
    def test_create_claim_minimal_parameters(self, mock_post):
        """Test creating a claim with only required parameters."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": 88888,
            "message": "Claim created successfully! Filenumber is 88888",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.create_claim(
            rentername="Bob Johnson",
            insurancecompany="Basic Insurance",
            dateofloss="2025-02-01",
            vehmake="Ford",
            vehmodel="F-150",
            vehcolor="Blue",
            vehvin="1FTPW14V38FA12345"
        )

        mock_post.assert_called_once()
        self.assertEqual(response.get("success"), True)

    @patch('httpx.Client.post')
    def test_create_claim_special_characters(self, mock_post):
        """Test creating a claim with special characters in data."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": 77777,
            "message": "Claim created successfully! Filenumber is 77777",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.create_claim(
            rentername="José García-Martinez",
            insurancecompany="Assurance & Protection Co.",
            dateofloss="2025-03-01",
            vehmake="Volkswagen",
            vehmodel="Jetta",
            vehcolor="Silver/Gray",
            vehvin="3VW2K7AJ9EM123456",
            note="Customer stated: 'Vehicle was damaged in parking lot' - needs investigation & review"
        )

        self.assertEqual(response.get("success"), True)

    @patch('httpx.Client.post')
    def test_create_claim_network_error(self, mock_post):
        """Test network error handling for create claim."""
        mock_post.side_effect = Exception("Request timeout")
        
        with self.assertRaises(Exception) as context:
            self.client.claims.create_claim(
                rentername="Test User",
                insurancecompany="Test Insurance",
                dateofloss="2025-01-01",
                vehmake="Test",
                vehmodel="Test",
                vehcolor="Test",
                vehvin="TEST123456"
            )
        
        self.assertIn("Request timeout", str(context.exception))

    @patch('httpx.Client.post')
    def test_update_claim_success(self, mock_post):
        """Test successful claim update."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": "12345",
            "message": "Claim updated successfully",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.update_claim(
            filenumber=12345,
            clientclaimno="UPDATED-CLM-001",
            claimnumber="UPD-123456789",
            note="Updated claim information",
            rentername="Updated Renter Name"
        )

        mock_post.assert_called_once()
        self.assertEqual(response.get("success"), True)

    @patch('httpx.Client.post')
    def test_update_claim_partial_update(self, mock_post):
        """Test updating only some fields of a claim."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.is_error = False
        mock_data = {
            "filenumber": "12345",
            "message": "Claim updated successfully",
            "error": 0,
            "success": True
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        response = self.client.claims.update_claim(
            filenumber=12345,
            clientclaimno="PARTIAL-UPDATE",
            note="Only updating claim number and note"
        )

        # Verify post was called
        mock_post.assert_called_once()
        self.assertEqual(response.get("success"), True)

    @patch('httpx.Client.post')
    def test_update_claim_error_response(self, mock_post):
        """Test handling of error response from update claim API."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.is_error = True
        mock_data = {
            "message": "Claim not found",
            "error": 1,
            "success": False
        }
        mock_response.json.return_value = mock_data
        mock_post.return_value = mock_response

        with self.assertRaises(APIResourceNotFoundError) as context:
            self.client.claims.update_claim(
                filenumber=999999,
                clientclaimno="NON-EXISTENT"
            )

        self.assertEqual(context.exception.status_code, 404)
        self.assertIn("not found", context.exception.response_data.get("message", "").lower())

    @patch('httpx.Client.post')
    def test_update_claim_network_error(self, mock_post):
        """Test network error handling for update claim."""
        mock_post.side_effect = Exception("Connection lost")
        
        with self.assertRaises(Exception) as context:
            self.client.claims.update_claim(
                filenumber=12345,
                clientclaimno="TEST"
            )
        
        self.assertIn("Connection lost", str(context.exception))

    def test_client_debug_mode(self):
        """Test client initialization in debug mode."""
        debug_client = HawkeyeClient("test-token", debug_mode=True)
        # Verify debug mode uses development URL
        self.assertIn("qa", debug_client.settings.base_url.lower())

    def test_client_production_mode(self):
        """Test client initialization in production mode."""
        prod_client = HawkeyeClient("test-token", debug_mode=False)
        # Verify production mode uses production URL
        self.assertNotIn("qa", prod_client.settings.base_url.lower())


if __name__ == "__main__":
    unittest.main()
