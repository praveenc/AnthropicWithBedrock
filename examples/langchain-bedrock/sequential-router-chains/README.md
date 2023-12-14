# Using Langchain with Anthropic Models on Amazon Bedrock

## Sequential calls to LLMs

```mermaid
flowchart LR
    A[Input] --> B[Branch1]
    A --> C[Branch2]
    B --> D[Combine]
    C --> D
```

Refer to notebook: [Langchain Sequential Chains](./anthropic-sequential-chains.ipynb)

## Classify and Route questions to various Prompts

```mermaid
flowchart TB
    A[User Input] --> B[Classifier Prompt]
    B -->|Math| C[Math Prompt Chain]
    B -->|Physics| D[Physics Prompt Chain]
    B -->|Computer Science| E[Computer Science Prompt Chain]
    B -->|History| F[History Prompt Chain]
    B -->|General| G[General Prompt Chain]
    C --> H[Output]
    D --> H
    E --> H
    F --> H
    G --> H
```

Refer to notebook: [Multi-prompt Router](./anthropic-router-chains.ipynb)

> [!WARNING]
> The above notebooks also contain *LEGACY* implementations only for demonstration purposes. LCEL is the preffered way.

### Quick Links

- [Model kwargs for various Bedrock Models](../utils/utils.py)
