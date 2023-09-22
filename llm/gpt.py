import os

from langchain.chains.openai_functions import create_structured_output_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    BaseMessage, ChatPromptTemplate, HumanMessagePromptTemplate
)

from config.project_config import project
from llm.llm import LLM

os.environ["OPENAI_API_KEY"] = project['OPENAI_API_KEY']


class GPT(LLM):
    FLAG = "ChatGPT"

    def __init__(self):
        super().__init__()
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k")

    def chat_result(self, stream: bool, *messages: BaseMessage):
        return self.chat(list(messages)).content

    def structured_output(self, schema, *messages: BaseMessage):
        messages = list(messages)
        input_message = messages[-1].content
        messages[-1] = HumanMessagePromptTemplate.from_template('{input}')
        chain_prompt = ChatPromptTemplate.from_messages(messages)
        chain = create_structured_output_chain(schema, self.chat, prompt=chain_prompt, verbose=True)
        return chain.run(input_message)
