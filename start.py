# 获取用户请求
from requirement.user_requirement_handler import UserRequirementHandler

urh = UserRequirementHandler()
user_requirement = urh.get_user_requirement()
# todo 验证用户请求

# 处理用户请求
handle_result = urh.handle_user_requirement(user_requirement)
# 发送处理结果
urh.sendHandleResult(handle_result)
