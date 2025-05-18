import pytest
import pymongo
from bson import json_util
import json
import os
import sys
from dotenv import load_dotenv
import tempfile
import shutil

# Add the current directory to the Python path
sys.path.append(os.getcwd())

from util.dao import DAO

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def validator_setup():
    """Setup validator files for testing"""
    # Create temporary directory structure
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'src', 'static', 'validators'), exist_ok=True)
    
    # Create validator file
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "active"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "active": {
                    "bsonType": "bool",
                    "description": "must be a boolean and is required"
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    "description": "must be a valid email address"
                }
            }
        }
    }
    
    validator_path = os.path.join(temp_dir, 'src', 'static', 'validators', 'test_collection.json')
    with open(validator_path, 'w') as f:
        json.dump(validator, f)
    
    # Change to temp directory
    original_dir = os.getcwd()
    os.chdir(temp_dir)
    
    yield
    
    # Cleanup
    os.chdir(original_dir)
    shutil.rmtree(temp_dir)

@pytest.fixture(scope="function")
def test_db():
    """Fixture to set up a test database connection"""
    # Use a test database URL or the default one
    MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
    client = pymongo.MongoClient(MONGO_URL)
    
    # Create a test database
    test_db = client.edutask_test
    
    yield test_db
    
    # Cleanup after tests
    client.drop_database('edutask_test')
    client.close()

@pytest.fixture(scope="function")
def test_dao(test_db, validator_setup):
    """Fixture to create a test DAO instance"""
    collection_name = "test_collection"
    
    # Drop the collection if it exists
    if collection_name in test_db.list_collection_names():
        test_db[collection_name].drop()
    
    # Create collection with validator
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "active"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "active": {
                    "bsonType": "bool",
                    "description": "must be a boolean and is required"
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    "description": "must be a valid email address"
                }
            }
        }
    }
    
    test_db.create_collection(
        collection_name,
        validator=validator,
        validationAction="error"
    )
    
    dao = DAO(collection_name)
    dao.collection = test_db[collection_name]
    
    yield dao
    
    # Cleanup after each test
    test_db[collection_name].drop()

def test_create_valid_document(test_dao):
    """Test creating a valid document that meets all validator requirements"""
    test_data = {
        "name": "Test User",
        "active": True,
        "email": "test@example.com"
    }
    
    result = test_dao.create(test_data)
    
    assert result is not None
    assert result["name"] == test_data["name"]
    assert result["active"] == test_data["active"]
    assert result["email"] == test_data["email"]
    assert "_id" in result

def test_create_missing_required_field(test_dao):
    """Test creating a document with missing required field"""
    test_data = {
        "name": "Test User"
        # missing required 'active' field
    }
    
    with pytest.raises(pymongo.errors.WriteError):
        test_dao.create(test_data)

def test_create_invalid_field_type(test_dao):
    """Test creating a document with invalid field type"""
    test_data = {
        "name": "Test User",
        "active": "true"  # should be boolean, not string
    }
    
    with pytest.raises(pymongo.errors.WriteError):
        test_dao.create(test_data)

def test_create_invalid_email_format(test_dao):
    """Test creating a document with invalid email format"""
    test_data = {
        "name": "Test User",
        "active": True,
        "email": "invalid-email"
    }
    
    with pytest.raises(pymongo.errors.WriteError):
        test_dao.create(test_data)

def test_create_multiple_documents(test_dao):
    """Test creating multiple valid documents"""
    test_data_1 = {
        "name": "User 1",
        "active": True,
        "email": "user1@example.com"
    }
    
    test_data_2 = {
        "name": "User 2",
        "active": False,
        "email": "user2@example.com"
    }
    
    result_1 = test_dao.create(test_data_1)
    result_2 = test_dao.create(test_data_2)
    
    assert result_1["name"] == test_data_1["name"]
    assert result_2["name"] == test_data_2["name"]
    assert result_1["_id"] != result_2["_id"] 