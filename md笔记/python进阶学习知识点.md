# Python 进阶学习路线 & 去哪里学

> 前提：基础已经过关：会语法、循环条件、函数、类、异常、文件操作、模块包，能写小脚本。进阶不再学语法，而是**底层原理、工程能力、高性能、生态库、架构思维**。

## 一、进阶核心学什么（重点清单）

### 1. Python 语言内核（必学）

- 高级语法：装饰器、生成器、迭代器、上下文管理器、闭包、*args/**kwargs、元类 metaclass
- 内存模型：变量引用、深浅拷贝、垃圾回收 GC、小整数池、GIL 全局解释器锁
- 并发编程：多线程、多进程、协程 asyncio，IO 密集 vs CPU 密集选型
- 模块与包：import 机制、`__init__.py`、相对导入、setup/pyproject.toml 打包发布

### 2. 工程化能力（工作最常用）

- 虚拟环境：venv /poetry/pipenv，依赖管理
- 类型注解 typing，mypy 静态类型检查
- 代码规范：flake8、ruff，格式化 black
- 单元测试 pytest，mock
- Git + pre‑commit 工作流
- 日志 logging、配置文件、异常处理最佳实践

### 3. 高性能 & 底层

- CPython 简单原理，性能分析 cProfile
- C 扩展基础 / Cython /ctypes
- 数据结构：collections、itertools，理解时间复杂度
- numpy 底层原理（如果做数据方向）

### 4. 方向分支（选一个深耕）

1. **后端开发**：FastAPI / Django，ORM，异步，接口设计
2. **数据分析 AI**：numpy/pandas，pytorch
3. **自动化脚本工具**：cli 开发 click/typer
4. **爬虫**：aiohttp 异步爬虫

---

## 二、学习资源（免费 + 付费，分网站 / 书籍）

### 📚 书籍（进阶首选，体系完整）

1. 《流畅 Python Fluent Python》✅ **进阶圣经，必看**，讲 Pythonic 写法、高级语法、并发
2. 《Python Cookbook》大量工程实战案例
3. 《Python 高性能编程》讲 GIL、性能优化
4. 《CPython 源码剖析》想啃底层虚拟机看这本

### 🆓 免费线上学习站点

1. **官方文档**

    [https://docs.python.org/zh-cn/3/](https://link.wtturl.cn/?target=https%3A%2F%2Fdocs.python.org%2Fzh-cn%2F3%2F&scene=im&aid=582478&lang=zh "autolink")

    进阶最重要的资料，很多人忽略，看语言参考、库参考。

2. 菜鸟教程不适合进阶，跳过。

3. B 站高质量进阶

- 李沐 Python 进阶（讲性能、GIL、并发）
- 鱼皮 Python 进阶工程化（虚拟环境、pytest、项目实战）
- 莫烦 python（适合数据分析方向）

4. 开源项目实战（最重要！进阶不能只看视频）

> 进阶关键：读别人写的成熟 Python 源码

- FastAPI 源码、requests 源码、pytest 源码
- github 搜小型高质量 python 项目，clone 下来读、改 bug、提交 PR

### ✨ 付费课程（可选）

- 极客时间《Python 核心技术与实战》，工程向，适合想提升工作能力
- 掘金小册：Python 进阶、asyncio 实战

## 三、进阶正确学习方式（避坑）

❌ 不要继续刷基础语法练习题

✅ 模式：**知识点 + 动手写小项目 + 读源码**

举几个进阶练手小项目：

1. 自己手写简易装饰器、简易 ORM
2. asyncio 写异步爬虫
3. 用 pytest 给自己写的脚本写单元测试
4. 把自己写的工具打包成 pip 可安装包

## 四、学习顺序建议

1. 先搞定：装饰器、生成器、上下文管理器 →《流畅 Python》前半部分
2. 再学：并发（线程 / 进程 /asyncio）
3. 工程化：类型注解、pytest、poetry、ruff
4. 了解 GIL、GC 内存原理
5. 选定业务方向（后端 / AI / 自动化）做实战项目