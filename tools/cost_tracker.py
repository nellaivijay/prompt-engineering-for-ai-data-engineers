#!/usr/bin/env python3
"""
Cost Tracker - Monitor and optimize AI model usage costs
This module provides tools for tracking API costs and optimizing model selection.
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from collections import defaultdict


@dataclass
class APIUsage:
    """Data class representing API usage."""
    timestamp: str
    model: str
    provider: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost: float
    task_type: str


class CostTracker:
    """
    Track and analyze AI API costs across different models and tasks.
    """
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize the cost tracker.
        
        Args:
            storage_path: Path to store usage data (default: data/cost_tracking.json)
        """
        if storage_path is None:
            storage_path = "data/cost_tracking.json"
        
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.usage_data = self._load_usage_data()
        self.model_costs = self._load_model_costs()
    
    def _load_usage_data(self) -> List[Dict[str, Any]]:
        """Load existing usage data from storage."""
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return []
    
    def _load_model_costs(self) -> Dict[str, Dict[str, float]]:
        """Load model cost information from configuration."""
        config_path = Path("config/model_configs.yaml")
        if not config_path.exists():
            return {}
        
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        model_costs = {}
        for provider, models in config.get('models', {}).items():
            for model_name, model_info in models.items():
                model_costs[model_name] = model_info.get('cost_per_1k_tokens', {})
        
        return model_costs
    
    def record_usage(
        self,
        model: str,
        provider: str,
        input_tokens: int,
        output_tokens: int,
        task_type: str
    ) -> APIUsage:
        """
        Record API usage and calculate cost.
        
        Args:
            model: Name of the model used
            provider: Provider of the model
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            task_type: Type of task performed
        
        Returns:
            APIUsage object with recorded information
        """
        # Calculate cost
        cost_per_1k = self.model_costs.get(model, {'input': 0.0, 'output': 0.0})
        input_cost = (input_tokens / 1000) * cost_per_1k.get('input', 0.0)
        output_cost = (output_tokens / 1000) * cost_per_1k.get('output', 0.0)
        total_cost = input_cost + output_cost
        
        # Create usage record
        usage = APIUsage(
            timestamp=datetime.now().isoformat(),
            model=model,
            provider=provider,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            cost=total_cost,
            task_type=task_type
        )
        
        # Store usage
        self.usage_data.append(asdict(usage))
        self._save_usage_data()
        
        return usage
    
    def _save_usage_data(self):
        """Save usage data to storage."""
        with open(self.storage_path, 'w') as f:
            json.dump(self.usage_data, f, indent=2)
    
    def get_total_cost(self, days: Optional[int] = None) -> float:
        """
        Get total cost for a specific time period.
        
        Args:
            days: Number of days to look back (None for all time)
        
        Returns:
            Total cost in USD
        """
        if days is None:
            return sum(usage['cost'] for usage in self.usage_data)
        
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_usage = [
            usage for usage in self.usage_data
            if datetime.fromisoformat(usage['timestamp']) >= cutoff_date
        ]
        return sum(usage['cost'] for usage in recent_usage)
    
    def get_cost_by_model(self, days: Optional[int] = None) -> Dict[str, float]:
        """
        Get cost breakdown by model.
        
        Args:
            days: Number of days to look back (None for all time)
        
        Returns:
            Dictionary mapping model names to costs
        """
        if days is None:
            relevant_usage = self.usage_data
        else:
            cutoff_date = datetime.now() - timedelta(days=days)
            relevant_usage = [
                usage for usage in self.usage_data
                if datetime.fromisoformat(usage['timestamp']) >= cutoff_date
            ]
        
        model_costs = defaultdict(float)
        for usage in relevant_usage:
            model_costs[usage['model']] += usage['cost']
        
        return dict(model_costs)
    
    def get_cost_by_task(self, days: Optional[int] = None) -> Dict[str, float]:
        """
        Get cost breakdown by task type.
        
        Args:
            days: Number of days to look back (None for all time)
        
        Returns:
            Dictionary mapping task types to costs
        """
        if days is None:
            relevant_usage = self.usage_data
        else:
            cutoff_date = datetime.now() - timedelta(days=days)
            relevant_usage = [
                usage for usage in self.usage_data
                if datetime.fromisoformat(usage['timestamp']) >= cutoff_date
            ]
        
        task_costs = defaultdict(float)
        for usage in relevant_usage:
            task_costs[usage['task_type']] += usage['cost']
        
        return dict(task_costs)
    
    def get_usage_statistics(self, days: int = 30) -> Dict[str, Any]:
        """
        Get comprehensive usage statistics.
        
        Args:
            days: Number of days to analyze
        
        Returns:
            Dictionary with usage statistics
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        relevant_usage = [
            usage for usage in self.usage_data
            if datetime.fromisoformat(usage['timestamp']) >= cutoff_date
        ]
        
        if not relevant_usage:
            return {
                'total_requests': 0,
                'total_tokens': 0,
                'total_cost': 0.0,
                'average_cost_per_request': 0.0,
                'most_used_model': None,
                'most_expensive_model': None
            }
        
        total_requests = len(relevant_usage)
        total_tokens = sum(usage['total_tokens'] for usage in relevant_usage)
        total_cost = sum(usage['cost'] for usage in relevant_usage)
        
        # Find most used model
        model_usage = defaultdict(int)
        for usage in relevant_usage:
            model_usage[usage['model']] += 1
        most_used_model = max(model_usage.items(), key=lambda x: x[1])[0] if model_usage else None
        
        # Find most expensive model
        model_costs = defaultdict(float)
        for usage in relevant_usage:
            model_costs[usage['model']] += usage['cost']
        most_expensive_model = max(model_costs.items(), key=lambda x: x[1])[0] if model_costs else None
        
        return {
            'total_requests': total_requests,
            'total_tokens': total_tokens,
            'total_cost': total_cost,
            'average_cost_per_request': total_cost / total_requests if total_requests > 0 else 0.0,
            'most_used_model': most_used_model,
            'most_expensive_model': most_expensive_model,
            'cost_by_model': self.get_cost_by_model(days),
            'cost_by_task': self.get_cost_by_task(days)
        }
    
    def check_budget_alert(self, budget_threshold: float, days: int = 30) -> bool:
        """
        Check if costs exceed budget threshold.
        
        Args:
            budget_threshold: Budget threshold in USD
            days: Number of days to check
        
        Returns:
            True if budget exceeded, False otherwise
        """
        current_cost = self.get_total_cost(days)
        return current_cost > budget_threshold
    
    def get_cost_optimization_suggestions(self) -> List[str]:
        """
        Get suggestions for cost optimization.
        
        Returns:
            List of optimization suggestions
        """
        suggestions = []
        stats = self.get_usage_statistics(30)
        
        # Check for expensive models
        cost_by_model = stats['cost_by_model']
        if cost_by_model:
            most_expensive = max(cost_by_model.items(), key=lambda x: x[1])
            if most_expensive[1] > stats['total_cost'] * 0.5:
                suggestions.append(
                    f"Consider switching from {most_expensive[0]} to a more cost-effective model "
                    f"for suitable tasks. It accounts for {most_expensive[1]/stats['total_cost']*100:.1f}% "
                    f"of your costs."
                )
        
        # Check for high average cost per request
        if stats['average_cost_per_request'] > 0.10:
            suggestions.append(
                "Your average cost per request is relatively high. Consider batching requests "
                "or using more cost-effective models for simpler tasks."
            )
        
        # Check for task-specific optimization
        cost_by_task = stats['cost_by_task']
        if 'data_cleaning' in cost_by_task and cost_by_task['data_cleaning'] > stats['total_cost'] * 0.3:
            suggestions.append(
                "Data cleaning tasks account for a significant portion of costs. Consider using "
                "local models like Llama for data cleaning to reduce API costs."
            )
        
        if not suggestions:
            suggestions.append("Your current usage is well-optimized. Keep monitoring for changes.")
        
        return suggestions


def main():
    """Example usage of the CostTracker."""
    tracker = CostTracker()
    
    # Example: Record some usage
    tracker.record_usage(
        model="gpt-4-turbo",
        provider="openai",
        input_tokens=1000,
        output_tokens=500,
        task_type="sql_generation"
    )
    
    tracker.record_usage(
        model="claude-3-sonnet",
        provider="anthropic",
        input_tokens=800,
        output_tokens=400,
        task_type="data_cleaning"
    )
    
    # Get statistics
    stats = tracker.get_usage_statistics(30)
    print("Usage Statistics (Last 30 Days):")
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Total Tokens: {stats['total_tokens']}")
    print(f"Total Cost: ${stats['total_cost']:.4f}")
    print(f"Average Cost per Request: ${stats['average_cost_per_request']:.4f}")
    print(f"Most Used Model: {stats['most_used_model']}")
    
    # Get cost breakdown
    print("\nCost by Model:")
    for model, cost in stats['cost_by_model'].items():
        print(f"  {model}: ${cost:.4f}")
    
    # Get optimization suggestions
    print("\nCost Optimization Suggestions:")
    for suggestion in tracker.get_cost_optimization_suggestions():
        print(f"  • {suggestion}")


if __name__ == "__main__":
    main()
