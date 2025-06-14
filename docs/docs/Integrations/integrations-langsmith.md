---
title: LangSmith
slug: /integrations-langsmith
---



LangSmith is a full-lifecycle DevOps service from LangChain that provides monitoring and observability. To integrate with Aiexec, add your LangChain API key and configuration as Aiexec environment variables, and then start Aiexec.

1. Obtain your LangChain API key from [https://smith.langchain.com](https://smith.langchain.com/)
2. Add the following keys to the Aiexec .env file.
Replace `LANGCHAIN_API_KEY` and `LANGSMITH_PROJECT_NAME` with your LangChain API key.

```text
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com/
LANGSMITH_API_KEY=LANGCHAIN_API_KEY
LANGSMITH_PROJECT=LANGSMITH_PROJECT_NAME
```

Alternatively, export the environment variables in your terminal:

`export LANGSMITH_TRACING=true && export LANGSMITH_ENDPOINT="https://api.smith.langchain.com/" && export LANGSMITH_API_KEY="LANGCHAIN_API_KEY" && export LANGSMITH_PROJECT="LANGSMITH_PROJECT_NAME"`

3. Restart Aiexec using `aiexec run --env-file .env`
4. Run a project in Aiexec.
5. View the Langsmith dashboard for monitoring and observability.

![](/img/langsmith-dashboard.png)

