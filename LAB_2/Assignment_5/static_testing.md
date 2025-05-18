# 2. Static Testing

## 2.1 Explanation of Static Test Techniques vs. Dynamic Test Techniques

**Static test techniques** involve evaluating the system's artifacts (such as code, documentation, and design) without executing the program. Examples include code reviews, static analysis, and inspections. These techniques help identify defects, code smells, and maintainability issues early in the development process. Static testing is especially useful for assessing qualities like maintainability and extensibility, as it allows reviewers to analyze structure, modularity, and adherence to standards. (Source: Lecture "Basics of Non-functional Testing")

**Dynamic test techniques** require executing the system to observe its behavior. This includes unit, integration, system, and acceptance testing. Dynamic tests are essential for verifying functional correctness and runtime qualities such as performance and reliability.

## 2.2 Static Code Review and Extensibility Evaluation

**Static Code Review:**
- The EduTask system is organized into separate frontend and backend components, with clear directory structures and modular code (see `frontend/src/` and `backend/src/`).
- The backend uses Flask blueprints, which support modularity and separation of concerns.
- The frontend is built with React, which encourages component-based design.
- Code is version-controlled with Git, and there is evidence of automated testing and CI support.

**Extensibility Evaluation (regarding adding medium articles):**
- The current backend appears to be designed around YouTube video resources. To support medium articles, the data model and API endpoints would need to be extended to handle a new resource type.
- If the codebase uses generic resource abstractions (e.g., a base class or interface for resources), adding a new type is straightforward. If not, refactoring may be required to avoid code duplication.
- The use of blueprints and modular React components suggests that the system is reasonably extensible, but a review of the data models and API routes is necessary to confirm this.
- Static analysis tools (e.g., linters, type checkers) can help ensure that new code for medium articles integrates cleanly and does not introduce maintainability issues.

**Conclusion:**
- The EduTask system demonstrates good practices for extensibility, but explicit support for new resource types should be verified in the data model and API design. Static testing (code review, static analysis) is recommended before implementing the extension. 