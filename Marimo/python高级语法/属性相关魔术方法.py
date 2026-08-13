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


@app.cell
def _():
    class _A:
        def __init__(self, data):
            self.data = data
            self.counter = 0

        def __getattribute__(self, name):
            if name == "data":
                self.counter += 1
            return super().__getattribute__(name)

    _o = _A("data_")
    _o.data
    _o.data
    _o.counter
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__setattr__`
    """)
    return


@app.cell
def _():
    class _A:
        def __init__(self, name):
            self.name = name

        def __setattr__(self, name, value):
            print(f"{name}: {value}")
            super().__setattr__(name, value)

    _o = _A("Li")
    return


@app.cell
def _():
    class _A:
        _attr = {}

        def __init__(self):
            self.data = "abc"

        def __getattr__(self, name):
            if name in self._attr:
                return self._attr[name]
            raise AttributeError

        def __setattr__(self, name, val):
            self._attr[name] = val

    _o1 = _A()
    _o2 = _A()
    _o1.data = "xyz"
    _o2.data
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__delattr__`
    """)
    return


@app.cell
def _():
    class _A:
        def __init__(self):
            self.data = "abc"

        def __delattr__(self, name):
            print(f"del {name}")
            super().__delattr__(name)

    _o = _A()
    del _o.data
    # print(_o.data)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
