"""
Tests for the Model Router module.
"""

import pytest
from tools.model_router import ModelRouter, TaskType, CostSensitivity, LatencyRequirement


class TestModelRouter:
    """Test suite for ModelRouter class."""
    
    @pytest.fixture
    def router(self):
        """Create a ModelRouter instance for testing."""
        return ModelRouter()
    
    def test_initialization(self, router):
        """Test that ModelRouter initializes correctly."""
        assert router.config is not None
        assert 'models' in router.config
        assert 'selection_guidelines' in router.config
    
    def test_categorize_task(self, router):
        """Test task categorization."""
        assert router._categorize_task("data cleaning") == "data_cleaning"
        assert router._categorize_task("SQL generation") == "sql_generation"
        assert router._categorize_task("data documentation") == "data_documentation"
        assert router._categorize_task("real-time processing") == "real_time_processing"
    
    def test_route_task_basic(self, router):
        """Test basic task routing."""
        result = router.route_task(
            task="data_cleaning",
            data_size="medium",
            cost_sensitivity="medium"
        )
        
        assert 'selected_model' in result
        assert 'reasoning' in result
        assert 'model_info' in result
        assert result['selected_model'] is not None
    
    def test_route_task_with_cost_sensitivity(self, router):
        """Test task routing with cost sensitivity."""
        result_high_cost = router.route_task(
            task="data_cleaning",
            cost_sensitivity="high"
        )
        
        result_low_cost = router.route_task(
            task="data_cleaning",
            cost_sensitivity="low"
        )
        
        assert result_high_cost['selected_model'] is not None
        assert result_low_cost['selected_model'] is not None
        # Cost-sensitive routing should prefer different models
    
    def test_get_model_info(self, router):
        """Test getting model information."""
        model_info = router._get_model_info("gpt-4-turbo")
        
        assert model_info['provider'] == 'openai'
        assert model_info['model_name'] == 'gpt-4-turbo'
        assert 'context_window' in model_info
        assert 'cost_per_1k_tokens' in model_info
    
    def test_get_model_info_invalid(self, router):
        """Test getting model information for invalid model."""
        with pytest.raises(ValueError):
            router._get_model_info("invalid_model_name")
    
    def test_compare_models(self, router):
        """Test model comparison."""
        comparison = router.compare_models(
            task="data_cleaning",
            models=["gpt-4-turbo", "claude-3-sonnet"]
        )
        
        assert "gpt-4-turbo" in comparison
        assert "claude-3-sonnet" in comparison
        assert all('cost' in comparison[model] for model in comparison)
        assert all('latency' in comparison[model] for model in comparison)
    
    def test_estimate_cost(self, router):
        """Test cost estimation."""
        cost = router.estimate_cost(
            model_name="gpt-3.5-turbo",
            input_tokens=1000,
            output_tokens=500
        )
        
        assert cost > 0
        assert isinstance(cost, float)
    
    def test_estimate_cost_free_model(self, router):
        """Test cost estimation for free model."""
        cost = router.estimate_cost(
            model_name="llama-3.1-70b",
            input_tokens=1000,
            output_tokens=500
        )
        
        assert cost == 0  # Local models should have zero API cost


class TestTaskType:
    """Test suite for TaskType enum."""
    
    def test_task_type_values(self):
        """Test that TaskType has expected values."""
        assert TaskType.DATA_CLEANING.value == "data_cleaning"
        assert TaskType.SQL_GENERATION.value == "sql_generation"
        assert TaskType.DATA_DOCUMENTATION.value == "data_documentation"
    
    def test_task_type_iteration(self):
        """Test iterating over TaskType values."""
        task_types = [task_type.value for task_type in TaskType]
        assert "data_cleaning" in task_types
        assert "sql_generation" in task_types


class TestCostSensitivity:
    """Test suite for CostSensitivity enum."""
    
    def test_cost_sensitivity_values(self):
        """Test that CostSensitivity has expected values."""
        assert CostSensitivity.LOW.value == "low"
        assert CostSensitivity.MEDIUM.value == "medium"
        assert CostSensitivity.HIGH.value == "high"


class TestLatencyRequirement:
    """Test suite for LatencyRequirement enum."""
    
    def test_latency_requirement_values(self):
        """Test that LatencyRequirement has expected values."""
        assert LatencyRequirement.LOW.value == "low"
        assert LatencyRequirement.MEDIUM.value == "medium"
        assert LatencyRequirement.HIGH.value == "high"
