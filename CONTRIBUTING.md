# Contributing to Prompt Engineering for AI Data Engineers

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing effectively.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Documentation Standards](#documentation-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## Code of Conduct

This project adheres to a code of conduct that all contributors must follow. By participating, you are expected to uphold this standard. Please report unacceptable behavior to the project maintainers.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Basic knowledge of data engineering concepts
- Familiarity with AI/LLM concepts

### Setup Development Environment

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment
4. Install development dependencies

```bash
# Clone your fork
git clone https://github.com/your-username/prompt-engineering-for-ai-data-engineers.git
cd prompt-engineering-for-ai-data-engineers

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e ".[dev]"
```

## Development Workflow

### Branch Strategy

- `main`: Production-ready code
- `develop`: Development branch
- `feature/*`: Feature branches
- `bugfix/*`: Bug fix branches
- `docs/*`: Documentation updates

### Creating a Branch

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### Making Changes

1. Make your changes on the feature branch
2. Follow coding standards (see below)
3. Write tests for new functionality
4. Update documentation as needed
5. Commit your changes with clear messages

### Commit Message Format

Use clear, descriptive commit messages:

```
type: brief description

Detailed description of the change, including:
- What was changed
- Why it was changed
- Any relevant context

Closes #issue-number
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

## Coding Standards

### Python Code Style

- Follow PEP 8 guidelines
- Use Black for code formatting
- Use isort for import sorting
- Maximum line length: 100 characters
- Use type hints where appropriate

### Code Quality

- Run flake8 for linting
- Use mypy for type checking
- Write docstrings for all functions and classes
- Follow the Google Python Style Guide for docstrings

### Example Code Structure

```python
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ExampleClass:
    """Brief description of the class.
    
    Longer description providing context about the class's purpose
    and usage.
    
    Attributes:
        attribute1: Description of attribute1
        attribute2: Description of attribute2
    """
    
    attribute1: str
    attribute2: int
    
    def example_method(self, param: str) -> Dict[str, str]:
        """Brief description of the method.
        
        Args:
            param: Description of parameter
            
        Returns:
            Dictionary with results
            
        Raises:
            ValueError: If param is invalid
        """
        if not param:
            raise ValueError("Parameter cannot be empty")
        
        return {"result": param}
```

### Security Guidelines

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Follow security best practices
- Run security scans before committing

## Documentation Standards

### Documentation Format

- Use Markdown for all documentation
- Follow the existing documentation structure
- Include code examples in documentation
- Use clear, concise language

### Documentation Structure

```markdown
# Title

Brief description of what this documentation covers.

## Section

Content with examples.

### Subsection

More detailed content.

## Code Example

```python
# Example code
```

## Notes

Additional information or warnings.
```

### Notebook Standards

- Include clear explanations in markdown cells
- Add comments in code cells
- Use descriptive variable names
- Include expected outputs
- Test all code before committing

## Testing Guidelines

### Test Structure

```python
import pytest
from tools.example_module import ExampleClass


class TestExampleClass:
    """Test suite for ExampleClass."""
    
    def test_initialization(self):
        """Test that ExampleClass initializes correctly."""
        example = ExampleClass(attribute1="test", attribute2=42)
        assert example.attribute1 == "test"
        assert example.attribute2 == 42
    
    def test_example_method(self):
        """Test the example method."""
        example = ExampleClass(attribute1="test", attribute2=42)
        result = example.example_method("input")
        assert result == {"result": "input"}
    
    def test_invalid_parameter(self):
        """Test that invalid parameters raise ValueError."""
        example = ExampleClass(attribute1="test", attribute2=42)
        with pytest.raises(ValueError):
            example.example_method("")
```

### Testing Requirements

- Write tests for all new functionality
- Maintain test coverage above 80%
- Use pytest for testing
- Mock external API calls
- Test both success and failure cases

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tools --cov-report=html

# Run specific test file
pytest tests/test_example.py

# Run specific test
pytest tests/test_example.py::TestExampleClass::test_initialization
```

## Pull Request Process

### Before Submitting

1. Ensure all tests pass
2. Update documentation
3. Add tests for new features
4. Run code quality checks
5. Update CHANGELOG if appropriate

### PR Description Template

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

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] No new warnings generated
- [ ] Added tests that prove fix is effective
- [ ] All tests passing
```

### PR Review Process

1. Automated checks must pass
2. At least one maintainer approval required
3. Address all review comments
4. Keep PRs focused and small
5. Squash commits before merging

## Issue Reporting

### Bug Reports

Include the following information:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages/stack traces
- Sample code if applicable

### Feature Requests

- Clear description of the feature
- Use case for the feature
- Potential implementation approach
- Examples of similar features in other projects

### Documentation Issues

- Specific section with issues
- Suggested improvements
- Examples of better documentation

## Community Guidelines

### Communication

- Be respectful and constructive
- Focus on what is best for the community
- Show empathy towards other community members
- Accept feedback gracefully

### Collaboration

- Work transparently
- Share knowledge freely
- Help newcomers get started
- Recognize contributions from others

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## Additional Resources

- [Project Documentation](README.md)
- [Getting Started Guide](GETTING_STARTED.md)
- [Model Guide](MODEL_GUIDE.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

## Questions?

Feel free to open an issue for questions about contributing or contact the maintainers directly.

---

Thank you for contributing to Prompt Engineering for AI Data Engineers!
