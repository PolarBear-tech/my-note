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
    def _timeit(f):
        def _inner(*args, **kwargs):
            start = time.time()
            f(*args, **kwargs)
            end = time.time()
            return end - start

        return _inner


    @_timeit
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
    def _timeit(repeat):
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

    @_timeit(3)
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

    - 可以修饰类的装饰器
    - 可以作为装饰器的类
    """)
    return


@app.cell
def _(time):
    class _Timer:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            start = time.time()
            self.func(*args, **kwargs)
            end = time.time()
            return end - start

    @_Timer
    def hunc():
        time.sleep(1)

    return (hunc,)


@app.cell
def _(hunc):
    hunc()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 带参数的类装饰器
    """)
    return


@app.cell
def _(time):
    class _Timer:
        def __init__(self, perfix):
            self.perfix = perfix

        def __call__(self, func):
            def _inner(*args, **kwargs):
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(f"{self.perfix}: {end - start}")
                return ret
            return _inner

    @_Timer("time")
    def lunc():
        time.sleep(0.5)

    return (lunc,)


@app.cell
def _(lunc):
    lunc()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
