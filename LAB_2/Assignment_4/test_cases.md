# GUI Test Cases for Requirement 8 (R8UC1, R8UC2, R8UC3)

**Source:** Derived using the 4-step test design technique from Tutorial 3 and the use-case-driven approach from the "Basics of UI Testing" lecture.

## R8UC1: Create To-Do Item
| Step | Action | Expected Outcome | Condition |
|------|--------|------------------|-----------|
| 1 | Navigate to the task list page | Task list is displayed | User is logged in |
| 2 | Enter a new to-do item in the input field | Text appears in the input | Input is not empty |
| 3 | Click the "Add" button | New to-do item appears in the list | |
| 4 | Verify the item is saved (refresh page) | Item persists after reload | |

**Test Design Techniques Used:**
- Scenario-based (happy path)
- Negative test: Try to add an empty item (should show error or do nothing)

---

## R8UC2: Toggle To-Do Item
| Step | Action | Expected Outcome | Condition |
|------|--------|------------------|-----------|
| 1 | Ensure at least one to-do item exists | Item is present in the list | |
| 2 | Click the checkbox/toggle for the item | Item is marked as completed (UI changes) | |
| 3 | Click the checkbox/toggle again | Item is marked as not completed | |

**Test Design Techniques Used:**
- State transition (toggle on/off)
- Negative test: Try toggling a non-existent item (should not crash)

---

## R8UC3: Delete To-Do Item
| Step | Action | Expected Outcome | Condition |
|------|--------|------------------|-----------|
| 1 | Ensure at least one to-do item exists | Item is present in the list | |
| 2 | Click the "Delete" button/icon for the item | Item is removed from the list | |
| 3 | Verify the item is deleted (refresh page) | Item does not reappear | |

**Test Design Techniques Used:**
- Scenario-based (happy path)
- Negative test: Try deleting when the list is empty (should not crash)

---

**References:**
- Tutorial 3: GUI Testing with Cypress (4-step test design technique)
- Lecture: Basics of UI Testing (use-case-driven test design)
