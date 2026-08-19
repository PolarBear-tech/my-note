import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import functools as ft
    from timeit import timeit

    return ft, mo, timeit


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
def _(ft, timeit):
    @ft.lru_cache
    def _fib(n: int):
        if n <= 1:
            return n
        return _fib(n-1) + _fib(n - 2)

    @timeit
    def _main():
        print(_fib(100))

    _main()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
