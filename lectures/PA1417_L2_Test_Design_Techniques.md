# Test Design Techniques
## PA1417 Lecture Unit 2

## Objectives of the lecture
In this lecture you will learn the building blocks of designing test cases. We will look at:
* Components of a test case
* How to determine what test cases you need
* Relevant techniques and approaches
Test case design is one of the core elements in this course and you have to apply the technique in every assignment.

## Test cases
What is a test case? A test case is a concise description of a single test. At minimum it contains the following:
* **ID**: a unique identifier of the test case
* **Action**: an activity (e.g., method) of the system under test that we evaluate
* **Inputs**: the list of conditions that represent the situation
* **Expected outcome**: the behavior the system is expected to exhibit given the inputs

## Ground truth and the test oracle
A test case has to be derived from some sort of ground truth which tells you how the system should behave. Sources for ground truth are:
1. A requirements specification/documentation
2. The context, i.e., an understanding of a system's purpose
3. Domain knowledge
4. Stakeholders
5. Assume the code is correct, write a test that confirms it (anti-pattern)

Do not test what the system does, test what it should do! Be explicit about your assumptions and talk to your stakeholders!

## Test case design
Knowing the ground truth, how do you determine all the relevant input values? There are several options:
1. **Try random values (monkey/ad-hoc testing)**: Not systematic, rarely deliver useful results.
2. **Try all the values (exhaustive testing)**: Most throughout, but impossible in most scenarios involving broad data types.
3. **Try values around important thresholds (Boundary value analysis)**.
4. **Try values that produce different outputs (Equivalence partitioning)**.

### Boundary value analysis (BVA)
A software testing technique in which tests are designed to include representatives of boundary values in a range. A boundary is a threshold in inputs that changes how the system/code behaves.
Boundaries usually can be identified in:
* Branching conditions
* Loops
* Limits of data types (length of arrays, min/max values)
Idea: Take the boundary value a and a+1, a-1 values.

### Equivalence partitioning (EP)
A software testing technique that divides the input data of a software unit into partitions of equivalent data from which test cases can be derived.
Idea: Look for ranges of values that produce the same output and pick one value from each range. EP is often used in combination with BVA.

## The 4-step test design technique
For a given scenario, the test design technique systematically elicits a test suite. It consists of the following steps:
1. **Identify actions and expected outcomes**: find all interaction of an external actor within the SUT.
2. **Identify conditions**: find all conditions (parameters, system state, ...) on which the outcome of the actions depends on. Use BVA and EP for continuous input variables.
3. **Determine combinations**: construct either all combinations or filter for relevant combinations based on domain knowledge.
4. **Denote expected outcomes**: for each constructed combination, derive the expected outcome based on the ground truth.

## Test coverage
We produced test cases, but how can we be sure that our system-under-test has been sufficiently tested?
* **Branch coverage**: calculates how many branches of a control flow graph are executed during the test. Full branch coverage is achieved if the test cases cover all the possible outcomes (true and false) of each condition at least once.
* **Statement coverage**: calculates how many statements are executed during the test. Make sure each line of your code is executed at least once.

When following the test design technique, full coverage should be implied.

## Summary
1. Test design technique (actions, conditions, combinations, outcomes) is one of the fundamental learning outcomes of this course.
2. Always test what the code is supposed to do, not what it does.
3. EP/BVA are useful methods to avoid monkey-testing.
4. 100% test coverage is the goal, however it does not imply your code is 100% correct.
