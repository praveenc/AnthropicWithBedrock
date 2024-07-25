# Building GenAI applications on Amazon Bedrock with Anthropic

## Tool Use with Anthropic LLMs on Amazon Bedrock

Refer [here](./examples/tool_use/claude_v3x/README.md) on how tool use works.

- [Tool use with Claudev3 and Amazon Bedrock](./examples/tool_use/claude_v3x/api_calls/tool_use_claudev3.ipynb)\
Demonstrate calling python functions with `tool_use` params.
  - [`calculator`](./examples/tool_use/claude_v3x/api_calls/tools_claudev3.py) function to perform arthimetic operations
  - [`get_lat_long`](./examples/tool_use/claude_v3x/api_calls/tools_claudev3.py) and [`get_weather`](./examples/tool_use/claude_v3x/api_calls/tools_claudev3.py) functions to get current weather information.



- [Get structured output with Tool use](./examples/tool_use/claude_v3x/structured_output/tool_use_structured_output.ipynb)\
Demonstrate extracting structured output for the following use-cases
   1. **Text Summarization**
   2. **Named Entity Recognition**
   3. **Sentiment Analysis**
   4. **Text Classification**

---

### Claudev2 Tool Use (Function calling) - Example with prompt engineering (not external packages)

- [How Tool use (function calling) works in Claude v2.x](./examples/tool_use/claude_v2x/README.md)
- [Tool use with Claude v2.x models on Anthropic_Bedrock Notebook](./examples/tool_use/claude_v2x/anthropic_func_calling.ipynb)
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
