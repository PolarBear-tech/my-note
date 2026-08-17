import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    class _A:
        def __new__(cls):
            print("__new__")
            return super().__new__(cls)
        
        def __init__(self):
            print("__init__")

    _o = _A()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 什么时候需要用new呢

    需要客制化建立object时，才需要使用，比如设置成单例模式
    """)
    return


if __name__ == "__main__":
    app.run()
