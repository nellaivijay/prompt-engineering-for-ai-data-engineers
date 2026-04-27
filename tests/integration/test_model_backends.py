"""
Integration tests for AI model backends.
Tests the integration with different AI model providers.
"""

import os
import pytest
from pathlib import Path
import sys

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools"))


class TestModelBackends:
    """Test suite for AI model backend integrations."""

    @pytest.fixture
    def api_keys(self):
        """Load API keys from environment or config."""
        return {
            'openai': os.getenv('OPENAI_API_KEY'),
            'anthropic': os.getenv('ANTHROPIC_API_KEY'),
            'gemini': os.getenv('GEMINI_API_KEY'),
            'llama': os.getenv('LLAMA_API_KEY'),
            'mistral': os.getenv('MISTRAL_API_KEY'),
            'cohere': os.getenv('COHERE_API_KEY'),
        }

    def test_openai_backend(self, api_keys):
        """Test OpenAI backend integration."""
        if not api_keys['openai']:
            pytest.skip("OPENAI_API_KEY not set")
        
        try:
            import openai
            client = openai.OpenAI(api_key=api_keys['openai'])
            
            # Simple test call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=10
            )
            
            assert response.choices is not None
            assert len(response.choices) > 0
        except ImportError:
            pytest.skip("openai package not installed")
        except Exception as e:
            pytest.fail(f"OpenAI backend test failed: {e}")

    def test_anthropic_backend(self, api_keys):
        """Test Anthropic backend integration."""
        if not api_keys['anthropic']:
            pytest.skip("ANTHROPIC_API_KEY not set")
        
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_keys['anthropic'])
            
            # Simple test call
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=10,
                messages=[{"role": "user", "content": "Hello"}]
            )
            
            assert response.content is not None
        except ImportError:
            pytest.skip("anthropic package not installed")
        except Exception as e:
            pytest.fail(f"Anthropic backend test failed: {e}")

    def test_gemini_backend(self, api_keys):
        """Test Google Gemini backend integration."""
        if not api_keys['gemini']:
            pytest.skip("GEMINI_API_KEY not set")
        
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_keys['gemini'])
            
            # Simple test call
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("Hello")
            
            assert response.text is not None
        except ImportError:
            pytest.skip("google-generativeai package not installed")
        except Exception as e:
            pytest.fail(f"Gemini backend test failed: {e}")

    def test_model_router(self):
        """Test model router functionality."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test model selection
            model = router.select_model(task="data_cleaning", budget=0.01)
            assert model is not None
            
            # Test cost estimation
            cost = router.estimate_cost(model, tokens=1000)
            assert cost >= 0
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Model router test failed: {e}")

    def test_cost_tracker(self):
        """Test cost tracker functionality."""
        try:
            from cost_tracker import CostTracker
            
            tracker = CostTracker()
            
            # Test cost tracking
            tracker.log_cost("openai", "gpt-3.5-turbo", 1000, 500)
            tracker.log_cost("anthropic", "claude-3-haiku", 500, 200)
            
            # Test cost summary
            summary = tracker.get_summary()
            assert summary is not None
            assert "total_cost" in summary
            
        except ImportError:
            pytest.skip("cost_tracker module not found")
        except Exception as e:
            pytest.fail(f"Cost tracker test failed: {e}")

    def test_api_key_config(self):
        """Test API key configuration loading."""
        config_path = Path(__file__).parent.parent.parent / "config" / "api_keys.example.yaml"
        
        if config_path.exists():
            import yaml
            
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            assert config is not None
            assert 'models' in config or 'api_keys' in config
        else:
            pytest.skip("API key config file not found")


class TestModelConfigurations:
    """Test model configurations and capabilities."""

    def test_model_configs_loading(self):
        """Test loading model configurations."""
        config_path = Path(__file__).parent.parent.parent / "config" / "model_configs.yaml"
        
        if config_path.exists():
            import yaml
            
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            assert config is not None
            assert 'models' in config
            
            # Check required fields
            for model_name, model_config in config['models'].items():
                assert 'cost_per_1k_tokens' in model_config
                assert 'capabilities' in model_config
        else:
            pytest.skip("Model config file not found")

    def test_model_capability_checking(self):
        """Test model capability checking."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test capability checks
            assert router.has_capability("gpt-3.5-turbo", "data_cleaning")
            assert router.has_capability("claude-3-haiku", "code_generation")
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Model capability test failed: {e}")


class TestPromptEngineering:
    """Test prompt engineering functionality."""

    def test_basic_prompt_creation(self):
        """Test basic prompt creation for data engineering tasks."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test prompt creation for data cleaning
            prompt = router.create_prompt(
                task="data_cleaning",
                context="Clean customer data",
                data_sample={"name": "John Doe", "email": "john@example.com"}
            )
            
            assert prompt is not None
            assert len(prompt) > 0
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Prompt creation test failed: {e}")

    def test_multi_model_comparison(self):
        """Test comparing responses across multiple models."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test multi-model comparison (without actual API calls)
            models = ["gpt-3.5-turbo", "claude-3-haiku"]
            comparison = router.compare_models(
                models=models,
                task="data_cleaning",
                prompt="Clean this data"
            )
            
            assert comparison is not None
            assert len(comparison) == len(models)
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Multi-model comparison test failed: {e}")