import unittest
from unittest.mock import patch, Mock
import json
from datetime import datetime

from hawkeye_sdk_for_python import HawkeyeClient
from hawkeye_sdk_for_python.types import DocType


class TestDocfilesModule(unittest.TestCase):
    def setUp(self):
        """Set up test client for each test case."""
        self.client = HawkeyeClient("test-auth-token")
        self.test_filenumber = 12345
        self.test_fileurl = "https://example.com/test-document.pdf"

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_with_defaults(self, mock_post):
        """Test uploading a file with default parameters."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "File uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl=self.test_fileurl
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": self.test_fileurl,
                "category": DocType.DEFAULT.value,
                "visibleToClient": False,
                "notes": ""
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_with_all_parameters(self, mock_post):
        """Test uploading a file with all parameters specified."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "File uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Test data
        test_notes = "Test document for insurance claim"
        test_category = DocType.INSURANCE_CARD
        test_visible = True

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl=self.test_fileurl,
            category=test_category,
            visibleToClient=test_visible,
            notes=test_notes
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": self.test_fileurl,
                "category": test_category.value,
                "visibleToClient": test_visible,
                "notes": test_notes
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_rental_agreement(self, mock_post):
        """Test uploading a rental agreement document."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Rental agreement uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl="https://example.com/rental-agreement.pdf",
            category=DocType.RENTAL_AGREEMENT,
            visibleToClient=True,
            notes="Initial rental agreement for claim processing"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": "https://example.com/rental-agreement.pdf",
                "category": "Rental Agreement",
                "visibleToClient": True,
                "notes": "Initial rental agreement for claim processing"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_police_report(self, mock_post):
        """Test uploading a police report document."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Police report uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl="https://example.com/police-report.pdf",
            category=DocType.POLICE_REPORT,
            visibleToClient=False,
            notes="Official police report for incident #12345"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": "https://example.com/police-report.pdf",
                "category": "Police Report",
                "visibleToClient": False,
                "notes": "Official police report for incident #12345"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_images(self, mock_post):
        """Test uploading images/photos."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Images uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl="https://example.com/damage-photos.zip",
            category=DocType.IMAGES,
            visibleToClient=True,
            notes="Vehicle damage photos from incident scene"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": "https://example.com/damage-photos.zip",
                "category": "Images",
                "visibleToClient": True,
                "notes": "Vehicle damage photos from incident scene"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_invoice(self, mock_post):
        """Test uploading an invoice document."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "Invoice uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl="https://example.com/repair-invoice.pdf",
            category=DocType.INVOICE,
            visibleToClient=True,
            notes="Repair shop invoice for vehicle restoration"
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": "https://example.com/repair-invoice.pdf",
                "category": "Invoice",
                "visibleToClient": True,
                "notes": "Repair shop invoice for vehicle restoration"
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_with_empty_notes(self, mock_post):
        """Test uploading a file with empty notes."""
        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "message": "File uploaded successfully",
            "success": True,
            "error": 0
        })
        mock_post.return_value = mock_response

        # Call the method
        result = self.client.docfiles.upload_file(
            filenumber=self.test_filenumber,
            fileurl=self.test_fileurl,
            category=DocType.OTHER,
            visibleToClient=False,
            notes=""
        )

        # Verify the request
        mock_post.assert_called_once_with(
            url=f"{self.client.settings.base_url}/savefile",
            headers=self.client.settings.headers,
            json={
                "filenumber": self.test_filenumber,
                "link": self.test_fileurl,
                "category": "Other",
                "visibleToClient": False,
                "notes": ""
            }
        )

    @patch('hawkeye_sdk_for_python.modules.docfiles.requests.post')
    def test_upload_file_network_error(self, mock_post):
        """Test handling of network errors during file upload."""
        # Setup mock to raise an exception
        mock_post.side_effect = Exception("Network error")

        # Verify that the exception is raised
        with self.assertRaises(Exception) as context:
            self.client.docfiles.upload_file(
                filenumber=self.test_filenumber,
                fileurl=self.test_fileurl
            )

        self.assertIn("Network error", str(context.exception))

    def test_doctype_enum_values(self):
        """Test that DocType enum values are correctly mapped."""
        # Test a few key document types
        self.assertEqual(DocType.DEFAULT.value, "Uncategorized API Document")
        self.assertEqual(DocType.RENTAL_AGREEMENT.value, "Rental Agreement")
        self.assertEqual(DocType.INSURANCE_CARD.value, "Insurance Card")
        self.assertEqual(DocType.POLICE_REPORT.value, "Police Report")
        self.assertEqual(DocType.IMAGES.value, "Images")
        self.assertEqual(DocType.INVOICE.value, "Invoice")
        self.assertEqual(DocType.OTHER.value, "Other")


if __name__ == '__main__':
    unittest.main()
