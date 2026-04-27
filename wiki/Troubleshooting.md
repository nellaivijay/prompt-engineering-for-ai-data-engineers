# Troubleshooting Guide

This guide covers common issues and their solutions when working with the Prompt Engineering for AI Data Engineers course.

## Installation Issues

### Python Version Errors

**Problem**: `Python 3.9+ is required` error

**Solutions**:
```bash
# Check your Python version
python --version

# Install Python 3.11 using pyenv (macOS/Linux)
pyenv install 3.11.0
pyenv global 3.11.0

# Or use conda
conda create -n prompt-engineering python=3.11
conda activate prompt-engineering
```

### Dependency Installation Failures

**Problem**: `pip install` fails with dependency conflicts

**Solutions**:
```bash
# Upgrade pip first
pip install --upgrade pip

# Try using UV (faster)
pip install uv
uv pip install -r requirements.txt

# Or use conda
conda install --file requirements.txt
```

### Virtual Environment Issues

**Problem**: Virtual environment not activating or packages not found

**Solutions**:
```bash
# Deactivate and recreate
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## API Configuration Issues

### API Key Errors

**Problem**: `AuthenticationError: Invalid API key`

**Solutions**:
1. Verify API key is correct in `config/api_keys.yaml`
2. Check for extra spaces or quotes in the key
3. Ensure the key has the necessary permissions
4. Regenerate the API key if needed

```bash
# Test your API key with curl
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Rate Limiting

**Problem**: `RateLimitError: Rate limit exceeded`

**Solutions**:
```python
import time
from openai import OpenAI
from openai import RateLimitError

client = OpenAI(api_key="your-key")

def call_with_retry(max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(...)
        except RateLimitError:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                raise
```

### Model Not Found

**Problem**: `Model not found or deprecated`

**Solutions**:
1. Check if the model name is correct
2. Verify you have access to the model
3. Update to the latest model names
4. Check the provider's model documentation

## Notebook Issues

### Import Errors in Notebooks

**Problem**: `ModuleNotFoundError: No module named 'langchain'`

**Solutions**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install missing package
pip install langchain

# Restart Jupyter kernel
# In Jupyter: Kernel -> Restart
```

### Kernel Crashes

**Problem**: Jupyter kernel keeps dying

**Solutions**:
```bash
# Check available memory
free -h  # Linux
# Task Manager # Windows

# Increase memory limits
# In Jupyter: File -> Trusted Notebooks

# Use smaller batch sizes
# Reduce model context window
```

### Display Issues

**Problem**: Plots or outputs not displaying

**Solutions**:
```python
# In notebook
%matplotlib inline
import matplotlib.pyplot as plt

# Enable widget output
%matplotlib widget
```

## Performance Issues

### Slow API Responses

**Problem**: API calls taking too long

**Solutions**:
```python
# Use faster models
# Switch from GPT-4 to GPT-3.5 Turbo

# Reduce context window
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=500  # Reduce from 2000
)

# Use streaming responses
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    stream=True
)
```

### High Memory Usage

**Problem**: Running out of RAM during processing

**Solutions**:
```python
# Process in batches
def process_in_batches(data, batch_size=10):
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        process_batch(batch)
        # Clear memory
        del batch
        import gc
        gc.collect()
```

### High Costs

**Problem**: Unexpectedly high API costs

**Solutions**:
```python
# Use cost tracker to monitor
from tools.cost_tracker import CostTracker

tracker = CostTracker()
tracker.record_usage("gpt-3.5-turbo", "openai", 
                   1000, 500, "data_cleaning")

# Check costs regularly
stats = tracker.get_usage_statistics(30)
print(f"Total cost: ${stats['total_cost']:.2f}")

# Switch to cheaper models
# Use local models when possible
```

## Model-Specific Issues

### OpenAI Issues

**Problem**: OpenAI API timeouts or errors

**Solutions**:
```python
# Increase timeout
import openai
client = openai.OpenAI(
    api_key="your-key",
    timeout=60.0  # Increase from default
)
```

### Anthropic Issues

**Problem**: Anthropic API formatting errors

**Solutions**:
```python
# Ensure correct message format
messages = [
    {"role": "user", "content": "Your prompt"}
]

# For complex prompts, use structured format
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Your text"},
            {"type": "image", "source": {"type": "base64", "data": "..."}}
        ]
    }
]
```

### Local Model Issues

**Problem**: Local models not responding

**Solutions**:
```bash
# Check if Ollama is running
ollama list

# Restart Ollama
ollama serve

# Check model availability
ollama pull llama3.1

# Test the model
ollama run llama3.1 "Hello"
```

## Data Issues

### File Reading Errors

**Problem**: Cannot read data files

**Solutions**:
```python
# Check file paths
import os
print(os.getcwd())
print(os.listdir('.'))

# Use absolute paths
from pathlib import Path
file_path = Path(__file__).parent / 'data' / 'file.csv'

# Check file permissions
chmod 644 your_file.csv
```

### Data Format Errors

**Problem**: Data not in expected format

**Solutions**:
```python
# Inspect data structure
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
print(df.dtypes)

# Handle missing data
df = df.fillna('')  # Or df.dropna()

# Convert data types
df['column'] = df['column'].astype(str)
```

## GitHub Issues

### Push Failures

**Problem**: Git push fails

**Solutions**:
```bash
# Check remote URL
git remote -v

# Update remote URL
git remote set-url origin https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers.git

# Pull latest changes first
git pull origin main

# Then push
git push origin main
```

### CI/CD Failures

**Problem**: GitHub Actions failing

**Solutions**:
1. Check Actions tab in GitHub repository
2. Review error logs
3. Ensure all dependencies are in requirements.txt
4. Verify API keys are configured as secrets
5. Check Python version compatibility

## Getting Help

### When to Ask for Help

1. You've tried the solutions above
2. The error persists after multiple attempts
3. The error is not documented here
4. You need clarification on course material

### How to Get Help

1. **Check existing issues**: Search GitHub Issues first
2. **Create a new issue**: Include error messages, steps to reproduce, and your environment
3. **Join discussions**: Ask questions in GitHub Discussions
4. **Check documentation**: Review main documentation and wiki

### Information to Include

When asking for help, include:

```markdown
## Environment
- Python version: 3.11.0
- OS: Ubuntu 22.04
- Virtual environment: Yes

## Error Message
```
Full error message here
```

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## What You Tried
- Solution 1: Result
- Solution 2: Result
```

## Additional Resources

- [Main Documentation](https://nellaivijay.github.io/prompt-engineering-for-ai-data-engineers/)
- [GitHub Issues](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/issues)
- [GitHub Discussions](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/discussions)
- [Getting Started Guide](Getting-Started)

---

**Last Updated**: 2024-04-26