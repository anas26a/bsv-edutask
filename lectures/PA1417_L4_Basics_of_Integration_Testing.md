# Basics of Integration Testing
## PA1417 Lecture Unit 4

## Objective
Today, in the first part, you will learn about integration testing and how to go about covering a system with low level tests. In the second part, we will dive back into Live Coding with some more concepts.

## Integration testing
Integration testing verifies whether individual software modules work together as a group.
Unit testing verifies each module in isolation. Integration testing focuses on making sure the two modules know how to talk to each other.

**Examples of integration:**
* Web backend & frontend
* Mobile app and backend API
* Reading/writing data to a database
* Reading file from a disk
* Calling Google Weather API
* One microservice calling another

## Integration test cases
Similar to unit tests. Focus on the communication between pairs of modules. Mock everything else. Boundary value analysis and equivalence partitioning still apply.
Examples:
1. Save and retrieve valid user data from the DB
2. Save and retrieve invalid user data from the DB
3. Try saving/retrieving data when DB is not available

## Black-box vs white-box testing
For integration testing you do not need to know how the other system is implemented. Focus on the API not the implementation. Follow specifications.
Example: To verify if your application can save results to the database you do not need to know how the DB engine is implemented. The DB server is a black-box, you assume it works. DB schema, SQL language, are your specifications.

## Causes of issues
Defects in the integration may arise from:
* Wrongly implemented API (client or server)
* Poor error handling
* Incompatible library versions
* Communication disruption
* Poorly communicated changes, one module updated without notifying another
* System robustness: Errors need to be handled gracefully! A defect in one module should not crash the whole system.

## Continuous Integration (CI)
Unit and integration tests are often used in an automated CI/CD pipeline:
1. Developer pushes changes to a repository.
2. CI (Jenkins, CircleCI, TeamCity) tool automatically takes the changes, creates test environment (Docker).
3. Builds everything, runs unit + integration tests.
4. If successful, the new code is approved and merged to master.
5. If unsuccessful, the merge is rejected and sent back to the developer along with the test report.

## Mocking revisited
Mocking is the process of substituting a part of the system for a mock (also called stub), which simulates the behavior of that part of the system.
**Reasons for Mocking:**
* Isolating the SUT
* Not yet implemented Dependency
* Non-deterministic calculation
* Expensive/dangerous unit

### Dependency injection vs hard-coded dependencies
* **Dependency injection**: The superordinate caller creates the dependency. The dependency is injected by the superordinate caller.
* **Hard-coded dependencies**: The superordinate caller creates the module without knowledge about its dependency. The dependency is hard-coded and established by the module itself.

### Mocking hard-coded dependencies with patch
You can use `@patch` from `unittest.mock` to mock hard-coded dependencies by patching the object in the namespace of the SUT. You can also patch impure functions (like `random.randint`).

### Fixture Cleanup
Use `yield` instead of `return` in a pytest fixture to execute cleanup code after the test is completed.
