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
    def dec(func: callable):
        @ft.wraps
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap

    def func(a: int):
        """
        a: an integer
        """
        print(a)

    return


if __name__ == "__main__":
    app.run()
