import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import dis

    return (dis,)


@app.cell
def _():
    class _A:
        """
        _A
        """
        name = "_A"
        def __init__(self, age: int):
            self.age = age


    print(_A.__dict__)
    _o = _A(10)
    print(_o.__dict__)
    return


@app.cell
def _(dis):
    class _A:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def func(cls):
            print(1)

    dis.dis(_A)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
