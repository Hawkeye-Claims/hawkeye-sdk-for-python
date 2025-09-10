import unittest
from unittest.mock import patch, Mock
import json
from datetime import datetime

from hawkeye_sdk_for_python import HawkeyeClient
from hawkeye_sdk_for_python.types import ApiResponse


class TestLogtrailsModule(unittest.TestCase):
    def setUp(self):
        """Set up test client for each test case."""
        self.client = HawkeyeClient("test-auth-token")
        self.test_filenumber = 12345
        self.test_activity = "Test activity for claim processing"

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_with_defaults(self, mock_post):
        """Test creating a log trail entry with default date."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Get current date for comparison
        current_date = datetime.now().strftime("%m/%d/%Y")

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity=self.test_activity
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": current_date,
                "activity": self.test_activity
            }
        )

        # Verify the response
        self.assertEqual(result["message"], "Log entry created successfully")
        self.assertTrue(result["success"])
        self.assertEqual(result["error"], 0)
        self.assertEqual(result.get("filenumber"), str(self.test_filenumber))

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_with_custom_date(self, mock_post):
        """Test creating a log trail entry with a custom date."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Test data
        custom_date = "01/15/2024"

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity=self.test_activity,
            date=custom_date
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": custom_date,
                "activity": self.test_activity
            }
        )

        # Verify the response
        self.assertEqual(result["message"], "Log entry created successfully")
        self.assertTrue(result["success"])
        self.assertEqual(result["error"], 0)

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_claim_created(self, mock_post):
        """Test creating a log trail entry for claim creation."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity="New claim created in system",
            date="09/10/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/10/2025",
                "activity": "New claim created in system"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_insurance_contact(self, mock_post):
        """Test creating a log trail entry for insurance company contact."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity="Contacted insurance company for status update",
            date="09/09/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/09/2025",
                "activity": "Contacted insurance company for status update"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_document_received(self, mock_post):
        """Test creating a log trail entry for document receipt."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity="Received rental agreement from customer",
            date="09/08/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/08/2025",
                "activity": "Received rental agreement from customer"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_settlement_update(self, mock_post):
        """Test creating a log trail entry for settlement updates."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity="Settlement offer of $5,000 received from insurance carrier",
            date="09/07/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/07/2025",
                "activity": "Settlement offer of $5,000 received from insurance carrier"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_claim_closed(self, mock_post):
        """Test creating a log trail entry for claim closure."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity="Claim closed - settlement payment received and processed",
            date="09/06/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/06/2025",
                "activity": "Claim closed - settlement payment received and processed"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_long_activity(self, mock_post):
        """Test creating a log trail entry with a long activity description."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        long_activity = ("Conducted thorough review of all claim documentation including rental agreement, "
                        "insurance policy details, police report, vehicle damage assessment, repair estimates, "
                        "and customer correspondence. Verified all required documentation is complete and accurate. "
                        "Prepared comprehensive summary for insurance adjuster review and settlement negotiation.")

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity=long_activity,
            date="09/05/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/05/2025",
                "activity": long_activity
            }
        )

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_error_response(self, mock_post):
        """Test handling of error response from API."""
        # Setup mock response with error
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.text = json.dumps({
            "message": "Invalid file number",
            "success": False,
            "error": 1
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=999999,  # Invalid file number
            activity=self.test_activity
        )

        # Verify the response contains error information
        self.assertEqual(result["message"], "Invalid file number")
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], 1)

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_network_error(self, mock_post):
        """Test handling of network errors during log trail creation."""
        # Setup mock to raise an exception
        mock_post.side_effect = Exception("Network connection failed")

        # Verify that the exception is raised
        with self.assertRaises(Exception) as context:
            self.client.logtrails.create_log_trail(
                file_number=self.test_filenumber,
                activity=self.test_activity
            )

        self.assertIn("Network connection failed", str(context.exception))

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_malformed_json_response(self, mock_post):
        """Test handling of malformed JSON response."""
        # Setup mock response with invalid JSON
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "Invalid JSON response"
        mock_post.return_value = mock_response

        # Verify that JSON decode error is raised
        with self.assertRaises(json.JSONDecodeError):
            self.client.logtrails.create_log_trail(
                file_number=self.test_filenumber,
                activity=self.test_activity
            )

    def test_date_format_validation(self):
        """Test that the default date format is MM/DD/YYYY."""
        # Get current date in expected format
        expected_format = datetime.now().strftime("%m/%d/%Y")
        
        # Verify format matches MM/DD/YYYY pattern
        self.assertRegex(expected_format, r'^\d{1,2}/\d{1,2}/\d{4}$')

    @patch('hawkeye_sdk_for_python.modules.logtrails.requests.post')
    def test_create_log_trail_special_characters(self, mock_post):
        """Test creating log trail with special characters in activity."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Log entry created successfully",
            "success": True,
            "error": 0,
            "filenumber": str(self.test_filenumber)
        })
        mock_post.return_value = mock_response

        # Activity with special characters
        special_activity = "Customer called regarding claim #12345 - stated vehicle VIN: 1ABCD23E45FG67890 & requested update on settlement ($5,000.00)"

        # Call the method
        result = self.client.logtrails.create_log_trail(
            file_number=self.test_filenumber,
            activity=special_activity,
            date="09/04/2025"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/createLogTrailEntry",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "date": "09/04/2025",
                "activity": special_activity
            }
        )


if __name__ == '__main__':
    unittest.main()
