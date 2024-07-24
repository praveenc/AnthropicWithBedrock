# Building GenAI applications on Amazon Bedrock with Anthropic

## Tool Use with Anthropic LLMs on Amazon Bedrock

### Claudev3 on Amazon Bedrock

- [Tool use with Claudev3 and Amazon Bedrock](./examples/tool_use/claude_v3x/tool_use_claudev3.ipynb)

### Claudev2 Tool Use (Function calling) - Example with prompt engineering (not external packages)

- [How function Calling with Claude works](./examples/tool_use/claude_v2x/README.md)
- [Function Calling with Anthropic_Bedrock py SDK](./examples/tool_use/claude_v2x/anthropic_func_calling.ipynb)
  - [List of functions to be called](./examples/tool_use/claude_v2x/tools.py)

---

## Chaining LLM calls using LangChain with Anthropic models on Amazon Bedrock

- [Langchain Sequential Chains](./examples/langchain-bedrock/sequential-router-chains/anthropic-sequential-chains.ipynb)
- [Langchain Multi-prompt Router Chains](./examples/langchain-bedrock/sequential-router-chains/anthropic-router-chains.ipynb)

## Retrieval Augmented Generation (RAG)

- [RAG with re-ranking Claudev2, Coherev3, Qdrant](./examples/langchain-bedrock/rag_with_bedrock/RAG_with_reranking_claudev2.ipynb)
- [RAG with MultiQuery Retriever Claudev2, Coherev3, Qdrant](./examples/langchain-bedrock/rag_with_bedrock/RAG_with_multiquery_claudev2.ipynb)


## LangChain Agents with Anthropic Claude

- [Enhancing LLM calls with External tools](./examples/langchain-bedrock/agents_with_anthropic/search_agents_with_claude.ipynb)

## Quick Links

- [Common `utils.py` file](./examples/langchain-bedrock/utils/utils.py)

## Contribution

Contributions to this repository are welcome. Please ensure you follow the [contribution guidelines](../CONTRIBUTING.md) when submitting pull requests.

## Feedback

If you have any feedback or encounter issues, please open an issue in the repository, and we will address it promptly.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
