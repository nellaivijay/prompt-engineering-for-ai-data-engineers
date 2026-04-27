# Contributing Guide

Thank you for your interest in contributing to the Prompt Engineering for AI Data Engineers course! This guide will help you get started.

## How to Contribute

### Ways to Contribute

1. **Report Issues**: Found a bug or have a suggestion? [Create an issue](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/issues)
2. **Fix Issues**: Pick an issue and submit a pull request
3. **Add Content**: Add new examples, notebooks, or documentation
4. **Improve Documentation**: Fix typos, improve explanations, add guides
5. **Share Experience**: Write about your use cases in the wiki or discussions

### Getting Started

1. **Fork the Repository**: Click the "Fork" button on GitHub
2. **Clone Your Fork**: 
   ```bash
   git clone https://github.com/YOUR_USERNAME/prompt-engineering-for-ai-data-engineers.git
   cd prompt-engineering-for-ai-data-engineers
   ```
3. **Create a Branch**: 
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes**: Edit files, add content, fix bugs
5. **Test Changes**: Ensure everything works
6. **Commit Changes**: 
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```
7. **Push to GitHub**: 
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create Pull Request**: Go to GitHub and create a PR

## Development Guidelines

### Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Before submitting, run:
```bash
pip install black isort flake8 mypy
black .
isort .
flake8 .
mypy tools/
```

### Pre-commit Hooks

We use pre-commit hooks to automatically check code quality:

```bash
pip install pre-commit
pre-commit install
```

### Testing

Run tests before submitting:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/integration/test_model_backends.py

# Run with coverage
pytest tests/ --cov=tools --cov-report=html
```

### Documentation

If you're adding new features or examples:

1. **Update README**: Add relevant information
2. **Update Wiki**: Add or update wiki pages
3. **Add Comments**: Document complex code
4. **Add Examples**: Include usage examples

## Content Guidelines

### Adding New Notebooks

When adding new notebooks:

1. **Follow naming convention**: `moduleX-topic-name.ipynb`
2. **Include metadata**: Add title, description, and tags
3. **Add documentation**: Explain the purpose and steps
4. **Test thoroughly**: Ensure code runs without errors
5. **Add dependencies**: Update requirements.txt if needed

### Example Notebook Structure

```markdown
# Title of the Notebook

## Description
Brief description of what this notebook demonstrates.

## Prerequisites
- Required knowledge
- Required tools
- Required API keys

## Steps
1. Step 1
2. Step 2
3. Step 3

## Expected Output
Description of what the user should see.

## Notes
Additional notes, tips, or warnings.
```

### Adding Documentation

When adding documentation:

1. **Use clear language**: Avoid jargon when possible
2. **Include examples**: Show, don't just tell
3. **Add diagrams**: Use visuals when helpful
4. **Keep it updated**: Review and update regularly
5. **Add links**: Reference related content

## Pull Request Guidelines

### PR Title Format

Use conventional commit format:
```
Type: Description

Examples:
- Docs: Update getting started guide
- Fix: Resolve API key configuration issue
- Feature: Add support for new model
- Refactor: Improve cost tracker performance
```

### PR Description

Include in your PR:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Changes require documentation update
```

### Review Process

1. **Automated Checks**: CI/CD will run automatically
2. **Code Review**: Maintainers will review your changes
3. **Feedback**: Address any feedback or questions
4. **Approval**: Once approved, your PR will be merged

## Issue Guidelines

### Reporting Bugs

When reporting bugs, include:

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- Python version:
- OS:
- Other relevant info:

## Additional Context
Logs, screenshots, or other helpful information
```

### Suggesting Features

When suggesting features:

```markdown
## Feature Description
Clear description of the feature

## Problem Statement
What problem does this solve?

## Proposed Solution
How should this be implemented?

## Alternatives
What other approaches did you consider?

## Additional Context
Examples, mockups, or other helpful information
```

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

### Communication

- Be clear and concise in issues and PRs
- Ask questions when unsure
- Help others when you can
- Share knowledge and experience

## Recognition

Contributors will be recognized in:

- CONTRIBUTORS.md file
- Release notes
- Project documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Getting Help

If you need help contributing:

1. **Read this guide**: Make sure you understand the process
2. **Check existing issues**: See if someone already asked your question
3. **Join discussions**: Ask questions in GitHub Discussions
4. **Contact maintainers**: Reach out for complex issues

## Resources

- [Main Documentation](https://nellaivijay.github.io/prompt-engineering-for-ai-data-engineers/)
- [GitHub Issues](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/issues)
- [GitHub Discussions](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/discussions)
- [CONTRIBUTING.md](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/blob/main/CONTRIBUTING.md)

---

**Thank you for contributing! 🙏**

**Last Updated**: 2024-04-26