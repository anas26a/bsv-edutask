# 2. Static Testing

## 2.1 Explanation of Static Test Techniques vs. Dynamic Test Techniques

**Static test techniques** involve evaluating the system's artifacts (such as code, documentation, and design) without executing the program. Examples include code reviews, static analysis, and inspections. These techniques help identify defects, code smells, and maintainability issues early in the development process. Static testing is especially useful for assessing qualities like maintainability and extensibility, as it allows reviewers to analyze structure, modularity, and adherence to standards. (Source: Lecture "Basics of Non-functional Testing")

**Dynamic test techniques** require executing the system to observe its behavior. This includes unit, integration, system, and acceptance testing. Dynamic tests are essential for verifying functional correctness and runtime qualities such as performance and reliability.

## 2.2 Static Code Review and Extensibility Evaluation

**Static Code Review:**

The EduTask system is organized into separate frontend and backend components, with clear directory structures and modular code (see `frontend/src/` and `backend/src/`).

**Backend Analysis:**
- The backend uses Flask blueprints, which support modularity and separation of concerns.
- The backend is organized into controllers, blueprints, and utility modules.
- Code is version-controlled with Git, and there is evidence of automated testing and CI support.

**Frontend Analysis (Critical for Extensibility Assessment):**

The frontend contains several critical aspects that significantly impact extensibility:

1. **Hardcoded YouTube Video Handling in TaskDetail.js:**
```javascript:frontend/src/Components/TaskDetail.js
<a href={`https://www.youtube.com/watch?v=${task.url}`} target='_blank' rel="noreferrer">
    <img src={`http://i3.ytimg.com/vi/${task.url}/hqdefault.jpg`} alt='' />
</a>
```
This code assumes all resources are YouTube videos, making it impossible to support other resource types like Medium articles without significant refactoring.

2. **Resource Type Assumptions in TaskDetail.js:**
```javascript:frontend/src/Components/TaskDetail.js
// The component expects task.url to be a YouTube video ID
// This creates tight coupling between the frontend and YouTube-specific functionality
```

3. **Backend Controller Hardcoding in taskcontroller.py:**
```python:backend/src/controllers/taskcontroller.py
# add the video url
video = self.videos_dao.create({'url': data['url']})
del data['url']
data['video'] = ObjectId(video['_id']['$oid'])
```
The backend controller explicitly creates video objects, making it difficult to extend to other resource types.

4. **Data Model Coupling:**
The current data model tightly couples tasks with videos, as seen in the `populate_task` method:
```python:backend/src/controllers/taskcontroller.py
# populate the video of the task
video = self.videos_dao.findOne(task['video']['$oid'])
task['video'] = video
```

**Extensibility Evaluation (regarding adding medium articles):**

**Critical Frontend Limitations:**
- **Resource Type Hardcoding**: The frontend components are hardcoded to expect YouTube video URLs and generate YouTube-specific UI elements (thumbnails, links).
- **Component Coupling**: The `TaskDetail` component directly embeds YouTube-specific logic, making it impossible to display Medium articles without component modification.
- **URL Processing**: The frontend assumes all URLs are YouTube video IDs and generates YouTube-specific URLs and thumbnail images.

**Backend Limitations:**
- **Resource Type Coupling**: The backend explicitly creates video objects and assumes all resources are videos.
- **Data Model Rigidity**: The task model has a hardcoded `video` field instead of a generic `resource` field.
- **Controller Specialization**: The `TaskController` is specifically designed for video resources.

**Required Changes for Medium Article Support:**

1. **Frontend Refactoring:**
   - Create a generic `ResourceDisplay` component that can handle different resource types
   - Implement resource type detection and appropriate rendering logic
   - Remove hardcoded YouTube assumptions from `TaskDetail.js`

2. **Backend Refactoring:**
   - Introduce a generic `Resource` model/interface
   - Modify the task model to use a generic `resource` field instead of `video`
   - Update controllers to handle different resource types polymorphically
   - Create resource-specific DAOs for different content types

3. **Data Migration:**
   - Existing tasks with video resources would need migration to the new generic structure
   - Database schema updates would be required

**Conclusion:**
The EduTask system demonstrates **poor extensibility** for adding new resource types like Medium articles. The frontend contains the most critical extensibility impediments through hardcoded YouTube assumptions and tight coupling between components and resource types. The backend also shows significant coupling to video resources. Adding Medium article support would require substantial refactoring of both frontend and backend components, indicating that the current architecture does not follow good extensibility principles.

**Recommendations:**
- Implement a generic resource abstraction layer
- Use dependency injection for resource handling
- Create resource type-specific renderers in the frontend
- Refactor the data model to be resource-agnostic
- Implement a resource factory pattern for creating different resource types 