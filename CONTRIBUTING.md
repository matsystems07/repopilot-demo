# Contributing to Student Expense Tracker
The Student Expense Tracker is an open-source project that aims to help students manage their expenses effectively. We welcome contributions from the community to make this project better. Here's a guide on how to contribute to the project.

## Getting Started
To contribute to the project, you'll need to fork and clone the repository. Here are the steps:

1. **Fork the repository**: Go to the [Student Expense Tracker repository](https://github.com/your-username/Student-Expense-Tracker) and click the "Fork" button in the top-right corner.
2. **Clone the repository**: Run the following command in your terminal:
   ```bash
git clone https://github.com/your-username/Student-Expense-Tracker.git
```
3. **Navigate to the repository**: Run the following command:
   ```bash
cd Student-Expense-Tracker
```
4. **Add the upstream repository**: Run the following command:
   ```bash
git remote add upstream https://github.com/original-username/Student-Expense-Tracker.git
```

## Branching
When making changes, create a new branch from the `main` branch. Use the following naming convention for your branch:

* `feature/your-feature-name` for new features
* `fix/your-fix-name` for bug fixes
* `docs/your-docs-name` for documentation changes
* `refactor/your-refactor-name` for code refactoring

Example:
```bash
git checkout -b feature/add-expense-category
```

## Pull Requests
When you're ready to submit your changes, create a pull request against the `main` branch. Here are some expectations:

* **Clear and concise title**: Use a descriptive title that summarizes the changes.
* **Detailed description**: Provide a detailed description of the changes, including any relevant context or explanations.
* **Related issues**: If your pull request fixes an issue, include the issue number in the description.
* **Code formatting**: Ensure that your code is formatted consistently with the rest of the project.

## Code Style
We follow standard professional guidelines for code style. Here are some key points:

* **Indentation**: Use 4 spaces for indentation.
* **Line length**: Keep lines under 80 characters.
* **Variable naming**: Use descriptive and concise variable names.
* **Function naming**: Use descriptive and concise function names.

## Issue Reporting
If you find a bug or have a feature request, please create an issue on the [issue tracker](https://github.com/your-username/Student-Expense-Tracker/issues). Here are some guidelines:

* **Clear and concise title**: Use a descriptive title that summarizes the issue.
* **Detailed description**: Provide a detailed description of the issue, including any relevant context or explanations.
* **Steps to reproduce**: Provide steps to reproduce the issue, if applicable.
* **Expected behavior**: Describe the expected behavior.

## Commit Messages
When committing changes, use the following format for your commit message:

`type: brief description`

* `type` can be one of:
	+ `feat` for new features
	+ `fix` for bug fixes
	+ `docs` for documentation changes
	+ `refactor` for code refactoring
	+ `test` for test additions or changes
	+ `chore` for miscellaneous changes

Example:
```bash
git commit -m "feat: add expense category feature"
```

By following these guidelines, you'll be helping us maintain a high-quality and consistent codebase. Thank you for contributing to the Student Expense Tracker!