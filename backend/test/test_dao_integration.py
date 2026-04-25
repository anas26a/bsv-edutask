import pytest
from pymongo import MongoClient
from pymongo.errors import WriteError
import json
from src.util.dao import DAO
from src.util.validators import getValidator


@pytest.fixture
def test_dao():
    """
    Fixture that provides a clean test DAO instance connected to a test collection.
    Uses MongoDB's schema validation to enforce data constraints.
    Cleans up (drops the collection) after the test completes.
    """
    # Connect to MongoDB at localhost
    client = MongoClient('mongodb://localhost:27017')
    test_db = client['edutask_test']
    
    # Drop collection if it exists (clean slate)
    if 'user' in test_db.list_collection_names():
        test_db['user'].drop()
    
    # Create collection with validator schema
    validator = getValidator('user')
    test_db.create_collection('user', validator=validator)
    
    # Create a DAO instance and redirect it to our test collection
    dao = DAO('user')
    dao.collection = test_db['user']
    
    # Yield the DAO to the test
    yield dao
    
    # Cleanup: drop the test collection
    test_db['user'].drop()
    client.close()


class TestDAOCreate:
    """Integration tests for DAO.create method with MongoDB validators."""
    
    # TC-01: All required fields present, all types correct, first document
    def test_create_valid_document_success(self, test_dao):
        """TC-01: Create a valid user document with all required fields."""
        data = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        
        result = test_dao.create(data)
        
        assert '_id' in result
    
    # TC-02: All required fields present, all types correct, second unique document
    def test_create_second_valid_document_success(self, test_dao):
        """TC-02: Create a second valid user document with unique email."""
        # Create first document
        data1 = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        test_dao.create(data1)
        
        # Create second document with different email
        data2 = {
            'firstName': 'Jane',
            'lastName': 'Smith',
            'email': 'jane@example.com'
        }
        
        result = test_dao.create(data2)
        
        assert '_id' in result
    
    # TC-03: Duplicate email should fail
    def test_create_duplicate_email_fails(self, test_dao):
        """TC-03: Creating a document with duplicate email should raise WriteError."""
        # Create first document
        data1 = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        test_dao.create(data1)
        
        # Try to create second document with same email
        data2 = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data2)
    
    # TC-04: Missing firstName
    def test_create_missing_firstName_fails(self, test_dao):
        """TC-04: Creating a document without firstName should raise WriteError."""
        data = {
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
    
    # TC-05: Missing lastName
    def test_create_missing_lastName_fails(self, test_dao):
        """TC-05: Creating a document without lastName should raise WriteError."""
        data = {
            'firstName': 'John',
            'email': 'john@example.com'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
    
    # TC-06: Missing email
    def test_create_missing_email_fails(self, test_dao):
        """TC-06: Creating a document without email should raise WriteError."""
        data = {
            'firstName': 'John',
            'lastName': 'Doe'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
    
    # TC-07: firstName with wrong type (int instead of string)
    def test_create_firstName_wrong_type_fails(self, test_dao):
        """TC-07: Creating a document with firstName as int should raise WriteError."""
        data = {
            'firstName': 123,  # int instead of string
            'lastName': 'Doe',
            'email': 'john@example.com'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
    
    # TC-08: lastName with wrong type (int instead of string)
    def test_create_lastName_wrong_type_fails(self, test_dao):
        """TC-08: Creating a document with lastName as int should raise WriteError."""
        data = {
            'firstName': 'John',
            'lastName': 456,  # int instead of string
            'email': 'john@example.com'
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
    
    # TC-09: email with wrong type (int instead of string)
    def test_create_email_wrong_type_fails(self, test_dao):
        """TC-09: Creating a document with email as int should raise WriteError."""
        data = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 789  # int instead of string
        }
        
        with pytest.raises(WriteError):
            test_dao.create(data)
