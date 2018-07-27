# 接口测试

## 简介

* 自动化基本框架：基于python + selenium + behave(BDD) + allure(报告)实现
* 此项目使用python版本3.6

## 自动化实现目标

* 覆盖主要功能
* 可读性强的代码、报告
* 定时执行，发送测试报告
* 生成测试覆盖率报告 -- 以M侧管理端为主，对应工具jacoco

## Dependency

* pip install -r requirements.txt
* 如果自己有新增加依赖，则安装完依赖后，在接口测试根目录下，使用以下命令来更新requirements.txt文件

```shell
pip freeze > requirements.txt
```

## 前提条件

* powershell 执行如下命令，安装allure

```shell
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
scoop install allure
```

## 基本结构

* report/ allure_result/  临时报告目录
* download/ 临时下载目录
* features feature文件目录
* knowledge_base 知识储备
    * feature_example feature文件常用示例，作为学习参考库，便于快速定位
    * step_example step常用示例，作为学习参考库，便于快速定位
* steps 步骤定义文件目录
* utils 常用工具目录
* environment.py 世界文件，脚本生命周期管理
* config_template.py 配置模板，每个人根据自己的需求，复制一份config.py文件
* behave.ini behave基础配置文件
* enums - 存放返回数据中，所有的enum信息，如code, message等

## 执行测试步骤

* 安装虚拟环境

```shell
# 安装虚拟环境
python -m venv ./venv
# 激活虚拟环境
source venv/bin/activate
```

* 安装依赖

```shell
pip install -r requirements.txt
```

* 安装allure，参见上面前提条件
* 复制config_template.py为config.py，并调整对应参数
* powershell中执行以下命令，执行测试

```shell
behave -f allure_behave.formatter:AllureFormatter -o report ./features
```

* powershell中执行以下命令，执行失败测试用例

```shell
behave '@rerun_failing.features'
```

* powershell中执行以下命令，讲报告转化

```shell
allure generate report -o allure_report --clean
```

* powershell中执行以下命令，将报告放到http服务中

```shell
allure open allure_report
```

* 访问终端的链接，查看报告
* 查看日志 credit_test.log

## Git 提交步骤（同一个branch）

* 查看本地更新的代码
* commit需要提交的内容，到本地仓库
* git pull
* 查看其他人提交的内容
* 处理merge，如果存在的话
* 查看提交的内容
* git push

## 常用命令

* behave执行指定feature文件

```shell
behave -f allure_behave.formatter:AllureFormatter -o report .\features\workbench\workbench.feature -t DEBUG
```

* allure集成命令

```shell
allure serve report
```

## 约定TAG

* NEED_LOGIN 需要登录
* REGRESSION_TEST 回归测试用例
* SMOKE_TEST 冒烟测试用例
* KNOWN_BUG_* 已知BUG, *表示bug id用于报告中跟踪定位

## VisualStudioCode插件

* Cucumber (Gherkin) Syntax and Snippets -- cucumer 语法检查
* Studio Icons -- 文件icon化
* TODO Highlight -- 文件中的TODO高亮显示
* markdownlint markdown语法检查
* Git History 查看git文件变更历史
* python

## FQA

* 脚本执行失败，怎么去定位失败原因
> 在执行终端中查看，是否有关键性错误信息
> 在credit_test.log中查看，是否有关键性错误信息；如果没有，手动增加信息；

## 参考文档

* 接口文档： credit-anhui-document/06-内部接口设计/M侧管理端模块
* [behave官网及帮助手册等](http://behave.readthedocs.io/en/latest/)
* [behave示例项目](https://github.com/behave/behave.example)
* [allure官网及帮助手册等](http://allure.qatools.ru/)
* [推荐使用visual studio code作为开发工具](https://code.visualstudio.com/)