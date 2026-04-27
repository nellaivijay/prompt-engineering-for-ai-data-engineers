# Getting Started Guide

Welcome to Prompt Engineering for AI Data Engineers - Multi-Model Edition. This guide will help you set up your environment and get started with the course.

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.9 or higher** installed
- **Git** for version control
- **Basic knowledge** of data engineering concepts
- **API keys** for at least one AI provider (optional for local models)

### Supported Python Versions

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

## Installation Methods

### Method 1: Standard pip Installation

```bash
# Clone the repository
git clone https://github.com/your-username/prompt-engineering-for-ai-data-engineers.git
cd prompt-engineering-for-ai-data-engineers

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Method 2: Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/your-username/prompt-engineering-for-ai-data-engineers.git
cd prompt-engineering-for-ai-data-engineers

# Install using uv (faster and more reliable)
uv pip install -r requirements.txt
```

### Method 3: Using Conda

```bash
# Clone the repository
git clone https://github.com/your-username/prompt-engineering-for-ai-data-engineers.git
cd prompt-engineering-for-ai-data-engineers

# Create conda environment
conda create -n prompt-engineering python=3.11
conda activate prompt-engineering

# Install dependencies
pip install -r requirements.txt
```

## Configuration Setup

### API Keys Configuration

1. Copy the example configuration file:
```bash
cp config/api_keys.example.yaml config/api_keys.yaml
```

2. Edit the configuration file with your API keys:
```bash
nano config/api_keys.yaml
# or use your preferred editor
```

3. The configuration file structure:
```yaml
openai:
  api_key: "your-openai-api-key"
  model: "gpt-4-turbo"
  
anthropic:
  api_key: "your-anthropic-api-key"
  model: "claude-3-sonnet"
  
google:
  api_key: "your-google-api-key"
  model: "gemini-pro"
  
cohere:
  api_key: "your-cohere-api-key"
  model: "command-r"
  
# Local models (no API key needed)
local:
  ollama_base_url: "http://localhost:11434"
  model: "llama3.1"
```

### Environment Variables (Alternative)

You can also set API keys as environment variables:

```bash
# OpenAI
export OPENAI_API_KEY="your-openai-api-key"

# Anthropic
export ANTHROPIC_API_KEY="your-anthropic-api-key"

# Google
export GOOGLE_API_KEY="your-google-api-key"

# Cohere
export COHERE_API_KEY="your-cohere-api-key"
```

## Local Model Setup

### Option 1: Ollama (Recommended for Beginners)

```bash
# Install Ollama
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.com/install.sh | sh
# Windows: Download from ollama.com

# Start Ollama service
ollama serve

# Pull a model
ollama pull llama3.1
ollama pull mistral
ollama pull codellama

# Test the installation
ollama run llama3.1 "Hello, how are you?"
```

### Option 2: vLLM (For Production)

```bash
# Install vLLM
pip install vllm

# Start vLLM server
python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf
```

### Option 3: LM Studio (GUI-Based)

1. Download LM Studio from lmstudio.ai
2. Install and launch the application
3. Download your preferred model
4. Start the local server

## Running the Setup Script

```bash
# Run the setup script to verify installation
python tools/setup.py
```

This script will:
- Check Python version compatibility
- Verify all required dependencies
- Test API key configuration
- Validate local model setup
- Create necessary directories

## Quick Start Examples

### Example 1: Basic Model Usage

```python
from tools.model_router import ModelRouter

# Initialize the model router
router = ModelRouter()

# Route a simple task
result = router.route_task(
    task="text_generation",
    prompt="Explain data engineering in simple terms",
    model_preference="cost_effective"
)

print(result)
```

### Example 2: Data Cleaning with Multiple Models

```python
import pandas as pd
from tools.data_cleaning import DataCleaner

# Load sample data
df = pd.read_csv('data/raw/sample_data.csv')

# Initialize data cleaner
cleaner = DataCleaner()

# Clean data using multiple models
cleaned_df = cleaner.clean_data(
    df,
    models=['gpt-4-turbo', 'claude-3-sonnet', 'llama3.1'],
    task='standardization'
)

print(cleaned_df.head())
```

### Example 3: SQL Generation

```python
from tools.sql_generator import SQLGenerator

generator = SQLGenerator()

# Generate SQL from natural language
sql = generator.generate_sql(
    natural_language="Find all customers who spent more than average last month",
    database_schema="sales_db",
    model_preference="gpt-4-turbo"
)

print(sql)
```

## Running the Notebooks

### Using Jupyter Notebook

```bash
# Install Jupyter
pip install jupyter notebook

# Start Jupyter
jupyter notebook

# Navigate to content/ and open any module notebook
```

### Using JupyterLab (Recommended)

```bash
# Install JupyterLab
pip install jupyterlab

# Start JupyterLab
jupyter lab

# Navigate to content/ and open any module notebook
```

### Using Google Colab

1. Upload the notebook to Google Colab
2. Install dependencies in the first cell:
```python
!pip install -r requirements.txt
```
3. Upload your API keys or use Colab secrets

## Verifying Your Installation

Run the verification script to ensure everything is set up correctly:

```bash
python tools/verify_setup.py
```

This will check:
- Python version
- Package installations
- API key configuration
- Local model availability
- Basic functionality tests

## Common Issues and Solutions

### Issue: API Key Errors

**Problem**: Authentication errors when using API-based models

**Solution**: 
- Verify your API keys are correct
- Check that the keys have necessary permissions
- Ensure the keys are set in the correct location

### Issue: Local Model Not Found

**Problem**: Cannot connect to local models

**Solution**:
- Ensure Ollama/vLLM service is running
- Check the model is downloaded
- Verify the base URL configuration

### Issue: Memory Errors

**Problem**: Out of memory when running large models

**Solution**:
- Use smaller models (e.g., Llama 3.2 3B instead of 70B)
- Reduce batch size in processing
- Use quantized models
- Increase system RAM or use cloud-based solutions

### Issue: Slow Performance

**Problem**: Model responses are slow

**Solution**:
- Use faster models (Gemini Flash, Claude Haiku)
- Enable caching in the configuration
- Use local models for privacy-sensitive data
- Consider GPU acceleration for local models

## Next Steps

1. **Start with Module 1**: Begin with the foundations module to understand the basics
2. **Choose your learning path**: Decide between beginner, intermediate, or advanced track
3. **Practice with examples**: Work through the examples in each module
4. **Experiment with different models**: Try various models to understand their strengths
5. **Build your own projects**: Apply what you learn to real data engineering tasks

## Getting Help

- **Documentation**: Check the docs/ directory for detailed guides
- **Issues**: Open an issue on GitHub for bugs or questions
- **Community**: Join our discussions for community support
- **Examples**: Look at the examples in each module for reference

## Additional Resources

- [Model Comparison Guide](MODEL_GUIDE.md)
- [Cost Optimization Guide](docs/cost-analysis.md)
- [Deployment Guides](docs/deployment-guides/)
- [API Reference](docs/api-reference/)

---

Happy learning! 🚀
