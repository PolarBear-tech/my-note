import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import functools as ft

    return ft, mo


@app.cell
def _(mo):
    mo.md("""
    # functools
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `lru_cache`
    """)
    return


@app.cell
def _(ft):
    @ft.lru_cache
    def _fib(n: int):
        if n <= 1:
            return n
        return _fib(n-1) + _fib(n - 2)

    _fib(50)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `partial`
    """)
    return


@app.cell
def _(ft):
    def _pow(a: int, b: int) -> int:
        return a ** b

    _square = ft.partial(_pow, b=2)
    _square(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `reduce`
    """)
    return


@app.cell
def _(ft):
    import operator

    ft.reduce(operator.add, range(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `cmp_to_key`
    """)
    return


@app.cell
def _(ft):
    print(sorted([1,6,4,5,3], key=ft.cmp_to_key(lambda a, b: a - b)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `wraps`
    """)
    return


@app.cell
def _(ft):
    def _dec(func: callable):
        @ft.wraps(func)
        def wrap(*args, **kwargs):
            print("in wrap")
            return func(*args, **kwargs)
        return wrap

    @_dec
    def _func(a: int):
        """a: an integer"""
        print(a)
        return a + 1

    print(_func(1))
    print(_func.__doc__)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## total_ordering
    """)
    return


@app.cell
def _(ft):
    @ft.total_ordering
    class _A:
        def __init__(self, v: int):
            self.v = v

        def __lt__(self, other):
            return self.v < other.v

        def __eq__(self, other):
            return self.v == other.v

        def __hash__(self):
            return hash((self.v,))

    _one = _A(1)
    _two = _A(2)

    print(_one <= _two)
    print(_one > _two)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## `singledispatch`
    """)
    return


@app.cell
def _(ft):
    @ft.singledispatch
    def _func(x):
        print("default:", x)


    @_func.register
    def _(x: int):
        print("int:", x)

    @_func.register
    def _(x: str):
        print("str:", x)

    _func(12)
    _func("12")
    _func(12j)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
