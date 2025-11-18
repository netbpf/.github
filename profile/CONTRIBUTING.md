# Contributing to NETBPF Projects

Thank you for your interest in contributing to NETBPF! We welcome all contributions, including bug reports, feature requests, documentation improvements, and code contributions.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contributions](#code-contributions)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [License](#license)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/your-username/repository.git
   cd repository
   ```
3. **Add the upstream repository**
   ```bash
   git remote add upstream https://github.com/netbpf/repository.git
   ```
4. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```
5. **Set up the development environment** (check project's README for specific requirements)

## How to Contribute

### Reporting Bugs

- Check if the bug has already been reported in the [issues](https://github.com/netbpf/.github/issues)
- If not, create a new issue with a clear title and description
- Include steps to reproduce the bug, expected behavior, and actual behavior
- Add any relevant logs or screenshots

### Suggesting Enhancements

- Check if the enhancement has already been suggested
- Create a new issue with a clear title and description
- Explain why this enhancement would be useful
- Include any design documents or references if applicable

### Code Contributions

1. **Start with an issue** - Discuss your proposed changes before writing code
2. **Follow the coding standards** (see below)
3. **Write tests** for your changes
4. **Update documentation** as needed
5. **Ensure all tests pass** before submitting a pull request

## Development Workflow

1. **Sync with upstream**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and commit them
   ```bash
   git add .
   git commit -m "Your detailed commit message"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build
2. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations, and container parameters
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent
4. You may merge the Pull Request once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you

## Coding Standards

- Follow the existing code style of the project
- Include comments for complex logic
- Write clear commit messages in the present tense
- Keep pull requests focused on a single feature or bug fix
- Update documentation along with code changes

## License

By contributing, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE) file.
