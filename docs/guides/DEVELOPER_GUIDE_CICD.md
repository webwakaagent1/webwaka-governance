# Developer Guide: CI/CD and Automated Testing

**Document ID:** DEV_GUIDE_CICD  
**Phase:** PF-4  
**Status:** ✅ **Active**  
**Date:** January 31, 2026  
**Author:** Manus AI

---

## 1. Introduction

This guide provides developers with everything they need to know about the automated testing and CI/CD infrastructure for the WebWaka platform. Our CI/CD pipelines are built on GitHub Actions and are designed to help you ship high-quality code faster.

---

## 2. Running Tests Locally

Before pushing your code, you should always run tests locally to catch issues early.

### 2.1. Running All Tests in a Repository

To run all tests for all implementations within a repository:

```bash
# Navigate to the repository root
cd webwaka-core-services

# Run tests for all implementations
for d in implementations/*/; do (cd "$d" && npm test); done
```

### 2.2. Running Tests for a Single Implementation

To run tests for a specific implementation:

```bash
# Navigate to the implementation directory
cd webwaka-core-services/implementations/CS-1

# Run tests
npm test
```

### 2.3. Running Tests with Coverage

To check your code coverage locally:

```bash
npm test -- --coverage
```

This will generate a coverage report in the `coverage/` directory.

---

## 3. Understanding the CI/CD Pipeline

Our CI/CD pipeline is composed of several workflows that run automatically.

### 3.1. Test Workflow (`test.yml`)

- **When it runs:** On every push and pull request.
- **What it does:** Runs the full test suite for all implementations in the repository.
- **Why it matters:** Provides fast feedback on whether your changes have broken any existing tests.

### 3.2. CI Workflow (`ci.yml`)

- **When it runs:** On pull requests to the `main` branch.
- **What it does:** Performs a comprehensive set of quality checks.
- **Why it matters:** This is the main quality gate that ensures only high-quality code is merged.

---

## 4. The Pull Request (PR) Process

1. **Create a PR:** When your feature is ready, create a pull request targeting the `main` branch.
2. **CI Checks Run:** The `test` and `ci` workflows will run automatically.
3. **Review Checks:** Check the "Checks" tab on your PR to see the status of each job.
4. **Fix Issues:** If any checks fail, review the logs, fix the issues locally, and push the changes to your branch. The checks will re-run automatically.
5. **Get Approval:** Once all checks are passing, request a review from your team lead.
6. **Merge:** After approval, you can merge your PR into the `main` branch.

---

## 5. Troubleshooting CI/CD Failures

### 5.1. Test Failures

- **Symptom:** The `test` job fails.
- **Solution:**
  1. Click "Details" next to the failing job to view the logs.
  2. Identify the failing test and the error message.
  3. Run the failing test locally to reproduce the issue.
  4. Fix the test and push your changes.

### 5.2. Linting Failures

- **Symptom:** The `lint` job fails.
- **Solution:**
  1. Review the logs to see which linting rules are being violated.
  2. Run `npm run lint` locally to see the errors.
  3. Fix the linting issues (many can be fixed automatically with `npm run lint -- --fix`).

### 5.3. Coverage Failures

- **Symptom:** The `coverage-check` job fails.
- **Solution:**
  1. Your code does not meet the 70% coverage threshold.
  2. Run `npm test -- --coverage` locally to view the coverage report.
  3. Identify the files with low coverage and add more tests.

---

## 6. Quality Gate Policies

- **Code Coverage:** Minimum 70% for lines, branches, functions, and statements.
- **Linting:** No ESLint errors.
- **Security:** No high or critical vulnerabilities from `npm audit`.
- **Type Safety:** No TypeScript errors.

---

## 7. Best Practices

- **Run tests locally before pushing.**
- **Keep your PRs small and focused.**
- **Write tests for all new code.**
- **Do not ignore failing tests.**
- **Review workflow logs carefully to understand failures.**

---

**Guide Status:** ✅ **Active**
