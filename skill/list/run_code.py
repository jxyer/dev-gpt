from agent import EXTRA_TYPE_NONE, Message
from config.project_config import project
from context import MessageContext
from skill.list.code_interpreter import CodeInterpreter
from skill.list.interrupt_skill import InterruptSkill
from skill.list.skill import send_robot_message


class RunCode(CodeInterpreter, InterruptSkill):
    FLAG = '运行代码'

    def describe(self) -> str:
        return "当用户需求完成后，可以选择这个技能。"

    async def act(self, messageManager) -> Message:
        self.interpreter.reset()
        self.interpreter.load(
            [{"role": "user", "content": msg.content}
             if index % 2 == 0 else {"role": "assistant", "content": msg.content}
             for index, msg in enumerate(MessageContext.message_record[0:-1])])

        requirement = MessageContext.message_record[-1].content if len(MessageContext.message_record) > 0 else ''
        message = f"""
            {requirement},
            你只需要去根据代码文件路径去运行代码。
            用户的项目路径为：{project['project_path']},
        """
        self.interpreter.chat(message)
        return await send_robot_message(messageManager, '成功执行', EXTRA_TYPE_NONE, [])
