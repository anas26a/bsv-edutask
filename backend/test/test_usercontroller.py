import pytest
from unittest.mock import MagicMock
from src.controllers.usercontroller import UserController
from src.util.dao import DAO

# Test cases for get_user_by_email function
class TestGetUserByEmail:
    
    def test_valid_registered_email(self):
        """Test that a registered email returns the correct user object"""
        # Setup mock DAO
        mock_dao = MagicMock()
        expected_user = {'_id': '123', 'email': 'test@example.com', 'name': 'Test User'}
        mock_dao.find.return_value = [expected_user]  # Simulate a single user match
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute
        result = controller.get_user_by_email('test@example.com')
        
        # Verify
        assert result == expected_user
        mock_dao.find.assert_called_once_with({'email': 'test@example.com'})

    def test_unregistered_email(self):
        """Test that an unregistered email returns None"""
        # Setup mock DAO
        mock_dao = MagicMock()
        mock_dao.find.return_value = []  # Simulate no user match
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute
        result = controller.get_user_by_email('unknown@example.com')
        
        # Verify
        assert result is None
        mock_dao.find.assert_called_once_with({'email': 'unknown@example.com'})

    def test_multiple_users_found(self):
        """Test that multiple users found with the same email prints a warning and returns the first user"""
        # Setup mock DAO
        mock_dao = MagicMock()
        mock_users = [
            {'_id': '123', 'email': 'test@example.com', 'name': 'User One'},
            {'_id': '456', 'email': 'test@example.com', 'name': 'User Two'}
        ]
        mock_dao.find.return_value = mock_users  # Simulate multiple users with the same email
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute
        with pytest.warns(UserWarning, match=f'Warning: more than one user found with email test@example.com'):
            result = controller.get_user_by_email('test@example.com')
        
        # Verify
        assert result == mock_users[0]  # The first user should be returned
        mock_dao.find.assert_called_once_with({'email': 'test@example.com'})

    def test_malformed_email(self):
        """Test that malformed emails raise a ValueError"""
        # Setup mock DAO
        mock_dao = MagicMock()
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute & Verify
        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email('not-an-email')
        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email('missing@dot')
        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email('@missinglocal.com')
        mock_dao.find.assert_not_called()

    def test_empty_email(self):
        """Test that empty string raises a ValueError"""
        # Setup mock DAO
        mock_dao = MagicMock()
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute & Verify
        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email('')
        mock_dao.find.assert_not_called()

    def test_none_email(self):
        """Test that None input raises a ValueError"""
        # Setup mock DAO
        mock_dao = MagicMock()
        
        # Initialize UserController with the mock DAO
        controller = UserController(dao=mock_dao)
        
        # Execute & Verify
        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email(None)
        mock_dao.find.assert_not_called()