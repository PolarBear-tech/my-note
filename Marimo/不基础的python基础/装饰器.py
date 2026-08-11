import marimo

__generated_with = "0.23.16"
app = marimo.App(css_file="")


@app.cell
def _():
    import marimo as mo
    import time

    return mo, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 装饰器
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 最简单的用法
    """)
    return


@app.cell
def _(time):
    def timer(f):
        def _inner(*args, **kwargs):
            start = time.time()
            f(*args, **kwargs)
            end = time.time()
            return end - start

        return _inner

    return (timer,)


@app.cell
def _(time, timer):
    @timer
    def func():
        time.sleep(1)

    return (func,)


@app.cell
def _(func):
    func()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    这相当于下面的语法糖

    ```python
    func = timer(func)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 带参数的
    """)
    return


@app.cell
def _(time):
    def timer_with_arg(repeat):
        def _timer(f):
            def _inner(*args, **kwargs):
                sum = 0
                for i in range(repeat):
                    start = time.time()
                    f(*args, **kwargs)
                    end = time.time()
                    sum += end - start
                    aver = sum / repeat
                return aver
            return _inner
        return _timer

    return (timer_with_arg,)


@app.cell
def _(time, timer_with_arg):
    @timer_with_arg(10)
    def gunc():
        time.sleep(1)

    return (gunc,)


@app.cell
def _(gunc):
    gunc()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 类与装饰器

    类装饰器：
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
