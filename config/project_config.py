import os

from llm.gpt import GPT

os.environ["OPENAI_API_KEY"] = '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'
project = {
    'project_path': "F:\\generate__project\\test",
    'stream': True,
    'user_message': 'console'
}
# 模型
llms = {
    GPT.FLAG: GPT()
}

cur_llm = GPT.FLAG


def set_project_path(path):
    project['project_path'] = path


def get_project_path():
    return project['project_path']
