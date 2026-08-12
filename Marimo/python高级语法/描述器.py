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
    # 描述器

    只要一个类定义了 `__get__`、`__set__`或`__delete__`，它都会成为一个描述器
    """)
    return


@app.cell
def _():
    class Name:
        def __get__(self, obj, objtype):
            return "Peter"

    class A:
        name = Name()

    _o = A()

    print(_o.name)
    print(A.name)
    return (Name,)


@app.cell
def _(Name):
    class B:
        def __init__(self):
            self.name = Name()

    _o = B()
    print(_o.name)
    return


@app.cell
def _(Name):
    class C:
        name = Name()

    _o = C()
    _o.name = "Bob"
    print(_o.name)
    Name.__set__ = lambda x, y, z: None
    print(_o.name)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
