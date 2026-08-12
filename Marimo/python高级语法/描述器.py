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

    只要一个类定义了 `__get__` ``
    """)
    return


if __name__ == "__main__":
    app.run()
