from llm.gpt import GPT

project = {
    'project_path': "F:\\generate__project\\test",
    'stream': True,
    'OPENAI_API_KEY':'sk-xxx'
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