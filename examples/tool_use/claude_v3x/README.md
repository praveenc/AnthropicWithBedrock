# How Tool Use Works (Claude v3)

Integrate external tools with Claude using the following steps:

## 1. Provide Claude with Tools and User Prompt

- Define tools with `names`, `descriptions`, and `input_schemas` in your API request.
- Include a user prompt that might require these tools, e.g., "What's the weather in San Francisco?"

## 2. Claude Decides to Use a Tool

- Claude assesses if any tools can help with the user's query.
- If yes, Claude constructs a properly formatted tool use request.
- The API response has a `stop_reason` of `tool_use`, signaling Claude's intent.

## 3. Extract Tool Input, Run Code, and Return Results

- On your end, extract the tool name and input from Claude's request.
- Execute the actual tool code client-side.
- Continue the conversation with a new user message containing a `tool_result` content block.

## 4. Claude Uses Tool Result to Formulate a Response

- Claude analyzes the tool results to craft its final response to the original user prompt.

---

```mermaid
flowchart TD
%% Nodes
    A(("fa:fa-play Start"))
    B("fa:fa-tools Provide Claude with tools and user prompt")
    C{"fa:fa-question Claude decides: Use a tool?"}
    D("fa:fa-cogs Claude constructs tool use request")
    E("fa:fa-code Extract tool input, run code, return results")
    F("fa:fa-reply Return tool_result to Claude")
    G("fa:fa-brain Claude formulates response without tool")
    H("fa:fa-analytics Claude analyzes tool results")
    I("fa:fa-comment Claude formulates final response")
    J(("fa:fa-flag-checkered End"))

%% Edge connections between nodes
    A --> B --> C
    C -->|Yes| D --> E --> F --> H --> I
    C -->|No| G --> I
    I --> J

%% Individual node styling
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#fbb,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333,stroke-width:2px
    style E fill:#fbf,stroke:#333,stroke-width:2px
    style F fill:#fbf,stroke:#333,stroke-width:2px
    style G fill:#bfb,stroke:#333,stroke-width:2px
    style H fill:#bfb,stroke:#333,stroke-width:2px
    style I fill:#bbf,stroke:#333,stroke-width:2px
    style J fill:#f9f,stroke:#333,stroke-width:2px
```