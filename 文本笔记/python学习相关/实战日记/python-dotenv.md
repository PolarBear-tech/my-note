> 这里所有出现的代码几乎都是来自`python-dotenv`，其他的来源会注明
## **2026-08-14** 19:59: _文档的书写_

`README.md` 当中要简明扼要地引出这个工具解决了什么问题，而非从个人经历谈起，再引出工具内容。
## **2026-08-15** 12:53: _错误的处理_

在某个函数中有多种情况的不同分支，当其中有一个分支出现错误，比如某文件找不到了，尽量不要raise一个error，而是返回和所有分支返回类型相同的一个对象，后续的任何函数在使用到这个函数时就不需要考虑那么多了。

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