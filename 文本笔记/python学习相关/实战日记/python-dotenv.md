> [!NOTE]
> 这里所有出现的代码几乎都是来自 `python-dotenv`，其他的来源会注明

## **2026-08-14** 19:59: _文档的书写_

`README.md` 当中要简明扼要地引出这个工具解决了什么问题，而非从个人经历谈起，再引出工具内容。

## **2026-08-15** 12:53: _错误的处理_

在某个函数中有多种情况的不同分支，当其中有一个分支出现错误，比如某文件找不到了，尽量不要 raise 一个 error，而是返回和所有分支返回类型相同的一个对象，后续的任何函数在使用到这个函数时就不需要考虑那么多了。

比如：

```python
def _get_stream(self) -> Iterator[IO[str]]:
        if self.dotenv_path and _is_file_or_fifo(self.dotenv_path):
            with open(self.dotenv_path, encoding=self.encoding) as stream:
                yield stream
        elif self.stream is not None:
            yield self.stream
        else:
            if self.verbose:
                logger.info(
                    "python-dotenv could not find configuration file %s.",
                    self.dotenv_path or ".env",
                )
            yield io.StringIO("")  # 这里给出了一个空的字节流，达到了上面的目的
```

## **2026-08-15** 13:27: *`raise err from None`*

- 用户看不懂底层堆栈，造成困惑
- 安全：防止信息泄露（非常重要）
- 抽象层隔离：上层不应该关心底层实现
  上层只应该关心「配置成功 / 失败」，不应该关心失败是因为什么。
  如果底层 API 一换，抛出的异常类型就变；上层代码就会被迫捕获一堆底层异常。
  而封装后：不管底层是 `FileNotFoundError` / `PermissionError` / `UnicodeDecodeError`，对外统一抛出 `ConfigError`，上层只需要捕获 `ConfigError`，不需要关心底层是什么原因。
- 避免误导：底层异常不是真正业务错误

## **2026-08-17** 13:25: 判断是否是交互模式或 `.exe` 文件环境

利用 `sys`的信息，固定模式是`getattr(sys, flag)` 判断是否存在`flag`

- 交互式环境，`ps1`、`ps2`
- 打包的二进制文件，`frozen`

## **2026-08-17** 14:23: 对数据的处理

在大多数情况下，返回整个数据是不太稳妥的，更好的做法是返回一个 generator，这样不会把书记直接加载到内存中，防止数据太多造成程序崩溃。

## **2026-08-21** 18:40: `hash` 值的计算

若明确处理的对象都是一个同一个类，他的 `hash` 值可以仅由其字段产生，但是更佳的写法是：

```python
def __hash__(self) -> int:
    return hash((self.__class__, self.fields))
```