import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # `__init_subclass__`
    """)
    return


@app.cell
def _():
    class _Base:
        def __init_subclass__(cls, name):
            cls.dict_ = {}
            cls.name = name

    class _A(_Base, name="Jack"):
        pass


    print(_A.dict_)
    print(_A.name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__set_name__`
    """)
    return


@app.cell
def _():
    class _D:
        def __set_name__(self, owner, name):
            print(owner, name)

    class _A:
        x = _D()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__mro_entries__`
    """)
    return


@app.cell
def _():
    class _A:
        def __mro_entries__(self, bases):
            print(bases)
            return ()

    class _B(_A()):
        pass

    print(issubclass(_B, _A))
    return


@app.cell
def _():
    class _A:
        def __mro_entries__(self, bases):
            print(bases)
            return (_A,)

    class _B(_A()):
        pass

    print(issubclass(_B, _A))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # `__prepare__`
    """)
    return


@app.cell
def _():
    class _Meta(type):
        @classmethod
        def __prepare__(cls, name, bases, **kwds):
            print(name, bases, kwds)
            return {}

    class _A(metaclass=_Meta):
        pass

    return


@app.cell
def _():
    class _Meta(type):
        @classmethod
        def __prepare__(cls, name, bases, **kwds):
            return {"x": 10}

    class _A(metaclass=_Meta):
        pass

    _A.x
    return


if __name__ == "__main__":
    app.run()
