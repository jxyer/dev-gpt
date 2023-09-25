import asyncio

from requirement.user_requirement_handler import UserRequirementHandler


async def run():
    urh = UserRequirementHandler()
    # 获取用户请求
    user_requirement = await urh.get_user_requirement()
    # todo 验证用户请求

    # 处理用户请求
    handle_result = await urh.handle_user_requirement(user_requirement)
    # 发送处理结果
    urh.sendHandleResult(handle_result)


if __name__ == '__main__':
    asyncio.run(run())
