# 小型高质量 Python 开源项目

筛选标准：**代码量不大 (几百～几千行)、架构干净、文档完善、适合阅读学习、无过度复杂业务**，适合读源码、模仿写法，甚至改改提交 PR。

分为：工具库、web、cli 命令行、底层小框架。

> 阅读小技巧：
>
> 1. 先看 `pyproject.toml`，了解依赖、打包配置
> 2. 看 `tests/` 单元测试，快速看懂 API 怎么用
> 3. 从 `__init__.py` 入口顺着读

## 🔧 通用工具库（最适合入门读源码）

### 1. httpx

- github：[https://github.com/encode/httpx](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Fencode%2Fhttpx&scene=im&aid=582478&lang=zh "autolink")
- 代码规模：几千行
- 学习点：同步 / 异步兼容设计、类型注解、requests 级别的 http 客户端、优雅的异常处理、测试用例组织。

> 比 requests 代码更现代，大量 typing，学习如何同时支持 sync/async。

### 2. python-dotenv

- github：[https://github.com/theskumar/python-dotenv](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Ftheskumar%2Fpython-dotenv&scene=im&aid=582478&lang=zh "autolink")
- 代码规模：几百行，非常小
- 学习点：读取.env 环境变量文件，解析文本、环境变量处理、跨平台兼容、简单的包结构。

> **新手读源码首选，体量极小，逻辑清晰。**

### 3. pydantic v1（别看 v2，v2 大量 rust）

- github：[https://github.com/pydantic/pydantic/tree/1.10.x](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Fpydantic%2Fpydantic%2Ftree%2F1.10.x&scene=im&aid=582478&lang=zh "autolink")
- 学习点：数据校验、模型类、元类使用、类型注解解析。v1 全部 python 实现，v2 内核是 Rust 不适合读 Python 源码。

## 🖥️ CLI 命令行工具项目

### 4. typer

- github：[https://github.com/tiangolo/typer](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Ftiangolo%2Ftyper&scene=im&aid=582478&lang=zh "autolink")
- 代码量：一千多行
- 学习点：基于类型注解做命令行解析，装饰器封装，命令行框架设计。作者就是 FastAPI 作者，代码风格极度优雅。

> 看完可以模仿写自己的 CLI 小工具。

### 5. rich

- github：[https://github.com/Textualize/rich](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2FTextualize%2Frich&scene=im&aid=582478&lang=zh "autolink")
- 代码量：几千行
- 学习点：终端美化、控制台渲染、表格进度条、ANSI 终端处理。适合学习复杂终端输出库如何分层设计。

## 🌐 Web / 异步相关

### 6. starlette（FastAPI 底层）

- github：[https://github.com/encode/starlette](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Fencode%2Fstarlette&scene=im&aid=582478&lang=zh "autolink")
- 代码规模：两千多行
- 学习点：ASGI 异步 web 框架核心，中间件设计、请求响应模型、路由、websocket。FastAPI 只是在 starlette 之上封装。

> 想学异步 web 不要直接啃 FastAPI，先读 starlette。

### 7. itsdangerous

- github：[https://github.com/pallets/itsdangerous](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Fpallets%2Fitsdangerous&scene=im&aid=582478&lang=zh "autolink")
- 几百行
- 学习点：签名序列化、token 生成，Flask 依赖的库。加密、序列化、异常处理，短小精悍。

## 🧪 测试 & 工具类

### 8. pluggy

- github：[https://github.com/pytest-dev/pluggy](https://link.wtturl.cn/?target=https%3A%2F%2Fgithub.com%2Fpytest-dev%2Fpluggy&scene=im&aid=582478&lang=zh "autolink")
- 一千行左右
- 学习点：**插件系统架构**，pytest 的底层核心。如何实现钩子、插件注册、扩展机制。非常经典的设计模式案例。

## ✍️ 适合动手改的练手项目（可以 fork 改 bug、加小功能）

1. `python‑dotenv`：可以尝试加一个小解析规则，练手打包发布
2. `typer`：一些简单 issue，适合新手提交 PR
3. `pluggy`：理解插件模式，可以模仿写一个自己小型插件框架

---

# 阅读顺序建议（由易到难）

1. **python‑dotenv**（几百行，最简单）
2. **itsdangerous**（加密序列化）
3. **typer**（装饰器 + 类型注解）
4. **pluggy**（插件架构）
5. **starlette**（异步 web、中间件）
6. **httpx**（同步异步兼容）

# 练习任务（读完一个项目可以做）

1. 模仿项目的目录结构，自己仿写一个迷你版：

- 仿写迷你 dotenv：实现读取.env，注入 os.environ
- 仿写迷你 typer：实现简单装饰器命令行
- 仿写迷你 pluggy：实现简易插件钩子系统