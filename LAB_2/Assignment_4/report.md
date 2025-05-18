# Test Execution Report: GUI E2E Tests (Assignment 4)

## Screenshot

![Cypress Test Runner Screenshot](./cypress_test_runner_screenshot.png)

---

## Brief Report

- **Test Execution Date:** Sunday, May 18, 2025
- **Test Environment:**
  - Cypress 14.3.3
  - Chrome browser
  - Ubuntu 22.04 (WSL2)
  - Application running at http://localhost:3000
- **Test Cases Executed:**
  - R8UC1: Create To-Do Item (including negative test for empty input)
  - R8UC2: Toggle To-Do Item (including negative test for non-existent item)
  - R8UC3: Delete To-Do Item (including negative test for empty list)
- **Result:** All tests passed successfully. The Cypress test runner (see screenshot above) shows green checkmarks for each scenario, indicating correct system behavior for all tested use cases.
- **System Failures Detected:** None. All functionalities worked as expected. No errors or unexpected behaviors were observed during test execution.
- **Notes:**
  - The tests were designed and implemented according to the official course Tutorials and Lectures, using the 4-step test design technique and a use-case-driven approach.
  - Assertions were made both for positive (happy path) and negative (edge case) scenarios.
  - For implementation details, see `cypress/todo_e2e.cy.js`.
