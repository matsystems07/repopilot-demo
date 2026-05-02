# Contributing to Crusteez Donut Website
Thank you for considering contributing to the Crusteez Donut Website! We're excited to have you on board. This guide will walk you through the process of contributing to our project.

## Getting Started
To start contributing, you'll need to fork and clone our repository. Here's a step-by-step guide:

1. **Fork the repository**: Go to the [Crusteez Donut Website repository](https://github.com/crusteez/crusteez-donut-website) and click the "Fork" button in the top-right corner.
2. **Clone the repository**: Run the following command in your terminal, replacing `your-username` with your actual GitHub username:
   ```bash
git clone https://github.com/your-username/crusteez-donut-website.git
```
3. **Navigate to the repository**: Change into the cloned repository:
   ```bash
cd crusteez-donut-website
```

## Branching
When making changes, create a new branch to keep your work separate from the main codebase. We follow a simple branch naming convention:

* **Feature branches**: Use `feature/` followed by a brief description of the feature (e.g., `feature/add-donut-filtering`)
* **Bug fix branches**: Use `fix/` followed by a brief description of the bug fix (e.g., `fix/donut-image-loading-issue`)
* **Documentation branches**: Use `docs/` followed by a brief description of the documentation change (e.g., `docs/update-contributing-guidelines`)

Create a new branch using the following command:
```bash
git checkout -b feature/your-branch-name
```
Replace `your-branch-name` with the actual name of your branch.

## Pull Requests
When you're ready to submit your changes, create a pull request against the `main` branch. Here's what we expect from a pull request:

* **Clear title**: Use a concise and descriptive title that summarizes the changes.
* **Detailed description**: Provide a detailed description of the changes, including any relevant context or explanations.
* **Related issues**: If your pull request fixes an issue, include the issue number in the description (e.g., "Fixes #123").
* **Code formatting**: Ensure your code is formatted consistently with the rest of the project.

To create a pull request, push your changes to your fork and then submit a pull request through the GitHub interface.

## Code Style
We follow standard professional guidelines for code style. Here are some key expectations:

* **Indentation**: Use 2 spaces for indentation.
* **Line length**: Keep lines under 80 characters.
* **Variable naming**: Use descriptive and concise variable names.
* **Function naming**: Use descriptive and concise function names.
* **Commenting**: Use comments to explain complex logic or algorithms.

We use [ESLint](https://eslint.org/) to enforce code style. You can run `npm run lint` to check your code for style issues.

## Issue Reporting
If you encounter an issue with the project, please report it using our issue tracker. Here's how:

1. **Check existing issues**: Search the issue tracker to see if the issue has already been reported.
2. **Create a new issue**: If the issue is not already reported, create a new issue with a clear and descriptive title.
3. **Provide context**: Include any relevant context, such as:
	* Steps to reproduce the issue
	* Expected behavior
	* Actual behavior
	* Any error messages or logs
4. **Label the issue**: Use the provided labels to categorize the issue (e.g., "bug", "feature request", etc.).

By following these guidelines, you'll help us maintain a high-quality and consistent codebase. Thank you again for contributing to the Crusteez Donut Website!