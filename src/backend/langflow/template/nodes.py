from typing import Optional

from langchain.agents import loading
from langchain.agents.mrkl import prompt

from langflow.template.base import FrontendNode, Template, TemplateField
from langflow.utils.constants import DEFAULT_PYTHON_FUNCTION


class ZeroShotPromptNode(FrontendNode):
    name: str = "ZeroShotPrompt"
    template: Template = Template(
        type_name="zero_shot",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value=prompt.PREFIX,
                name="prefix",
            ),
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value=prompt.SUFFIX,
                name="suffix",
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value=prompt.FORMAT_INSTRUCTIONS,
                name="format_instructions",
            ),
        ],
    )
    description: str = "Prompt template for Zero Shot Agent."
    base_classes: list[str] = ["BasePromptTemplate"]

    def to_dict(self):
        return super().to_dict()


class PromptTemplateNode(FrontendNode):
    name: str = "PromptTemplate"
    template: Template
    description: str
    base_classes: list[str] = ["BasePromptTemplate"]

    def to_dict(self):
        return super().to_dict()


class PythonFunctionNode(FrontendNode):
    name: str = "PythonFunction"
    template: Template = Template(
        type_name="python_function",
        fields=[
            TemplateField(
                field_type="code",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                value=DEFAULT_PYTHON_FUNCTION,
                name="code",
            )
        ],
    )
    description: str = "Python function to be executed."
    base_classes: list[str] = ["function"]

    def to_dict(self):
        return super().to_dict()


class ToolNode(FrontendNode):
    name: str = "Tool"
    template: Template = Template(
        type_name="tool",
        fields=[
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value="",
                name="name",
            ),
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value="",
                name="description",
            ),
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value="",
                name="func",
            ),
        ],
    )
    description: str = "Tool to be used in the flow."
    base_classes: list[str] = ["BaseTool"]

    def to_dict(self):
        return super().to_dict()


class JsonAgentNode(FrontendNode):
    name: str = "JsonAgent"
    template: Template = Template(
        type_name="json_agent",
        fields=[
            TemplateField(
                field_type="BaseToolkit",
                required=True,
                show=True,
                name="toolkit",
            ),
            TemplateField(
                field_type="BaseLanguageModel",
                required=True,
                show=True,
                name="llm",
            ),
        ],
    )
    description: str = """Construct a json agent from an LLM and tools."""
    base_classes: list[str] = ["AgentExecutor"]

    def to_dict(self):
        return super().to_dict()


class InitializeAgentNode(FrontendNode):
    name: str = "initialize_agent"
    template: Template = Template(
        type_name="initailize_agent",
        fields=[
            TemplateField(
                field_type="str",
                required=True,
                is_list=True,
                show=True,
                multiline=False,
                options=list(loading.AGENT_TO_CLASS.keys()),
                value=list(loading.AGENT_TO_CLASS.keys())[0],
                name="agent",
            ),
            TemplateField(
                field_type="BaseChatMemory",
                required=False,
                show=True,
                name="memory",
            ),
            TemplateField(
                field_type="Tool",
                required=False,
                show=True,
                name="tools",
                is_list=True,
            ),
            TemplateField(
                field_type="BaseLanguageModel",
                required=True,
                show=True,
                name="llm",
            ),
        ],
    )
    description: str = """Construct a json agent from an LLM and tools."""
    base_classes: list[str] = ["AgentExecutor"]

    def to_dict(self):
        return super().to_dict()

    @staticmethod
    def format_field(field: TemplateField, name: Optional[str] = None) -> None:
        # do nothing and don't return anything
        pass


class CSVAgentNode(FrontendNode):
    name: str = "CSVAgent"
    template: Template = Template(
        type_name="csv_agent",
        fields=[
            TemplateField(
                field_type="file",
                required=True,
                show=True,
                name="path",
                value="",
                suffixes=[".csv"],
                fileTypes=["csv"],
            ),
            TemplateField(
                field_type="BaseLanguageModel",
                required=True,
                show=True,
                name="llm",
            ),
        ],
    )
    description: str = """Construct a json agent from a CSV and tools."""
    base_classes: list[str] = ["AgentExecutor"]

    def to_dict(self):
        return super().to_dict()