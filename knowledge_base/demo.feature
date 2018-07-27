Feature: 基本示例

    基本示例

    Scenario: 查询待办列表
        When 我发送请求去获取待办列表
        Then 我应该收到对应的列表信息

    Scenario: 查询待办事项详情
        When 我发送请求去获取待办详情，参数如下
        """
        {
            "id": 1
        }
        """
        Then 我应该收到对应的待办详情

    Scenario: 新增待办事项
        When 我发送请求去新增待办事项，参数如下
        """
        {
            "title": "新增待办",
            "content": "新增待办"
        }
        """
        Then 我应该新增成功

    Scenario: 修改待办事项
        When 我发送请求去修改待办事项，参数如下
        """
        {
            "params": {
                "id": 1
            },
            "data": {
                "title": "修改待办",
                "content": "修改待办"
            }
        }
        """
        Then 我应该修改成功