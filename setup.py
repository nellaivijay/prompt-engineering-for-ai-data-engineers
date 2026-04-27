from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prompt-engineering-for-ai-data-engineers",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive course on prompt engineering for AI data engineers with multi-model support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/prompt-engineering-for-ai-data-engineers",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "langchain>=0.1.0",
        "langchain-community>=0.0.20",
        "langchain-openai>=0.0.5",
        "langchain-anthropic>=0.1.0",
        "llama-index>=0.9.0",
        "openai>=1.12.0",
        "anthropic>=0.18.0",
        "google-generativeai>=0.3.0",
        "cohere>=5.0.0",
        "pandas>=2.0.0",
        "polars>=0.20.0",
        "numpy>=1.24.0",
        "pyarrow>=14.0.0",
        "sqlalchemy>=2.0.0",
        "pyyaml>=6.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "black>=23.12.0",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
            "isort>=5.13.0",
            "pre-commit>=3.6.0",
            "bandit>=1.7.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.5.0",
            "jupyter>=1.0.0",
            "nbconvert>=7.14.0",
        ],
        "local": [
            "ollama>=0.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "prompt-engineering=tools.cli:main",
        ],
    },
)
