import pytest
from unittest.mock import MagicMock
from src.controllers.usercontroller import UserController

class TestGetUserByEmail:
    def test_valid_registered_email_returns_matching_user(self):
        mock_dao = MagicMock()
        expected_user = {'_id': '123', 'email': 'test@example.com', 'name': 'Test User'}
        mock_dao.find.return_value = [expected_user]
        controller = UserController(dao=mock_dao)

        result = controller.get_user_by_email('test@example.com')

        assert result == expected_user

    def test_db_success_calls_find_once(self):
        mock_dao = MagicMock()
        mock_dao.find.return_value = [{'_id': '123', 'email': 'test@example.com'}]
        controller = UserController(dao=mock_dao)

        controller.get_user_by_email('test@example.com')

        assert mock_dao.find.call_count == 1

    def test_unregistered_email_returns_none(self):
        mock_dao = MagicMock()
        mock_dao.find.return_value = []
        controller = UserController(dao=mock_dao)

        result = controller.get_user_by_email('unknown@example.com')

        assert result is None

    def test_multiple_users_found_returns_first_user(self):
        mock_dao = MagicMock()
        mock_users = [
            {'_id': '123', 'email': 'test@example.com', 'name': 'User One'},
            {'_id': '456', 'email': 'test@example.com', 'name': 'User Two'}
        ]
        mock_dao.find.return_value = mock_users
        controller = UserController(dao=mock_dao)

        result = controller.get_user_by_email('test@example.com')

        assert result == mock_users[0]

    @pytest.mark.parametrize('bad_email', ['not-an-email', 'missing@dot', '@missinglocal.com'])
    def test_malformed_email_raises_value_error(self, bad_email):
        mock_dao = MagicMock()
        controller = UserController(dao=mock_dao)

        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email(bad_email)

    def test_empty_email_raises_value_error(self):
        mock_dao = MagicMock()
        controller = UserController(dao=mock_dao)

        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email('')

    def test_none_email_raises_value_error(self):
        mock_dao = MagicMock()
        controller = UserController(dao=mock_dao)

        with pytest.raises(ValueError, match='Error: invalid email address'):
            controller.get_user_by_email(None)

    def test_database_operation_failure_is_propagated(self):
        mock_dao = MagicMock()
        mock_dao.find.side_effect = Exception('database unavailable')
        controller = UserController(dao=mock_dao)

        with pytest.raises(Exception, match='database unavailable'):
            controller.get_user_by_email('test@example.com')