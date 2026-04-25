# Basics of Unit Testing
## PA1417 Lecture Unit 3

## Objectives
**Part I:**
1. What is a unit test?
2. How to create good unit tests?
3. Why writing clean code is important?

**Part II:**
1. How to use PyTest to automate unit tests?
2. How to use coverage to evaluate unit tests?
3. What is mocking?

## Unit testing
Unit testing aims to verify that the smallest meaningful units of the code works as intended. Usually, "unit" refers to a single method or function. Each unit test implements one test case. Typically, you need more than one unit test to make sure the "unit" works correctly.

## What is a good unit test?
1. **Focuses on one unit of code in isolation** (Function, Method). Can verify both functionality and quality.
2. **Implements one test case**. No bundling test cases together. Important when a large number of tests are run in an automated pipeline.
3. **Is independent**. Test result should not depend on the system state, execution order, or anything else not part of the "unit" being tested.
4. **Is trivial**. The simplest implementation is the best.
5. **Has clear pass/fail conditions**.

## Testing clean code is easier
* "Pure" function: return value depends only on parameter values. Does only "one thing". Easy to identify and write test cases. Easy to spot causes for wrong behaviour.
* "Impure" function: depends on random, API values. Does many things. Difficult to identify test cases, difficult to automate. If the behaviour is not what is expected, many things could have gone wrong.

## PyTest framework
The pytest framework makes it easy to write small, readable tests for Python code. Primarily, useful for unit and integration testing. Similar to JUnit, PHPUnit, XUnit, Jest, etc.
pytest provides:
1. Infrastructure for running tests (CLI, automation, CI).
2. Helper functions for writing tests (Fixtures, Comparing composite variables, API for reporting errors).
3. Support for mocking (replacing dependencies with fake objects).

## Important concepts about test automation
* **Assert**: keyword raises a special exception if a condition is not met and prints information in the test log.
* **Test setup (@pytest.fixture)**: sometimes tests need to be set up (preparing DB records, env conditions, system state). After tests, you need to clean up the system.
* **Test parameterization (@pytest.mark.parametrize)**: allows reuse of the same test implementation with different parameters.
* **Mocking (pytest-mock)**: allows you to fake or "mock" your test dependencies making your unit tests independent from APIs, side effects.
