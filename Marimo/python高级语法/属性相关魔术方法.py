import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__getattr__`
    """)
    return


@app.cell
def _():
    class _A:
        def __init__(self, data):
            self.data = data

        def __getattr__(self, name):
            print(f"getting {name}")
            return f"{name}_"

    _o = _A("data_")
    print(_o.data)
    print(_o.test)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__getattribute__`
    """)
    return


app._unparsable_cell(
    r"""
    class _A:
        def __init__(self, data):
            self.data = data
            self.counter = 0

        def __getattribute__(self, name):
            if name == "data":
                self.counter += 1
            return super().)__geta
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
