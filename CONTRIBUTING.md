# Contributing to CmdCalc
Thank you for considering contributing to CmdCalc, an open-source command-line calculator project. This guide outlines the steps and expectations for contributing to the project.

## Getting Started
To start contributing, you'll need to fork and clone the repository. Here's a step-by-step guide:

1. **Fork the repository**: Go to the [CmdCalc repository](https://github.com/your-username/CmdCalc) and click the "Fork" button in the top-right corner. This will create a copy of the repository in your own GitHub account.
2. **Clone the repository**: Run the following command in your terminal to clone the repository to your local machine:
   ```bash
git clone https://github.com/your-username/CmdCalc.git
```
3. **Navigate to the repository**: Change into the cloned repository:
   ```bash
cd CmdCalc
```
4. **Create a new branch**: Create a new branch for your feature or bug fix. We use the following branch naming convention:
   * `feature/<feature-name>` for new features
   * `fix/<bug-description>` for bug fixes
   * `docs/<documentation-change>` for documentation changes
   * `refactor/<code-refactor>` for code refactoring
   Example:
   ```bash
git checkout -b feature/add-new-trigonometric-function
```

## Pull Request Expectations
When submitting a pull request, please ensure that:

* Your code is formatted according to our code style guidelines (see below)
* Your changes are thoroughly tested and include any necessary test cases
* Your pull request includes a clear and concise description of the changes made
* Your pull request is targeted at the `main` branch

## Code Style Expectations
We follow the standard professional guidelines for code style, with a few additional rules:

* Use 4 spaces for indentation
* Use meaningful variable names and follow the camelCase convention
* Keep functions short and focused on a single task
* Use comments to explain complex logic or algorithms
* Use Markdown formatting for documentation and comments

Example of good code style:
```python
def calculate_trigonometric_function(angle):
    # Calculate the sine of the angle
    sine = math.sin(angle)
    return sine
```

## Issue Reporting Guidance
If you encounter a bug or have a feature request, please follow these steps:

1. **Check the existing issues**: Search the [issue tracker](https://github.com/your-username/CmdCalc/issues) to see if the issue has already been reported.
2. **Create a new issue**: If the issue is not already reported, create a new issue with a clear and concise description of the problem or feature request.
3. **Provide relevant information**: Include any relevant information, such as:
	* The version of CmdCalc you are using
	* The operating system and platform you are running on
	* Any error messages or output
	* Steps to reproduce the issue (if applicable)

Example of a good issue report:
```markdown
### Issue Description
The `calculate_trigonometric_function` function is returning incorrect results for certain input values.

### Steps to Reproduce
1. Run the `calculate_trigonometric_function` function with an input angle of 30 degrees.
2. Verify that the result is incorrect.

### Expected Result
The result should be the correct sine value for the input angle.

### Actual Result
The result is an incorrect value.
```

## Commit Message Guidelines
When committing changes, please follow the standard professional guidelines for commit messages:

* Use the imperative mood (e.g., "Add new trigonometric function" instead of "Added new trigonometric function")
* Keep the first line concise and focused on the main change
* Use a blank line to separate the brief summary from the body of the commit message
* Use bullet points to list multiple changes or features

Example of a good commit message:
```
Add new trigonometric function

* Implement the `calculate_trigonometric_function` function
* Add test cases for the new function
* Update documentation to reflect the new feature
```

By following these guidelines, you'll be helping us maintain a high-quality and consistent codebase. Thank you again for considering contributing to CmdCalc!