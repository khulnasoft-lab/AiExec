from aiexec.components.data import FileComponent
from aiexec.components.input_output import ChatInput, ChatOutput
from aiexec.components.languagemodels import OpenAIModelComponent
from aiexec.components.processing import ParserComponent
from aiexec.components.prompts import PromptComponent
from aiexec.graph import Graph


def document_qa_graph(template: str | None = None):
    if template is None:
        template = """Answer user's questions based on the document below:

---

{Document}

---

Question:
{Question}

Answer:
"""
    file_component = FileComponent()
    parse_data_component = ParserComponent()
    parse_data_component.set(input_data=file_component.load_files)

    chat_input = ChatInput()
    prompt_component = PromptComponent()
    prompt_component.set(
        template=template,
        context=parse_data_component.parse_combined_text,
        question=chat_input.message_response,
    )

    openai_component = OpenAIModelComponent()
    openai_component.set(input_value=prompt_component.build_prompt)

    chat_output = ChatOutput()
    chat_output.set(input_value=openai_component.text_response)

    return Graph(start=chat_input, end=chat_output)
