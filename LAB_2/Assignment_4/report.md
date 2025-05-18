# Test Execution Report: GUI E2E Tests (Assignment 4)

## Screenshot

![All Tests - Cypress Test Runner](./all_tests.png)

![Failed Tests - Cypress Test Runner](./failed.png)

If not visible check the screenshots folder.
---

## Brief Report

- **Test Execution Date:** Sunday, May 16, 2025
- **Test Environment:**
  - Cypress (GUI runner)
  - Chrome browser
  - Application running at http://localhost:3000
- **Test Cases Executed:**
  - R8UC1: Add a New Todo Item (Main Scenario)
  - R8UC1: Add a New Todo Item (Alternative: Empty Description)
  - R8UC2: Toggle a Todo Item (Active to done)
  - R8UC2: Toggle a Todo Item (Done to Active)
  - R8UC3: Delete a Todo Item
- **Result:**
  - The main scenario for adding a new todo item, both toggle scenarios, and the delete scenario passed successfully (green checkmarks).
  - The alternative scenario for R8UC1 (Add with Empty Description) failed. The test expected the "Add" button to be disabled when the input is empty, but it was not disabled, indicating a possible UI/UX or validation issue.
  - The delete scenario for R8UC3 failed in one run, as the test expected the deleted item to be removed from the list, but it was still present. This may indicate a bug in the delete functionality or a test setup issue (e.g., not isolating test data).
- **System Failures Detected:**
  - R8UC1 (Alternative): The "Add" button is not disabled for empty input, which does not match the requirement.
  - R8UC3: The deleted todo item sometimes remains in the list, suggesting a possible bug or state management issue.
- **Notes:**
  - The screenshots above (all_tests.png and failed.png) show the test runner with both passing and failing tests, as well as the error stack traces for failed assertions.
  - The test implementation follows the requirements and course best practices, but the failures indicate areas where the application does not fully meet the specified requirements.
  - For implementation details, see `cypress/todo_e2e.cy.js`. 