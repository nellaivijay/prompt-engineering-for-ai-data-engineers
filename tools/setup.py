#!/usr/bin/env python3
"""
Setup script for Prompt Engineering for AI Data Engineers
This script verifies the installation and configuration of the course environment.
"""

import sys
import os
import subprocess
import importlib
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    if version < (3, 9):
        print(f"❌ Python {version.major}.{version.minor} is not supported. Please use Python 3.9 or higher.")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible.")
    return True

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("\nChecking dependencies...")
    required_packages = [
        'langchain', 'pandas', 'numpy', 'pyyaml', 
        'requests', 'pydantic', 'sqlalchemy'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} is installed.")
        except ImportError:
            print(f"❌ {package} is missing.")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    return True

def check_directory_structure():
    """Check if required directories exist."""
    print("\nChecking directory structure...")
    required_dirs = [
        'content', 'docs', 'data', 'tools', 'config', 'tests'
    ]
    
    missing_dirs = []
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if not dir_path.exists():
            print(f"❌ Directory '{dir_name}' is missing.")
            missing_dirs.append(dir_name)
        else:
            print(f"✅ Directory '{dir_name}' exists.")
    
    if missing_dirs:
        print(f"\nCreating missing directories...")
        for dir_name in missing_dirs:
            Path(dir_name).mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory '{dir_name}'.")
    
    return True

def check_config_files():
    """Check if configuration files exist."""
    print("\nChecking configuration files...")
    config_file = Path('config/api_keys.yaml')
    example_file = Path('config/api_keys.example.yaml')
    
    if not config_file.exists():
        if example_file.exists():
            print("⚠️  API keys configuration file not found.")
            print("   Copy the example file and add your API keys:")
            print("   cp config/api_keys.example.yaml config/api_keys.yaml")
            return False
        else:
            print("❌ Configuration example file not found.")
            return False
    
    print("✅ Configuration file exists.")
    return True

def check_local_models():
    """Check if local models are available."""
    print("\nChecking local model setup...")
    try:
        import requests
        ollama_url = "http://localhost:11434/api/tags"
        try:
            response = requests.get(ollama_url, timeout=2)
            if response.status_code == 200:
                print("✅ Ollama service is running.")
                models = response.json().get('models', [])
                if models:
                    print(f"✅ Found {len(models)} local models:")
                    for model in models[:5]:  # Show first 5 models
                        print(f"   - {model.get('name', 'unknown')}")
                else:
                    print("⚠️  Ollama is running but no models are installed.")
                    print("   Install a model with: ollama pull llama3.1")
            else:
                print("⚠️  Ollama service is not responding.")
                print("   Start Ollama with: ollama serve")
        except requests.exceptions.ConnectionError:
            print("⚠️  Ollama service is not running.")
            print("   Local models are optional. You can use API-based models instead.")
            print("   To use local models, start Ollama with: ollama serve")
    except ImportError:
        print("⚠️  Requests library not installed. Skipping local model check.")
    
    return True  # Local models are optional

def create_sample_data():
    """Create sample data directories and files."""
    print("\nCreating sample data structure...")
    data_dirs = ['data/raw', 'data/processed', 'data/reference']
    
    for dir_path in data_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {dir_path}")
    
    # Create a sample data file
    sample_data = Path('data/raw/sample_data.csv')
    if not sample_data.exists():
        sample_data.write_text("id,name,value\n1,Sample Data,100\n2,Test Data,200\n")
        print(f"✅ Created sample data file: {sample_data}")
    
    return True

def run_basic_tests():
    """Run basic functionality tests."""
    print("\nRunning basic functionality tests...")
    
    try:
        # Test basic imports
        import yaml
        print("✅ YAML library works.")
        
        # Test configuration loading
        config_file = Path('config/model_configs.yaml')
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
            print("✅ Configuration file can be loaded.")
        
        return True
    except Exception as e:
        print(f"❌ Basic tests failed: {e}")
        return False

def main():
    """Main setup function."""
    print("=" * 60)
    print("Prompt Engineering for AI Data Engineers - Setup")
    print("=" * 60)
    
    checks = [
        check_python_version,
        check_dependencies,
        check_directory_structure,
        check_config_files,
        check_local_models,
        create_sample_data,
        run_basic_tests
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Error during {check.__name__}: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("Setup Summary")
    print("=" * 60)
    
    if all(results):
        print("✅ All checks passed! You're ready to start.")
        print("\nNext steps:")
        print("1. Configure your API keys in config/api_keys.yaml")
        print("2. Start with Module 1: content/module1-foundations/")
        print("3. Run the notebooks in Jupyter or JupyterLab")
        return 0
    else:
        failed = len([r for r in results if not r])
        print(f"⚠️  {failed} check(s) failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
