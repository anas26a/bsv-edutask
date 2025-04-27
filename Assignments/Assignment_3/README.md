# Assignment 3 - Integration Testing Setup

## Prerequisites

You'll need to install MongoDB and Python packages to run the tests. Follow these steps:

### 1. Install MongoDB (Ubuntu/WSL)
```bash
# Add MongoDB GPG key
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor

# Add MongoDB repository
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | \
   sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Update package list and install MongoDB
sudo apt-get update
sudo apt-get install -y mongodb-org

# Start MongoDB service
sudo service mongod start
```

### 2. Install Python Dependencies
```bash
pip install pytest pymongo python-dotenv
```

## Running the Tests

1. Make sure MongoDB is running:
```bash
# Check MongoDB status
mongosh --eval "db.version()"
```

2. Navigate to the backend directory:
```bash
cd backend
```

3. Run the tests:
```bash
pytest ../Assignments/Assignment_3/test_dao_integration.py -v
```

## Expected Output
You should see all 5 tests passing:
- test_create_valid_document
- test_create_missing_required_field
- test_create_invalid_field_type
- test_create_invalid_email_format
- test_create_multiple_documents

## Troubleshooting

1. If MongoDB fails to start, try:
```bash
sudo service mongod restart
```

2. If you get import errors, make sure you're running the tests from the backend directory.

3. If you get permission errors with MongoDB:
```bash
sudo chown -R mongodb:mongodb /var/lib/mongodb
sudo chown mongodb:mongodb /tmp/mongodb-27017.sock
```

## Files in this Assignment
- `test_dao_integration.py`: Integration tests for the DAO layer
- `conftest.py`: Configuration file that sets up the Python path for tests
- `integration_testing_report.md`: Documentation and test results
- `README.md`: This setup guide

## Note
The tests use a separate test database (`edutask_test`) and clean up after themselves, so they won't interfere with any production data. 