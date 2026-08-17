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
    ## 装饰器类
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
    ## 带参数的装饰器类
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 类装饰器

    注意和*装饰器类*做区分
    """)
    return


@app.cell
def _():
    def _add_str(cls):
        def __str__(self):
            return str(self.__dict__)
        cls.__str__ = __str__
        return cls

    @_add_str
    class _A:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    o = _A(1, "str")
    return (o,)


@app.cell
def _(o):
    print(o)
    return


@app.cell(hide_code=True)
def _():
    def _add_str(perfix):
        def _set(cls):
            def __str__(self):
                return perfix + ":" + str(self.__dict__)
            cls.__str__ = __str__
            return cls
        return _set

    @_add_str(perfix="_A")
    class _A:
        def __init__(self, a, b):
            self.a = a
            self.b = b

    p = _A(1, "str")
    return (p,)


@app.cell
def _(p):
    print(p)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
