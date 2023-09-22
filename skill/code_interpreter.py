from abc import ABC

import interpreter

from .skill import Skill


class CodeInterpreter(Skill, ABC):

    def __init__(self):
        super().__init__()
        interpreter.auto_run = True
        interpreter.model = "gpt-3.5-turbo-16k-0613"
        interpreter.temperature = 0
        interpreter.api_key = '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'
        self.interpreter = interpreter
