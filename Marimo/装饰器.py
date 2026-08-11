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
        def inner(*args, **kwargs):
            start = time.time()
            f(*args, **kwargs)
            end = time.time()
            return end - start

        return inner

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


app._unparsable_cell(
    r"""
    def timer_with_arg(repeat):
        def timer(f):
            def inner():
            
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
