# Hawkeye SDK for Python

A Python SDK for interacting with the Hawkeye Claims Management API. This SDK provides a simple and intuitive interface for managing insurance claims, documents, and status logs.

## Features

- **Claims Management**: Create, retrieve, and update insurance claims
- **Document Management**: Upload and manage claim-related documents
- **Log Trails**: Create activity logs for claims
- **Type Safety**: Full type hints and dataclass support
- **Environment Support**: Production and development environment support

## Installation

Install the SDK using `uv` with the GitHub repository:

```bash
uv add git+https://github.com/Hawkeye-Claims/hawkeye-sdk-for-python
```

Or using pip:

```bash
pip install git+https://github.com/Hawkeye-Claims/hawkeye-sdk-for-python

```

## Quick Start

```python
from hawkeye_sdk_for_python import HawkeyeClient

# Initialize the client
client = HawkeyeClient("your-auth-token")

# For development environment
client = HawkeyeClient("your-auth-token", debug_mode=True)

# Get all claims
claims = client.claims.get_claims()

# Get a specific claim
claim = client.claims.get_single_claim(filenumber=12345)

# Create a new claim
response = client.claims.create_claim(
    rentername="John Doe",
    inscompaniesid="ABC Insurance",
    dateofloss="2024-01-15",
    vehmake="Toyota",
    vehmodel="Camry",
    vehcolor="Blue",
    vehvin="1HGBH41JXMN109186"
)
```

## API Reference

### HawkeyeClient

The main client class for interacting with the Hawkeye API.

```python
client = HawkeyeClient(auth_token: str, debug_mode: bool = False)
```

**Parameters:**
- `auth_token`: Your Hawkeye API authentication token
- `debug_mode`: Set to `True` to use the development environment (default: `False`)

### Claims Module

#### Get All Claims

```python
claims = client.claims.get_claims(include_inactive: bool = False)
```

Returns a list of [`Claim`](hawkeye_sdk_for_python/types/api_request_response.py) objects.

#### Get Single Claim

```python
claim = client.claims.get_single_claim(filenumber: int)
```

Returns a single [`Claim`](hawkeye_sdk_for_python/types/api_request_response.py) object.

#### Create Claim

```python
response = client.claims.create_claim(
    rentername: str,
    insurancecompany: str,
    dateofloss: str,
    vehmake: str,
    vehmodel: str,
    vehcolor: str,
    vehvin: str,
    # Optional parameters
    clientclaimno: Optional[str] = None,
    claimnumber: Optional[str] = None,
    note: Optional[str] = None,
    insuredname: Optional[str] = None,
    policynumber: Optional[str] = None,
    renterphone: Optional[str] = None,
    renteremail: Optional[str] = None,
    vehlocationdetails: Optional[str] = None,
    vehlocationcity: Optional[str] = None,
    vehlocationstate: Optional[str] = None,
    vehyear: Optional[int] = None,
    vehedition: Optional[str] = None,
    vehplatenumber: Optional[str] = None,
    vehuninumber: Optional[str] = None
)
```

Returns an [`ApiResponse`](hawkeye_sdk_for_python/types/api_request_response.py) object.

#### Update Claim

```python
response = client.claims.update_claim(
    filenumber: int,
    # All other parameters are optional
    clientclaimno: Optional[str] = None,
    claimnumber: Optional[str] = None,
    # ... (same optional parameters as create_claim)
)
```

### Document Files Module

#### Upload File

```python
client.docfiles.upload_file(
    filenumber: int,
    fileurl: str,
    category: Optional[DocType] = DocType.DEFAULT,
    visibleToClient: Optional[bool] = False,
    notes: Optional[str] = ""
)
```

**Document Types:**
The SDK supports various document types via the [`DocType`](hawkeye_sdk_for_python/types/hc_enums.py) enum, including:
- `IMAGES`
- `RENTAL_AGREEMENT`
- `INSURANCE_CARD`
- `POLICE_REPORT`
- `INVOICE`
- And many more...

### Status Log Module

#### Create Status Log Trail Entry

```python
response = client.logtrails.create_log_trail(
    file_number: int,
    activity: str,
    date: Optional[str] = None  # Defaults to current date
)
```

## Data Types

### Claim

The [`Claim`](hawkeye_sdk_for_python/types/api_request_response.py) dataclass contains all claim information including:

- Basic information (filenumber, customer name, renter name)
- Insurance details (company, policy number, adjuster)
- Vehicle information (make, model, VIN, year)
- Financial data (estimate amount, settlement amounts)
- Associated documents and log trails

### DocFile

The [`DocFile`](hawkeye_sdk_for_python/types/api_request_response.py) dataclass represents uploaded documents with:
- Document type and category
- Upload date and user
- File URL and notes

### LogTrail

The [`LogTrail`](hawkeye_sdk_for_python/types/api_request_response.py) dataclass represents activity logs with:
- Date and activity description
- User who created the entry

## Examples

### Complete Workflow Example

```python
from hawkeye_sdk_for_python import HawkeyeClient, DocType

# Initialize client
client = HawkeyeClient("your-auth-token")

# Create a new claim
create_response = client.claims.create_claim(
    rentername="Jane Smith",
    insurancecompany="XYZ Insurance Co.",
    dateofloss="2024-02-01",
    vehmake="Honda",
    vehmodel="Civic",
    vehcolor="Red",
    vehvin="2HGFC2F59MH123456",
    clientclaimno="CLM-2024-001",
    vehyear=2021
)

filenumber = create_response["filenumber"]
print(f"Created claim with file number: {filenumber}")

# Upload a document
client.docfiles.upload_file(
    filenumber=filenumber,
    fileurl="https://example.com/rental-agreement.pdf",
    category=DocType.RENTAL_AGREEMENT,
    notes="Initial rental agreement"
)

# Add a log entry
client.logtrails.create_log_trail(
    file_number=filenumber,
    activity="Initial claim setup completed"
)

# Retrieve the updated claim
updated_claim = client.claims.get_single_claim(filenumber)
print(f"Claim has {len(updated_claim.docfiles)} documents")
print(f"Claim has {len(updated_claim.logtrail)} log entries")
```

### Error Handling

```python
try:
    claim = client.claims.get_single_claim(999999)
except Exception as e:
    print(f"Error retrieving claim: {e}")
```

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_claims.py
```

### Environment Setup

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

## API Documentation

For detailed API documentation, visit the [Hawkeye API Documentation](https://documenter.getpostman.com/view/21670991/UzBtkNQg).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## Support

For support or questions, please contact the development team or open an issue on GitHub.
