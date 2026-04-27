# Model Configuration Guide

This guide explains how to configure and optimize different AI models for data engineering tasks.

## Configuration Files

### API Keys Configuration

Located at `config/api_keys.yaml`:

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
```

### Model Configuration

Located at `config/model_configs.yaml`:

```yaml
models:
  openai:
    gpt-4-turbo:
      provider: openai
      model_name: gpt-4-turbo
      context_window: 128000
      max_tokens: 4096
      cost_per_1k_tokens:
        input: 0.01
        output: 0.03
      strengths:
        - Complex reasoning
        - SQL generation
        - Data analysis
      best_for:
        - SQL query generation
        - Complex data transformation
```

## Model Selection

### By Task Type

#### Data Cleaning
- **Recommended**: GPT-3.5 Turbo, Claude 3 Haiku
- **Why**: Fast, cost-effective, good at pattern recognition
- **Cost**: $0.0005-$0.001 per 1K tokens

#### SQL Generation
- **Recommended**: GPT-4 Turbo, Claude 3 Sonnet
- **Why**: Strong understanding of database schemas
- **Cost**: $0.01-$0.03 per 1K tokens

#### Data Documentation
- **Recommended**: Claude 3 Opus, GPT-4 Turbo
- **Why**: Excellent at technical writing and explanation
- **Cost**: $0.015-$0.03 per 1K tokens

#### Real-time Processing
- **Recommended**: Local Llama models, Claude 3 Haiku
- **Why**: Low latency, privacy, cost control
- **Cost**: Free (local) or $0.00025 per 1K tokens

### By Cost Sensitivity

#### Cost-Optimized
- **Models**: GPT-3.5 Turbo, Claude 3 Haiku, Local Llama
- **Use Cases**: High-volume tasks, batch processing
- **Strategy**: Use cheaper models for simple tasks

#### Performance-Optimized
- **Models**: GPT-4 Turbo, Claude 3 Opus, Gemini Ultra
- **Use Cases**: Complex reasoning, critical tasks
- **Strategy**: Use for tasks requiring high accuracy

#### Balanced
- **Models**: Claude 3 Sonnet, GPT-4, Gemini Pro
- **Use Cases**: General-purpose tasks
- **Strategy**: Good balance of cost and performance

## Parameter Tuning

### Temperature

- **0.0-0.2**: Deterministic, factual responses
- **0.3-0.7**: Balanced creativity and accuracy (recommended)
- **0.8-1.0**: Creative, varied responses

**Recommendations by Task**:
- Data Cleaning: 0.2-0.4
- SQL Generation: 0.1-0.3
- Documentation: 0.3-0.5
- Brainstorming: 0.7-0.9

### Max Tokens

- **Short responses**: 500-1000 tokens
- **Medium responses**: 1000-2000 tokens
- **Long responses**: 2000-4000 tokens
- **Code generation**: 1000-3000 tokens

### Top P

- **1.0**: Use all probability mass (default)
- **0.9**: Focus on likely tokens
- **0.5**: High diversity

## Model-Specific Configurations

### OpenAI GPT Models

```python
import openai

client = openai.OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Your prompt"}],
    temperature=0.7,
    max_tokens=2000,
    top_p=0.9,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
```

### Anthropic Claude Models

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=2000,
    temperature=0.7,
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

### Google Gemini Models

```python
import google.generativeai as genai

genai.configure(api_key="your-key")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(
    "Your prompt",
    generation_config=genai.types.GenerationConfig(
        temperature=0.7,
        max_output_tokens=2000,
        top_p=0.9
    )
)
```

## Cost Optimization

### Token Estimation

```python
from tools.cost_tracker import CostTracker

tracker = CostTracker()

# Estimate cost before making API call
estimated_cost = tracker.estimate_cost(
    model_name="gpt-3.5-turbo",
    input_tokens=1000,
    output_tokens=500
)
print(f"Estimated cost: ${estimated_cost:.4f}")
```

### Model Routing

```python
from tools.model_router import ModelRouter

router = ModelRouter()

# Automatically select best model based on requirements
result = router.route_task(
    task="data_cleaning",
    cost_sensitivity="high",
    latency_requirement="medium"
)
print(f"Selected model: {result['selected_model']}")
```

## Performance Optimization

### Caching

Enable response caching for repeated requests:

```python
# In your API configuration
cache_enabled = True
cache_ttl = 3600  # 1 hour
```

### Batch Processing

Process multiple items in batches to reduce API calls:

```python
def batch_process(items, batch_size=10):
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        # Process batch
        process_batch(batch)
```

### Parallel Processing

Use concurrent processing for independent tasks:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(process_item, items))
```

## Troubleshooting

### Model Not Available

**Issue**: Model not found or deprecated
- **Solution**: Check model availability and update configuration

### Rate Limiting

**Issue**: API rate limits exceeded
- **Solution**: Implement exponential backoff and request queuing

### High Costs

**Issue**: Unexpectedly high API costs
- **Solution**: Use cost tracker, optimize prompts, switch to cheaper models

### Poor Performance

**Issue**: Model not performing well for specific tasks
- **Solution**: Adjust parameters, try different models, improve prompts

## Best Practices

1. **Start with cheaper models** for testing
2. **Monitor costs** regularly using the cost tracker
3. **Use appropriate parameters** for each task type
4. **Cache responses** when possible
5. **Implement error handling** for API failures
6. **Test locally** before deploying to production
7. **Keep API keys secure** and never commit them to version control
8. **Use environment variables** for sensitive configuration
9. **Document your model choices** and reasoning
10. **Regularly review** model performance and costs

## Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [Google Gemini Documentation](https://ai.google.dev/gemini-api/docs)
- [Cohere API Documentation](https://docs.cohere.com)

---

**Last Updated**: 2024-04-26