import unittest
from unittest.mock import patch, Mock
import requests
import json

from hawkeye_sdk_for_python import HawkeyeClient
from hawkeye_sdk_for_python.types.api_request_response import Claim, ApiResponse

class TestClaimsModule(unittest.TestCase):
    @patch('requests.get')
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
        mock_response.text = json.dumps(mock_data)
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

    @patch('requests.get')
    def test_get_single_claim_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
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
        mock_response.text = json.dumps(mock_data)
        mock_get.return_value = mock_response

        client = HawkeyeClient("mock_token")
        claim = client.claims.get_single_claim(24111756)

        mock_get.assert_called_once_with(
            url="https://hawkeye.g2it.co/api/getclaims/24111756",
            headers={"Content-Type": "application/json", "Authorization": "Bearer mock_token"}
        )
        self.assertIsInstance(claim, Claim)
        if claim:
            self.assertEqual(claim.filenumber, 24111756)
            self.assertEqual(claim.rentername, "John Doe")
            print("Get Single Claim Test Passed\n")

    @patch('requests.post')
    def test_create_claim_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_data = {
            "filenumber": 24111756,
            "message": "Claim created sucessfully! Filenumber is 24111756",
            "error": 0,
            "success": True
        }
        mock_response.text = json.dumps(mock_data)
        mock_post.return_value = mock_response

        client = HawkeyeClient("mock_token")
        response = client.claims.create_claim(
            rentername="John Doe",
            insurancecompany="Test Insurance Co.",
            dateofloss="2024-12-01",
            vehmake="Toyota",
            vehmodel="Camry",
            vehcolor="Blue",
            vehvin="1HGBH41JXMN109186"
        )

        mock_post.assert_called_once_with(
            url="https://hawkeye.g2it.co/api/createclaim",
            headers={"Content-Type": "application/json", "Authorization": "Bearer mock_token"},
            data={
                "rentername": "John Doe",
                "insurancecompany": "Test Insurance Co.",
                "dateofloss": "2024-12-01",
                "vehmake": "Toyota",
                "vehmodel": "Camry",
                "vehcolor": "Blue",
                "vehvin": "1HGBH41JXMN109186"
            }
        )

        #self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.get("filenumber"), 24111756)

if __name__ == "__main__":
    unittest.main()
