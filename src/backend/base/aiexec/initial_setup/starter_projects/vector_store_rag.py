from textwrap import dedent

from aiexec.components.data import FileComponent
from aiexec.components.embeddings import OpenAIEmbeddingsComponent
from aiexec.components.input_output import ChatInput, ChatOutput
from aiexec.components.languagemodels import OpenAIModelComponent
from aiexec.components.processing import ParserComponent
from aiexec.components.processing.split_text import SplitTextComponent
from aiexec.components.prompts import PromptComponent
from aiexec.components.vectorstores import AstraDBVectorStoreComponent
from aiexec.graph import Graph


def ingestion_graph():
    # Ingestion Graph
    file_component = FileComponent()
    text_splitter = SplitTextComponent()
    text_splitter.set(data_inputs=file_component.load_files)
    openai_embeddings = OpenAIEmbeddingsComponent()
    vector_store = AstraDBVectorStoreComponent()
    vector_store.set(
        embedding_model=openai_embeddings.build_embeddings,
        ingest_data=text_splitter.split_text,
    )

    return Graph(file_component, vector_store)


def rag_graph():
    # RAG Graph
    openai_embeddings = OpenAIEmbeddingsComponent()
    chat_input = ChatInput()
    rag_vector_store = AstraDBVectorStoreComponent()
    rag_vector_store.set(
        search_query=chat_input.message_response,
        embedding_model=openai_embeddings.build_embeddings,
    )

    parse_data = ParserComponent()
    parse_data.set(input_data=rag_vector_store.search_documents)
    prompt_component = PromptComponent()
    prompt_component.set(
        template=dedent("""Given the following context, answer the question.
                         Context:{context}

                         Question: {question}
                         Answer:"""),
        context=parse_data.parse_combined_text,
        question=chat_input.message_response,
    )

    openai_component = OpenAIModelComponent()
    openai_component.set(input_value=prompt_component.build_prompt)

    chat_output = ChatOutput()
    chat_output.set(input_value=openai_component.text_response)

    return Graph(start=chat_input, end=chat_output)


def vector_store_rag_graph():
    return ingestion_graph() + rag_graph()
