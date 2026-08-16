Python 代码覆盖率工具。统计**哪些代码被测试跑到了，哪些没跑到**，用来评估 pytest 测试的完备程度。

> 核心原理：运行你的程序时，跟踪每一行是否执行；测试跑完输出报告，看到未覆盖的行、分支。

## ⚠️ 不能用 `uv tool install coverage`

必须作为**项目开发依赖**。

因为它需要和被测 Python 进程同环境运行，全局隔离的 tool 模式统计失效。

```bash
uv add --dev coverage
```

## 常用命令（搭配 pytest）

```bash
# 运行测试，收集覆盖率数据
uv run coverage run -m pytest

# 控制台文本报告
uv run coverage report

# 生成 html 可视化报告，打开 htmlcov/index.html 查看
uv run coverage html
```

`html` 生成网页：绿色 = 执行到；红色 = 没跑；还会标出**未覆盖分支**。

## 配置文件 pyproject.toml 片段

```toml
[tool.coverage.run]
source = ["src"]          # 要统计的源码目录
branch = true             # 开启分支覆盖率（if/else 是否都走到）

[tool.coverage.report]
show_missing = true       # 显示没覆盖到的行号
fail_under = 80           # 覆盖率低于80直接报错，CI很有用
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
]
```

## 两个重要概念

1. **行覆盖率 (line)**：这一行代码有没有被执行
2. **分支覆盖率 (branch)**：`if` 的真、假两个分支是否都走到。

> 只看行覆盖率有迷惑性：一行 `if cond: do()`，行跑到了，但 cond=False 的分支完全没测，行覆盖率依旧 100%，所以建议打开 `branch = true`。

## 常见坑

1. 不要全局装 coverage，**必须项目环境内运行**，否则统计不到你的项目源码；
2. 不要用 `coverage run pytest`，正确写法：`coverage run -m pytest`；
3. 运行前清理旧数据：`uv run coverage erase`，避免上次残留数据干扰。

## 和工具生态配合

- **tox**：可以在每个 tox 测试环境内部跑 coverage；
- pre‑commit：有 `coverage` pre‑commit 钩子；
- CI (GitHub Actions)：上传覆盖率报告到 codecov。