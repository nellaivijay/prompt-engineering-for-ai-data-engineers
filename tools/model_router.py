#!/usr/bin/env python3
"""
Model Router - Smart model selection for data engineering tasks
This module provides intelligent routing between different AI models based on task requirements.
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum


class TaskType(Enum):
    """Enumeration of data engineering task types."""
    DATA_CLEANING = "data_cleaning"
    SQL_GENERATION = "sql_generation"
    DATA_DOCUMENTATION = "data_documentation"
    REAL_TIME_PROCESSING = "real_time_processing"
    COMPLEX_REASONING = "complex_reasoning"
    SCHEMA_INFERENCE = "schema_inference"
    ANOMALY_DETECTION = "anomaly_detection"
    DATA_TRANSFORMATION = "data_transformation"


class CostSensitivity(Enum):
    """Cost sensitivity levels for model selection."""
    LOW = "low"  # Prioritize performance over cost
    MEDIUM = "medium"  # Balanced approach
    HIGH = "high"  # Prioritize cost over performance


class LatencyRequirement(Enum):
    """Latency requirements for model selection."""
    LOW = "low"  # Latency not critical
    MEDIUM = "medium"  # Moderate latency requirements
    HIGH = "high"  # Low latency critical


class ModelRouter:
    """
    Intelligent model router for data engineering tasks.
    Selects the best model based on task requirements, cost sensitivity, and latency needs.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the model router.
        
        Args:
            config_path: Path to the model configuration file
        """
        if config_path is None:
            config_path = "config/model_configs.yaml"
        
        self.config_path = Path(config_path)
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load model configuration from YAML file."""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                "Please ensure the file exists or provide the correct path."
            )
        
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def route_task(
        self,
        task: str,
        data_size: str = "medium",
        cost_sensitivity: str = "medium",
        latency_requirement: str = "low",
        model_preference: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Route a task to the most appropriate model.
        
        Args:
            task: The task type (e.g., "data_cleaning", "sql_generation")
            data_size: Size of data ("small", "medium", "large")
            cost_sensitivity: Cost sensitivity ("low", "medium", "high")
            latency_requirement: Latency requirement ("low", "medium", "high")
            model_preference: Preferred model (optional)
        
        Returns:
            Dictionary containing model selection and reasoning
        """
        # If specific model is preferred, use it
        if model_preference:
            return self._get_model_info(model_preference)
        
        # Determine task category
        task_category = self._categorize_task(task)
        
        # Get selection guidelines
        guidelines = self.config.get('selection_guidelines', {})
        task_guidelines = guidelines.get(task_category, {})
        
        # Select model based on cost sensitivity
        if cost_sensitivity == "high":
            recommended_models = task_guidelines.get('cost_optimized', [])
        elif latency_requirement == "high":
            recommended_models = task_guidelines.get('latency_sensitive', [])
        else:
            recommended_models = task_guidelines.get('recommended', [])
        
        # Select the best model from recommendations
        if recommended_models:
            selected_model = recommended_models[0]
            model_info = self._get_model_info(selected_model)
            
            return {
                'selected_model': selected_model,
                'reasoning': f"Selected based on task category '{task_category}' and cost sensitivity '{cost_sensitivity}'",
                'alternatives': recommended_models[1:],
                'model_info': model_info
            }
        
        # Fallback to default model
        return self._get_default_model()
    
    def _categorize_task(self, task: str) -> str:
        """
        Categorize a task into known task types.
        
        Args:
            task: The task description
        
        Returns:
            The task category
        """
        task_lower = task.lower()
        
        # Task keyword mapping
        task_keywords = {
            TaskType.DATA_CLEANING: ['clean', 'cleaning', 'quality', 'standardization', 'profiling'],
            TaskType.SQL_GENERATION: ['sql', 'query', 'database', 'optimization'],
            TaskType.DATA_DOCUMENTATION: ['documentation', 'dictionary', 'glossary', 'lineage'],
            TaskType.REAL_TIME_PROCESSING: ['real-time', 'stream', 'latency', 'fast'],
            TaskType.COMPLEX_REASONING: ['complex', 'reasoning', 'analysis', 'logic'],
            TaskType.SCHEMA_INFERENCE: ['schema', 'structure', 'inference'],
            TaskType.ANOMALY_DETECTION: ['anomaly', 'outlier', 'detection'],
            TaskType.DATA_TRANSFORMATION: ['transform', 'convert', 'migration', 'etl']
        }
        
        for task_type, keywords in task_keywords.items():
            if any(keyword in task_lower for keyword in keywords):
                return task_type.value
        
        # Default to data cleaning if no match
        return TaskType.DATA_CLEANING.value
    
    def _get_model_info(self, model_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific model.
        
        Args:
            model_name: Name of the model
        
        Returns:
            Dictionary with model information
        """
        models = self.config.get('models', {})
        
        # Search for the model across all providers
        for provider, provider_models in models.items():
            if model_name in provider_models:
                model_info = provider_models[model_name]
                return {
                    'provider': provider,
                    'model_name': model_info.get('model_name', model_name),
                    'context_window': model_info.get('context_window', 0),
                    'max_tokens': model_info.get('max_tokens', 0),
                    'cost_per_1k_tokens': model_info.get('cost_per_1k_tokens', {}),
                    'strengths': model_info.get('strengths', []),
                    'best_for': model_info.get('best_for', []),
                    'latency': model_info.get('latency', 'unknown'),
                    'accuracy': model_info.get('accuracy', 'unknown')
                }
        
        raise ValueError(f"Model '{model_name}' not found in configuration")
    
    def _get_default_model(self) -> Dict[str, Any]:
        """Get the default model for general use."""
        return self._get_model_info('gpt-3.5-turbo')
    
    def compare_models(
        self,
        task: str,
        models: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Compare multiple models for a specific task.
        
        Args:
            task: The task type
            models: List of models to compare (optional)
        
        Returns:
            Dictionary with model comparison
        """
        if models is None:
            # Get all available models
            models = []
            for provider_models in self.config.get('models', {}).values():
                models.extend(provider_models.keys())
        
        comparison = {}
        for model_name in models:
            try:
                model_info = self._get_model_info(model_name)
                comparison[model_name] = {
                    'cost': model_info['cost_per_1k_tokens'],
                    'latency': model_info['latency'],
                    'accuracy': model_info['accuracy'],
                    'suitability': task in model_info.get('best_for', [])
                }
            except ValueError:
                continue
        
        return comparison
    
    def estimate_cost(
        self,
        model_name: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:
        """
        Estimate the cost for using a specific model.
        
        Args:
            model_name: Name of the model
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
        
        Returns:
            Estimated cost in USD
        """
        model_info = self._get_model_info(model_name)
        costs = model_info['cost_per_1k_tokens']
        
        input_cost = (input_tokens / 1000) * costs.get('input', 0)
        output_cost = (output_tokens / 1000) * costs.get('output', 0)
        
        return input_cost + output_cost


def main():
    """Example usage of the ModelRouter."""
    router = ModelRouter()
    
    # Example 1: Route a data cleaning task
    result = router.route_task(
        task="data_cleaning",
        data_size="medium",
        cost_sensitivity="medium"
    )
    print("Data Cleaning Task Routing:")
    print(f"Selected Model: {result['selected_model']}")
    print(f"Reasoning: {result['reasoning']}")
    
    # Example 2: Route a SQL generation task with cost sensitivity
    result = router.route_task(
        task="sql_generation",
        cost_sensitivity="high"
    )
    print("\nSQL Generation Task Routing (Cost Optimized):")
    print(f"Selected Model: {result['selected_model']}")
    print(f"Reasoning: {result['reasoning']}")
    
    # Example 3: Compare models for a task
    comparison = router.compare_models("data_cleaning", ["gpt-4-turbo", "claude-3-sonnet", "llama-3.1-70b"])
    print("\nModel Comparison for Data Cleaning:")
    for model, metrics in comparison.items():
        print(f"{model}:")
        print(f"  Cost: {metrics['cost']}")
        print(f"  Latency: {metrics['latency']}")
        print(f"  Accuracy: {metrics['accuracy']}")


if __name__ == "__main__":
    main()
