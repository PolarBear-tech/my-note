import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
