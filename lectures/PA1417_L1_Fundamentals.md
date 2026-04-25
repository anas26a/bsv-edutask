# Fundamentals
## PA1417 Lecture Unit 1

## Agenda
In this lecture we will cover some key concepts that are needed to understand the rest of the course.
* What is testing and why it is important?
* What are test activities?
* What are different levels of tests?

## Background
Software is part of nearly every product and service, either embedded in it or critical for manufacturing/logistics/back office functions. When software does not work as intended, it may cause inconvenience, damage to business, financial loss, injury and death.

**Few notorious examples:**
* Heathrow disruption (Feb 2020)
* Facebook/Instagram/WhatsApp outage (July 2019)
* Ariane 5 rocket explosion (June 1996 - cost $370m)
* CrowdStrike update chaos (July 2024)
* Boeing 737 MAX disaster

## Why do defects happen?
* Software is complex
  * Changing requirements and evolving software
  * Large size, internal dependencies
* Software development process is complex
  * Not enough time and resources for thorough design and testing
  * Poor planning
  * Lack of accountability, training
  * Issues in communication and coordination
* Human nature
  * Lack of experience
  * Carelessness
  * Human errors

## Defects, bugs, errors, failures?
* **Error**: Human-centric, e.g., misunderstandings, lack of knowledge.
* **Defect**: Flaws in the software itself, e.g., wrong branching conditions.
* **Failure**: Deviation of the system's behavior from the expectation, e.g., wrong calculation, system crash.

The purpose of testing is to find defects. A good test is one that fails (Keep this in mind when writing your own tests). Discipline and process is important to catch defects as soon as they are introduced.

## What testing can and cannot do?
**Testing can:**
* Reduce costs to remove defects (Removing a bug while in early stages of development is relatively cheap. It is much more expensive to fix it late or in production).
* Reduce chances of adverse effects (Injury, financial damage, suboptimal customer experience).
* Show where defects are.

**Testing cannot:**
* Prove that there are no defects left. No matter how much we test, we cannot be certain that there are no remaining defects.
* Find a cause and fix the defect (that is debugging).

## Different standards for different systems
* **Safety-critical**: failures cause harm to the life of people (e.g., autopilot on an airplane, MRI). Necessitates most robust, meticulous testing. External audits & independent verification.
* **Business-critical**: failures cause harm to a business (e.g., online store, Steam client). Necessitates rigorous testing.
* **Non-critical**: neither of the above (e.g., a meme generator). Is content with good-enough testing.

## Levels of testing, test pyramid
* **Low level** (cheap, easy to run):
  * Unit testing: Test if methods/functions behave correctly.
  * Integration testing: Test if interfaces and communication behave correctly.
* **Middle level**:
  * Scenario testing: can the software execute some steps of a function correctly.
  * GUI testing: does it look and feel right?
  * Quality testing: performance, security, reliability.
* **High level** (large, time consuming):
  * End-to-end system testing
  * Acceptance testing
  * Smoke testing

## How to know how much testing is needed?
* It is impossible to find all defects.
* We can only write a finite number of test cases.
* FOCUS on tests with the greatest value/impact if fail.

## Fundamental test activities
Testing is a process, often iterative, and should be aligned with the overall development approach.
1. **Planning and Control**: decide on what, how, and how much to test. What are success/failure thresholds, testing objectives, schedule, etc.
2. **Analysis and Design**: analyze requirements, design test cases.
3. **Implementation and Execution**: implement and run tests.
4. **Evaluating exit criteria and reporting**: compile & report results to other stakeholders.
5. **Test Closure activities**: check and package for handover to maintenance and archiving.

## Test case design
Most of this course will be about how to design and implement good test cases.
A test case is a concise description of:
* What is the initial state
* What are the inputs
* Expected output

Goals of test design:
* to have a maximum benefit with the least number of test cases.
* to have confidence in the test results.

## Conclusion
* Software is complex and evolving, it is practically impossible to make it perfect.
* Errors -> Defects -> Failures
* Different software have different quality standards.
* Tests on different levels ensure both overall behaviour and small details are covered.
* Tests can contain defects as well, in this course, we will learn how to create good and reliable tests by design.
