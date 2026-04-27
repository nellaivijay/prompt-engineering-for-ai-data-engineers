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
            
            # Test model routing
            result = router.route_task(task="data_cleaning", cost_sensitivity="medium")
            assert result is not None
            assert 'selected_model' in result
            
            # Test cost estimation
            cost = router.estimate_cost("gpt-3.5-turbo", 1000, 500)
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
            tracker.record_usage("gpt-3.5-turbo", "openai", 1000, 500, "data_cleaning")
            tracker.record_usage("claude-3-haiku", "anthropic", 500, 200, "sql_generation")
            
            # Test cost summary
            stats = tracker.get_usage_statistics(30)
            assert stats is not None
            assert "total_cost" in stats
            
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
            # The actual config has provider names as keys (openai, anthropic, etc.)
            assert 'openai' in config or 'anthropic' in config or 'models' in config
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
            
            # Check that models have proper structure
            # The actual structure is nested by provider
            for provider, models in config['models'].items():
                assert isinstance(models, dict)
                for model_name, model_config in models.items():
                    # Check for cost structure (it's nested as {'input': x, 'output': y})
                    if 'cost_per_1k_tokens' in model_config:
                        costs = model_config['cost_per_1k_tokens']
                        assert isinstance(costs, dict)
        else:
            pytest.skip("Model config file not found")

    def test_model_capability_checking(self):
        """Test model capability checking."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test model routing for different tasks (actual method)
            result = router.route_task(task="data_cleaning", cost_sensitivity="medium")
            assert result is not None
            assert 'selected_model' in result
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Model capability test failed: {e}")


class TestPromptEngineering:
    """Test prompt engineering functionality."""

    def test_basic_prompt_creation(self):
        """Test basic task routing for data engineering tasks."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test task routing for data cleaning
            result = router.route_task(
                task="data_cleaning",
                cost_sensitivity="medium"
            )
            
            assert result is not None
            assert 'selected_model' in result
            assert 'model_info' in result
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Task routing test failed: {e}")

    def test_multi_model_comparison(self):
        """Test comparing multiple models for a specific task."""
        try:
            from model_router import ModelRouter
            
            router = ModelRouter()
            
            # Test multi-model comparison (actual method signature)
            comparison = router.compare_models(
                task="data_cleaning",
                models=["gpt-3.5-turbo", "gpt-4-turbo"]
            )
            
            assert comparison is not None
            assert isinstance(comparison, dict)
            
        except ImportError:
            pytest.skip("model_router module not found")
        except Exception as e:
            pytest.fail(f"Multi-model comparison test failed: {e}")