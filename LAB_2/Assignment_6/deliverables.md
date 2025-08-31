# Assignment 6: Continuous Integration - Deliverables

### 1. GitHub Workflow Link 

**File**: `.github/workflows/backend-ci.yml`

**Link**: [Backend CI Workflow](https://github.com/anas26a/bsv-edutask/blob/master/.github/workflows/backend-ci.yml)

**Description**: This workflow automatically executes all backend unit tests when:
- Code is pushed to any branch
- Pull requests are created or updated
- Changes are made to backend files or the workflow itself

**Workflow Configuration**:
```yaml
name: Backend Unit Tests CI
on:
  push:
    paths: ['backend/**', '.github/workflows/backend-ci.yml']
  pull_request:
    paths: ['backend/**', '.github/workflows/backend-ci.yml']
```

### 2. Pull Request Link 

**Pull Request**: [Fix get_user_by_email method and add CI workflow](https://github.com/anas26a/bsv-edutask/pull/X)
