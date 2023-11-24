# Using Langchain with Anthropic Models on Amazon Bedrock

## Sequential calls to LLMs

```mermaid
flowchart LR
    A[Input] --> B[Branch1]
    A --> C[Branch2]
    B --> D[Combine]
    C --> D
```

## Quick Links

- [Langchain Sequential Chains](./anthropic-sequential-chains.ipynb)
- [Multi-prompt Router Chains](./anthropic-router-chains.ipynb)
- [Model kwargs for various Bedrock Models](./utils.py)
