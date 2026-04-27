# Getting Started Guide

This guide will help you set up your environment and get started with the Prompt Engineering for AI Data Engineers course.

## Prerequisites

### System Requirements

- **Python**: 3.9 or higher
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 10GB free space
- **Internet Connection**: Required for API-based models

### Required Software

- Python 3.9+
- pip (Python package manager)
- Git
- Jupyter Notebook or JupyterLab
- IDE (VS Code, PyCharm, or similar)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers.git
cd prompt-engineering-for-ai-data-engineers
```

### 2. Create a Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n prompt-engineering python=3.11
conda activate prompt-engineering
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a copy of the example configuration file:

```bash
cp config/api_keys.example.yaml config/api_keys.yaml
```

Edit `config/api_keys.yaml` and add your API keys:

```yaml
openai:
  api_key: "your-openai-api-key-here"
  model: "gpt-4-turbo"
  temperature: 0.7
  max_tokens: 2000

anthropic:
  api_key: "your-anthropic-api-key-here"
  model: "claude-3-sonnet"
  temperature: 0.7
  max_tokens: 2000

google:
  api_key: "your-google-api-key-here"
  model: "gemini-pro"
  temperature: 0.7
  max_tokens: 2000
```

### 5. Run the Setup Script

```bash
python tools/setup.py
```

This will verify your installation and create necessary directories.

## API Key Setup

### OpenAI

1. Go to https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key and add it to your config file

### Anthropic

1. Go to https://console.anthropic.com/
2. Sign in or create an account
3. Go to API Keys section
4. Click "Create Key"
5. Copy the key and add it to your config file

### Google Gemini

1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your config file

### Cohere

1. Go to https://dashboard.cohere.com/api-keys
2. Sign in or create an account
3. Click "Create API Key"
4. Copy the key and add it to your config file

## Local Model Setup (Optional)

If you want to use local models for privacy or cost savings:

### Ollama Setup

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.1

# Run Ollama server
ollama serve
```

### vLLM Setup

```bash
pip install vllm

# Run a model
python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-2-7b-chat-hf
```

## Verify Installation

Run the verification script:

```bash
python tools/setup.py
```

You should see:
- ✅ Python version check
- ✅ Dependencies check
- ✅ Directory structure check
- ✅ Configuration files check
- ✅ Basic functionality tests

## Start Learning

### Option 1: Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to the `content/` directory and start with Module 1.

### Option 2: JupyterLab

```bash
jupyter lab
```

### Option 3: VS Code

1. Install the Jupyter extension for VS Code
2. Open the repository in VS Code
3. Open any `.ipynb` file to start

## Course Structure

```
prompt-engineering-for-ai-data-engineers/
├── content/                 # Course notebooks and materials
│   ├── module1-foundations/
│   ├── module2-data-cleaning/
│   └── ...
├── tools/                   # Utility scripts
│   ├── setup.py
│   ├── model_router.py
│   └── cost_tracker.py
├── config/                  # Configuration files
│   ├── api_keys.yaml
│   └── model_configs.yaml
├── docs/                    # Documentation
├── tests/                   # Test files
└── requirements.txt         # Python dependencies
```

## Next Steps

1. **Complete Module 1**: Foundations of Multi-Model Prompt Engineering
2. **Choose a primary model**: Start with one provider before exploring others
3. **Practice with examples**: Work through the notebooks in each module
4. **Join the community**: Participate in GitHub Discussions

## Troubleshooting

### Common Issues

**Issue**: Import errors when running notebooks
- **Solution**: Make sure you've activated your virtual environment and installed dependencies

**Issue**: API key errors
- **Solution**: Verify your API keys are correctly configured in `config/api_keys.yaml`

**Issue**: Out of memory errors
- **Solution**: Use a smaller model or reduce batch sizes in your notebooks

**Issue**: Slow response times
- **Solution**: Consider using local models or optimizing your prompts

## Additional Resources

- [Main Documentation](https://nellaivijay.github.io/prompt-engineering-for-ai-data-engineers/)
- [Model Configuration Guide](Model-Configuration)
- [Troubleshooting Guide](Troubleshooting)
- [GitHub Issues](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/issues)

## Getting Help

If you encounter any issues:

1. Check the [Troubleshooting](Troubleshooting) wiki page
2. Search existing [GitHub Issues](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/issues)
3. Create a new issue with detailed information about your problem
4. Join the [GitHub Discussions](https://github.com/nellaivijay/prompt-engineering-for-ai-data-engineers/discussions) for community support

---

**Happy Learning! 🚀**