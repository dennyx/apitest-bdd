Feature: 首页工作台测试集

  测试工作台相关接口

  Scenario: 工作台-通知公告-获取
      When 我发送POST请求，组件为"workbench" key为"GET_NOTIFY_LIST"，请求内容为
      """json
      {}
      """
      Then 我应该获取到正常的返回数据
      And 返回数据"list" 和数据库中的内容一致, sql如下
      """sql
      -- 这个是对应的需要执行的sql
      select 1 from dual
      """
