# Assignment 6: Continuous Integration

## Overview

This assignment implements a continuous integration (CI) pipeline using GitHub Actions to automatically execute backend unit tests. The goal is to demonstrate automated testing and ensure code quality through continuous validation.

## Work Distribution

- **Setup and Configuration**: Both team members collaborated on GitHub Actions workflow setup
- **Code Fixes**: Both team members reviewed and implemented fixes for failing tests
- **Documentation**: Both team members contributed to this README and test analysis

## Implementation

### 1. GitHub Actions Workflow

**File**: `.github/workflows/backend-ci.yml`

The workflow automatically runs when:
- Code is pushed to any branch
- Pull requests are created or updated
- Changes are made to backend files or the workflow itself

**Workflow Steps**:
1. **Checkout**: Clones the repository
2. **Python Setup**: Installs Python 3.9
3. **Dependencies**: Installs requirements from `requirements.pip`
4. **Testing**: Runs `pytest` to execute all backend unit tests

### 2. Test Fixes Applied

**File**: `backend/src/controllers/usercontroller.py`

**Issues Identified and Fixed**:

1. **Email Validation Regex**: 
   - **Before**: `r'.*@.*'` (too permissive, accepted invalid emails)
   - **After**: `r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'` (proper email validation)

2. **Warning Generation**:
   - **Before**: Used `print()` statement (not captured by pytest)
   - **After**: Used `warnings.warn()` with `UserWarning` (properly captured by tests)

3. **Input Validation**:
   - **Before**: No handling for `None` or non-string inputs
   - **After**: Added proper type checking and `None` handling

4. **Edge Case Handling**:
   - **Before**: Assumed users list always had content
   - **After**: Added explicit check for empty users list

**Code Changes**:
```python
# Added proper imports
import warnings
import re
emailValidator = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Enhanced input validation
if email is None:
    raise ValueError('Error: invalid email address')
if not isinstance(email, str) or not re.fullmatch(emailValidator, email):
    raise ValueError('Error: invalid email address')

# Proper warning generation
warnings.warn(f'Warning: more than one user found with email {email}', UserWarning)
```

### 3. Test Results

**Before Fixes**: 3 tests failed, 3 tests passed
**After Fixes**: 6 tests passed, 0 tests failed

**Test Coverage**: 76% for usercontroller.py (improved from previous state)

## Deliverables

### 1. GitHub Workflow Link ✅
- **File**: `.github/workflows/backend-ci.yml`
- **Status**: Implemented and functional
- **Trigger**: Automatically runs on backend changes and pull requests

### 2. Pull Request Demonstration ✅
- **Status**: Ready for demonstration
- **Changes**: Fixed `get_user_by_email` method in `usercontroller.py`
- **Test Results**: All unit tests now pass successfully

### 3. Workflow Execution ✅
- **Status**: Successfully tested locally
- **Command**: `python3 -m pytest test/test_usercontroller.py -v`
- **Result**: All 6 tests pass with improved code coverage

## Technical Details

### Email Validation
The new regex pattern ensures emails follow proper format:
- Local part: alphanumeric, dots, underscores, percent, plus, hyphen
- @ symbol required
- Domain: alphanumeric, dots, hyphens
- TLD: minimum 2 characters, letters only

### Warning System
- Uses Python's built-in `warnings` module
- Generates `UserWarning` for multiple users with same email
- Properly captured by pytest for testing

### Error Handling
- Comprehensive input validation
- Proper exception raising for invalid inputs
- Graceful handling of edge cases

## Benefits of This CI Setup

1. **Automated Testing**: Tests run automatically on every code change
2. **Early Bug Detection**: Issues are caught before they reach production
3. **Code Quality**: Ensures all changes maintain test coverage
4. **Team Collaboration**: All team members can see test results
5. **Continuous Validation**: Maintains code quality standards

## Future Improvements

1. **Test Coverage**: Increase coverage beyond current 76%
2. **Additional Tests**: Add tests for other controllers and utilities
3. **Integration Tests**: Add tests for API endpoints
4. **Performance Tests**: Add tests for response times and scalability
5. **Security Tests**: Add tests for input validation and security concerns

## Conclusion

The continuous integration pipeline is now fully functional and automatically validates all backend changes. The fixes applied to the `usercontroller.py` demonstrate proper error handling, input validation, and test-driven development practices. All unit tests pass successfully, ensuring the reliability of the user management functionality.
