# 1. Qualities

## 1.1 Why Explicit Definition is Necessary Before Testing

An explicit definition of a quality is necessary before testing because it provides a clear, measurable target for the test process. Without a precise definition, tests may be subjective, inconsistent, or fail to address stakeholder needs. Defining the quality ensures that all team members have a shared understanding of what is being evaluated, allows for the selection of appropriate test techniques, and enables objective assessment of whether the system meets its non-functional requirements. (Source: Lecture "Basics of Non-functional Testing")

## 1.2 Explicit Definitions of Three Qualities

- **Accessibility:** The degree to which the system can be used by people with a wide range of abilities and disabilities, including those with visual, auditory, motor, or cognitive impairments. Accessibility ensures that all users can perceive, understand, navigate, and interact with the system effectively. (Source: Lecture "Basics of UI Testing")

- **Maintainability:** The ease with which the system can be modified to correct defects, improve performance, or adapt to a changed environment. Maintainability includes aspects such as code readability, modularity, documentation, and the presence of automated tests. (Source: Lecture "Basics of Non-functional Testing")

- **Reliability:** The probability that the system will perform its intended functions without failure under specified conditions for a specified period of time. Reliability focuses on consistent, error-free operation and the system's ability to handle errors gracefully. (Source: Lecture "Basics of Non-functional Testing")

## 1.3 Potential Test Techniques for Each Quality

- **Accessibility:**
  - Use automated accessibility checkers (e.g., axe, Lighthouse) to scan for WCAG violations.
  - Conduct manual testing with screen readers and keyboard navigation.
  - Review color contrast and alternative text for images.

- **Maintainability:**
  - Perform static code analysis to check for code smells, complexity, and adherence to coding standards.
  - Review code modularity and documentation.
  - Evaluate the presence and quality of automated tests and CI pipelines.

- **Reliability:**
  - Execute automated test suites (unit, integration, E2E) to ensure consistent behavior.
  - Use fault injection and stress testing to observe system behavior under failure conditions.
  - Monitor system logs and error rates during operation.
